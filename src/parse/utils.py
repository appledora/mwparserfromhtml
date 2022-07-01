import re

from bs4 import Comment  # for parsing the HTML

# regex for checking if a string is a valid URL
regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

htmlCodes = [
    ["&", "&amp;"],
    ["<", "&lt;"],
    [">", "&gt;"],
    ['"', "&quot;"],
]
## actually can't remember why I did this - but it seems to work
htmlCodesReversed = htmlCodes[:]
htmlCodesReversed.reverse()

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




def htmlDecode(s, codes=htmlCodesReversed):
    """Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>. It is the inverse of htmlEncode()."""
    for code in codes:
        s = s.replace(code[1], code[0])
    return s



def title_normalization(link):
    try:
        link = link.split(":", 1)[1]
    except Exception as e:
        return link.strip().replace("_", " ")
    return link.strip().replace("_", " ")
