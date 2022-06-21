import re
from typing import List, Any

import bs4
from bs4 import Comment  # for parsing the HTML

# regex for checking if a string is a valid URL
regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def is_comment(element):
    return isinstance(element, Comment)


def to_printable(
        datatype: Any = None, attr: str = None, printtype: str = None
) -> List[Any]:
    """
    Custom print method that handles printing different datatypes and converts them to a list

    Args:
        datatype (Any): datatype to be printed
        attr (str, optional): attribute of the datatype to be printed. Defaults to None.
        printtype (str, optional): type of print. Defaults to None.
    """

    if isinstance(datatype, list):
        printable = []
        if printtype == "gettext":
            printable = [l.get_text() for l in datatype]
        elif attr != None:
            printable = [l[attr] for l in datatype]
        else:
            printable = [l for l in datatype]
        return printable


def custom_string_filter(
        pollute: str, target: bs4.element.ResultSet, mode: bool, attr: str = None
) -> List[str]:
    """
    custom string filter method that filters an input list of strings and returns a list of strings that either has the target string or not

    Args:
        pollute : the string to be filtered
        target : the list of strings to be filtered
        mode : True if we want to filter the target list of strings that has the pollute string, False if we want to filter the target list of strings that does not have the pollute string
        attr : the attribute of the target list of strings to be filtered
    """
    itemlist = []
    if mode == False:
        if attr != None:
            for item in target:
                if pollute not in str(item[attr]):
                    itemlist.append(item)
        else:
            for item in target:
                if pollute not in str(item):
                    itemlist.append(item)

    else:
        if attr != None:
            for item in target:
                if pollute in str(item[attr]):
                    itemlist.append(item)
        else:
            for item in target:
                if pollute in str(item):
                    itemlist.append(item)
    return itemlist


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


def tag_visible(element):
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    if re.match(r"\[\d+\]", str(element)):
        return False
    return True


def flatten_list(A):
    rt = []
    for i in A:
        if isinstance(i, list):
            rt.extend(flatten_list(i))
        else:
            if i.strip() != "":
                rt.append(i)
    return rt


def link_to_text(links: List[str], formatting_directives: dict) -> str:
    remove = formatting_directives["remove"]
    target = formatting_directives["replace_target"]
    value = formatting_directives["replace_value"]
    formatted_links = []
    for l in links:
        try:
            l = l.strip(remove)
        except:
            pass
        try:
            l = l.replace(target, value)
        except:
            pass
        if l.strip() == None:
            continue
        formatted_links.append(l)
    return formatted_links


htmlCodes = [
    ["&", "&amp;"],
    ["<", "&lt;"],
    [">", "&gt;"],
    ['"', "&quot;"],
]
htmlCodesReversed = htmlCodes[:]
htmlCodesReversed.reverse()


def htmlDecode(s, codes=htmlCodesReversed):
    """Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>. It is the inverse of htmlEncode()."""
    for code in codes:
        s = s.replace(code[1], code[0])
    return s


def process_headers(header_list: List[str]) -> List[str]:
    """
    Processes the headers of the HTML file and returns a list of headers
    """
    return [h.text for h in header_list]
