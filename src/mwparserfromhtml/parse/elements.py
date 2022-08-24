from .utils import check_transclusion, get_tid, map_namespace, title_normalization
from .const import _RE_COMBINE_WHITESPACE
from .utils import (
    check_transclusion,
    get_tid,
    title_normalization,
)


class Element:
    """
    Base class to instantiate a wiki element from the HTML
    """

    def __init__(self, html_string):
        self.name = self.__class__.__name__
        self.html_string = html_string
        self.title = None
        self.plaintext = html_string.get_text()
        self.tid = get_tid(html_string)
        self.transclusion = check_transclusion(html_string)

    def __str__(self):
        return f"{self.name} (VALUE = {self.title} and PROPS =  {self.__dict__})"


class Wikilink(Element):
    """
    Instantiates a Wikilink object from HTML string. The Wikilink object contains the following attributes:
    - disambiguation: boolean, True if if the wikilink leads to a disambiguation page
    - redirect: boolean, True if the wikilink is a redirect
    - redlink: boolean, True if the wikilink is a redlink
    - interwiki: boolean, True if the wikilink is an interwiki link
    """

    def __init__(self, html_string, namespace="en"):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
            language: the language of article content, required for determining the namespace of the wikilink.
        """
        super().__init__(html_string)
        self.title = html_string["title"] if html_string.has_attr("title") else ""
        self.link = html_string["href"] if html_string.has_attr("href") else ""
        self.namespace_id = map_namespace(self.link, namespace)
        self.disambiguation = False
        self.redirect = False
        self.redlink = False
        self.interwiki = False

        if html_string.has_attr("class"):
            if "new" in html_string["class"]:  # redlink
                self.redlink = True
            if "mw-disambig" in html_string["class"]:  # disambiguation
                self.disambiguation = True
            if "mw-redirect" in html_string["class"]:  # redirect
                self.redirect = True
            if "extiw" in html_string["class"]:
                self.interwiki = True


class ExternalLink(Element):
    """
    Instantiates an ExternalLink object from HTML string. The ExternalLink object contains the following attributes:
    - autolinked: boolean, True if the external link is not a numbered or a named link
    - numbered: boolean, True if the external link is a numbered link
    - named: boolean, True if the external link is a named link
    """

    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__(html_string)
        self.title = html_string["title"] if html_string.has_attr("title") else ""
        self.link = html_string["href"] if html_string.has_attr("href") else ""
        self.autolinked = False
        self.numbered = False
        self.named = False
        if "text" in html_string["class"]:
            self.named = True
        elif "autonumber" in html_string["class"]:
            self.numbered = True
        else:
            self.autolinked = True


class Category(Element):
    """
    Instantiates a Category object from an HTML string or a BeautifulSoup Tag object.
    The Category object contains the following attributes:
    - title: the title of the Category normalized from the link
    """

    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__(html_string)
        self.title = title_normalization(html_string["href"])
        self.link = html_string["href"] if html_string.has_attr("href") else ""


class Template(Element):
    """
    Instantiates a Template object from HTML string. Template objects contain the following attribute:
    - title: the title of the template
    - link: the link to the template
    """

    def __init__(self, html_string, data_dictionary):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
            data_dictionary: a dictionary containing the HTML attributes of the template
        """
        super().__init__(html_string)
        self.title = data_dictionary["wt"]
        self.link = data_dictionary["href"]


class Reference(Element):
    """
    Instantiates a References object from HTML string. The References object contains the following attributes:
    """

    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object. Reference objects include the following attribute:
            - ref_id: the id of the reference, that can be used to connect it with the place of reference
        """
        super().__init__(html_string)
        self.plaintext = _RE_COMBINE_WHITESPACE.sub(" ", html_string.get_text())
        self.ref_id = html_string["id"]


class Media(Element):
    """
    Instantiates a Media object from HTML string. The Media object contains the following attributes:
    - title: the title of the media
    - link: the link to the media
    """

    def __init__(self, html_string, media_type=0, caption=None):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
            media_type: if the value is one, it represents an image object. Otherwise, it can be audio or video.
        """
        super().__init__(html_string)
        self.title = html_string["resource"].split(":")[-1]
        self.extension = self.title.split(".")[-1]
        self.caption = caption
        if media_type == 1:
            self.alt_text = html_string["alt"] if html_string.has_attr("alt") else ""
            self.link = html_string["src"]

        else:
            sources_tag = html_string.find_all("source")
            self.link = [tag["src"] for tag in sources_tag]
