from .utils import title_normalization
class Element:
    def __init__(self, html_string):
        self.name = self.__class__.__name__
        self.title = html_string["title"]
        self.text = html_string.get_text() #plain text value of the element (if any)
    def __str__(self):
        return f"{self.name} (VALUE = {self.title} and PROPS =  {self.__dict__})"
    
class Wikilink(Element):
    """
    Instantiates a Wikilink object from HTML string. The Wikilink object contains the following attributes:
    - disambiguation: boolean, True if if the wikilink leads to a disambiguation page
    - redirect: boolean, True if the wikilink is a redirect
    - redlink: boolean, True if the wikilink is a redlink
    - transclusion: boolean, True if the wikilink was transcluded onto the page
    - interwiki: boolean, True if the wikilink is an interwiki link
    """
    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__( html_string)
        self.disambiguation = False 
        self.redirect = False
        self.redlink = False
        self.transclusion = False
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
        if html_string.has_attr("about"):  # transclusion
            if html_string["about"].startswith("#mwt"):
                self.transclusion = True

        

class ExternalLink(Element) :
    """
    Instantiates an ExternalLink object from HTML string. The ExternalLink object contains the following attributes:
    - autolinked: boolean, True if the external link is not a numbered or a named link
    - numbered: boolean, True if the external link is a numbered link
    - named: boolean, True if the external link is a named link
    - transclusion: boolean, True if the wikilink was transcluded onto the page
    """
    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__(html_string)
        self.autolinked = False
        self.numbered = False
        self.named = False
        self.transclusion = False

        if html_string.has_attr("about"):  # transclusion
            if html_string["about"].startswith("#mwt"):
                self.transclusion = True
        if "text" in html_string["class"]:
            self.named = True
        elif "autonumber" in html_string["class"]:
            self.numbered = True
        else: 
            self.autolinked = True
class Category(Element):
    """
    Instantiates an Category object from an HTML string or a BeautifulSoup Tag object. The Category object contains the following attributes:
    - title: the title of the Category normalized from the link
    - transclusion: True if the category is a transclusion
    """
    def __init__(self,html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__(html_string)
        self.title = title_normalization( html_string["href"])
        self.transclusion = False

        #since transclusion is present in different elements, may be this should be a base property? 
        if html_string.has_attr("about") and html_string["about"].startswith("#mwt"):
            self.transclusion = True

