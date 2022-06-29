class Element:
    """
    Base class to instantiate an wiki element from the HTML
    """
    def __init__(self, html_string):
        self.name = self.__class__.__name__
        self.value = html_string.get_text().strip() #plain text value of the element
    def __str__(self):
        return f"{self.name} (VALUE = {self.value} and PROPS =  {self.__dict__})"

    def get_value(self):
        return self.value.strip()

    


class Wikilink(Element):
    """
    Instantiates a Wikilink object from HTML string. The Wikilink object contains the following attributes:
    - value: the value of the wikilink
    - disambiguation: boolean, True if the wikilink is a disambiguation
    - redirect: boolean, True if the wikilink is a redirect
    - redlink: boolean, True if the wikilink is a redlink
    - transclusion: boolean, True if the wikilink is a transclusion
    - interwiki: boolean, True if the wikilink is an interwiki link
    - standard: boolean, True if the wikilink is not a redlink or a disambiguation or a transclusion or an interwiki link
    """
    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__( html_string)
        self.value = html_string["title"]
        self.disambiguation = False 
        self.redirect = False
        self.redlink = False
        self.transclusion = False
        self.standard = False
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
            if "mwt" in html_string["about"]:
                self.transclusion = True
        # we are defining standard links as those, that are not redlinks, disambiguations, interwiki or transclusions
        if not self.redlink and not self.disambiguation and not self.transclusion and not self.interwiki:
            self.standard = True # normal link
        

class ExternalLink(Element) :
    """
    Instantiates an ExternalLink object from HTML string. The ExternalLink object contains the following attributes:
    - value: the value of the external link
    - standard: boolean, True if the external link is not a numbered or named link
    - numbered: boolean, True if the external link is a numbered link
    - named: boolean, True if the external link is a named link
    """
    def __init__(self, html_string):
        """
        Args:
            html_string: an HTML string or a BeautifulSoup Tag object.
        """
        super().__init__(html_string)
        self.standard = False
        self.numbered = False
        self.named = False
        self.transclusion = False

        if html_string.has_attr("about"):  # transclusion
            if "mwt" in html_string["about"]:
                self.transclusion = True
        if "text" in html_string["class"]:
            self.named = True
        elif "autonumber" in html_string["class"]:
            self.numbered = True
        else: 
            self.standard = True
