from .utils import check_transclusion, get_tid, title_normalization


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

    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__(html_string)
        self.title = html_string["title"] if html_string.has_attr("title") else ""
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


class Template(Element):
    """
    Instantiates a Template object from HTML string. The Template object contains the following attributes:
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
