from .const import WIKILINK


class Elements:
    def __init__(self, name, html_string):
        self.name = name
        self.value = html_string.get_text()
        self.type = []
        self.type_mapping = None ## I don't want make this a part of the class instance
    def __str__(self):
        return f"{self.name} (value = {self.value} and types =  {self.type})"

    def get_value(self):
        return self.value

    def normalize_link(self, link):
        return link.strip().replace("_", " ")


class Wikilink(Elements):
    def __init__(self, html_string):
        super().__init__("WIKILINK", html_string)
        self.type_mapping = WIKILINK["type"]
        if html_string.has_attr("class"):
            if "new" in html_string["class"]:  # redlink
                self.type.append("2")
            if "mw-disambig" in html_string["class"]:  # disambiguation
                self.type.append("5")
            if "mw-redirect" in html_string["class"]:  # redirect
                self.type.append("6")
        if html_string.has_attr("about"):  # transclusion
            if "mwt" in html_string["about"]:
                self.type.append("3")
        if not any(item in self.type for item in ["2", "5", "3"]):
            self.type.append("1")  # normal link
        
    def get_type(self): ## but i also don't want to rewrite this method for multiple subclasses. What could be a work around? 
        return [WIKILINK["type"][item] for item in self.type]
