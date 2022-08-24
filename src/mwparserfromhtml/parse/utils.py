from bs4 import Comment  # for parsing the HTML
from .const import NAMESPACES


def is_comment(element) -> bool:
    return isinstance(element, Comment)


def is_wikilink(tag_string):
    return (
        tag_string.name == "a"
        and tag_string.has_attr("rel")
        and "mw:WikiLink" in tag_string["rel"]
    )


def is_category(tag_string):
    return (
        tag_string.name == "link"
        and tag_string.has_attr("rel")
        and "mw:PageProp/Category" in tag_string["rel"]
    )


def is_external_link(tag_string):
    return (
        tag_string.name == "a"
        and tag_string.has_attr("rel")
        and "mw:ExtLink" in tag_string["rel"]
    )


def is_heading(tag_string):
    return tag_string.name in ["h2", "h3", "h4", "h5", "h6"]


def is_stub(tag_string):
    return (
        tag_string.name == "p"
        and tag_string.has_attr("class")
        and "asbox-body" in tag_string["class"]
    )


def nested_value_extract(key, var):
    """
    function to extract the value of all occurances of a specific key from a nested dictionary
    """
    if hasattr(var, "items"):
        for k, v in var.items():
            if k == key:
                if v != "":
                    yield v
            if isinstance(v, dict):
                for result in nested_value_extract(key, v):
                    if result != "":
                        yield result
            elif isinstance(v, list):
                for d in v:
                    for result in nested_value_extract(key, d):
                        if result != "":
                            yield result


def title_normalization(link):
    try:
        # strip everything before the first ":" as a naive way to strip namespace information i.e: "Category" in this case
        return link.split(":", 1)[1].replace("_", " ")
    except Exception as e:
        return link


def get_namespaces():
    """
    Utility for generating NAMESPACES dictionary found in const.py.

    Not intended to be called from code but to be occasionally run locally and used to manually update NAMESPACES.
    """
    import re
    import requests
    import time

    def get_wikipedia_sites():
        session = requests.Session()
        base_url = "https://meta.wikimedia.org/w/api.php"
        params = {
            "action": "sitematrix",
            "smlangprop": "|".join(["code", "site"]),
            "smsiteprop": "|".join(["url"]),
            "format": "json",
            "formatversion": "2",
        }
        result = session.get(url=base_url, params=params)
        result = result.json()

        wiki_languages = set()
        # ^: start of string
        # (?<=...): match https:// but don't keep
        # (...): match wiki language and keep
        # (?=...): match .wikipedia.org but don't keep
        # $ end of string
        wikipedia_pat = re.compile(r"(?<=^https://)([a-z\-]*)(?=.wikipedia.org$)")
        if "sitematrix" in result:
            for lang in result["sitematrix"]:
                try:
                    int(lang)  # weirdly, wikis are keyed as numbers in the results
                    for wiki in result["sitematrix"][lang].get("site", []):
                        if "closed" not in wiki:
                            is_wikipedia = wikipedia_pat.search(wiki["url"])
                            if is_wikipedia:
                                wiki_languages.add(is_wikipedia.group())
                                break
                except ValueError:  # skip count metadata and special wikis
                    continue
        return sorted(wiki_languages)

    def get_namespace_prefix_map(lang):
        """Get official mapping of namespace names to IDs for a wiki -- e.g., Talk:1

        This ignores aliases as the HTML dumps standardize the namespace prefixes on links.
        NOTE: this data can alternatively be extracted from the dumps:
        <lang>-<date>-siteinfo-namespaces.json.gz
        """
        session = requests.Session()
        base_url = "https://{0}.wikipedia.org/w/api.php".format(lang)
        params = {
            "action": "query",
            "meta": "siteinfo",
            "siprop": "namespaces",
            "format": "json",
            "formatversion": "2",
        }
        result = session.get(url=base_url, params=params)
        result = result.json()

        namespaces = {}
        if "namespaces" in result.get("query", {}):
            for ns in result["query"]["namespaces"].values():
                # skip main namespace -- no prefixes
                if ns.get("name"):
                    namespaces[ns["name"]] = ns["id"]
        return namespaces

    wiki_languages = get_wikipedia_sites()
    print(f"{len(wiki_languages)} languages: {wiki_languages}")
    NAMESPACES = {}
    for lang in wiki_languages:
        NAMESPACES[lang] = get_namespace_prefix_map(lang)
        time.sleep(0.5)
    print(NAMESPACES)


def get_tid(tag_string):
    """
    Utility for extracting the id of an element from a HTML string.
    """
    return tag_string["about"] if tag_string.has_attr("about") else None


def check_transclusion(tag_string):
    """
    Utility for checking if an element is transcluded on the web page.
    """
    if tag_string.has_attr("about") and tag_string["about"].startswith("#mwt"):
        return True
    return False


def map_namespace(href, wiki_db) -> int:
    """
    returns the namespace id of a namespace type (i.e: article, talks etc.)
    """
    try:
        namespace_type = href.split(":")[0].strip("./").replace("_", " ")
        namespace_id = NAMESPACES[wiki_db][namespace_type]
        return namespace_id
    except Exception as e:
        return 0


def identify_elements_(tag_string):
    """
    utility function that returns an instance of the identified object
    """
    from .elements import (
        Element,
        Wikilink,
        Category,
        ExternalLink,
    )  # to prevent circular/mutual import

    if is_category(tag_string):
        return Category(tag_string)
    if is_wikilink(tag_string):
        return Wikilink(tag_string)
    if is_external_link(tag_string):
        return ExternalLink(tag_string)
    else:
        return Element(tag_string)


def dfs(
    parent_node,
    skip_transclusion=False,
    skip_headers=False,
    skip_categories=False,
):
    """
    recursive depth-first search function to traverse the HTML tree
    returns generator for plaintext of each node.
    """
    for cnode in parent_node.contents:
        if hasattr(cnode, "attrs"):  # if node has attributes, check the attributes
            tag_obj = identify_elements_(cnode)
            nested_transclusion = skip_transclusion and tag_obj.transclusion
            ## don't have to explicitly check for comments

            if nested_transclusion:
                continue
            elif is_heading(cnode):
                if skip_headers:
                    continue
                yield cnode.text
            elif tag_obj.name in ["Wikilink", "ExternalLink", "Category"]:
                if skip_categories and tag_obj.name == "Category":
                    continue
                else:
                    yield tag_obj.plaintext if len(
                        tag_obj.plaintext
                    ) > 0 else tag_obj.title

            else:
                for pt in dfs(
                    cnode,
                    skip_transclusion=skip_transclusion,
                    skip_categories=skip_categories,
                    skip_headers=skip_headers,
                ):
                    yield pt
        # Raw string -- output
        else:
            yield cnode.text


def get_metadata(body):
    # the NON_KEYS array contains the keys which has already been defined
    # within the article class by extracting directly from the HTML.
    # That's why we don't redundantly include them in the metadata.
    NON_KEYS = ["article_body", "url", "namespace", "name", "in_language"]
    metadata = {}
    for k in body.keys():
        if k not in NON_KEYS:
            metadata[k] = body.get(k)
    return metadata
