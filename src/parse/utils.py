from bs4 import Comment  # for parsing the HTML


def is_comment(element):
    return isinstance(element, Comment)


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


def flatten_list(A):
    rt = []
    for i in A:
        if isinstance(i, list):
            rt.extend(flatten_list(i))
        else:
            if i.strip() != "":
                rt.append(i)
    return rt


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

def get_id(html_string):
    """
    Utility for extracting the id of an element from a HTML string.
    """
    return html_string["about"] if html_string.has_attr("about") else None

def check_transclusion(html_string):
    """
    Utility for checking if an element is transcluded on the web page.
    """
    if html_string.has_attr("about") and html_string["about"].startswith("#mwt"):
        return True
    return False