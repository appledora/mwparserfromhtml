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
        #strip everything before the first ":" as a naive way to strip namespace information i.e: "Category" in this case
        return link.split(":", 1)[1].replace("_", " ")
    except Exception as e:
        return link 
