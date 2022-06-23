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
        return self.value.strip()

    


class Wikilink(Elements):
    def __init__(self, html_string):
        super().__init__("WIKILINK", html_string)
        self.type_mapping = WIKILINK["type"]
        self.disambiguation = False 
        self.redirect = False
        if html_string.has_attr("class"):
            if "new" in html_string["class"]:  # redlink
                self.type.append("2")
            if "mw-disambig" in html_string["class"]:  # disambiguation
                self.disambiguation = True
            if "mw-redirect" in html_string["class"]:  # redirect
                self.redirect = True
        if html_string.has_attr("about"):  # transclusion
            if "mwt" in html_string["about"]:
                self.type.append("3")
        if not any(type in self.type for type in ["2", "3"]):
            self.type.append("1")  # normal link
        
    def get_type(self): ## but i also don't want to rewrite this method for multiple subclasses. What could be a work around? 
        return [WIKILINK["type"][type] for type in self.type]
