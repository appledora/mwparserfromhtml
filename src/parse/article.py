import ast
import re
import sys
from bs4 import BeautifulSoup
from typing import List

from .elements import ExternalLink, Media, Reference, Template, Wikilink, Category
from .utils import is_comment, nested_value_extract


class Article:
    """
    Class file to create instance of a Wikipedia article from the dump
    """

    def __init__(self, html: str) -> None:
        """
        Constructor for Article class
        """
        self.raw_html = html
        self.parsed_html = BeautifulSoup(html, "html.parser")
        self.title = self.parsed_html.title.text
        self.address = self.parsed_html.find("link", {"rel": "dc:isVersionOf"})["href"]
        self.size = sys.getsizeof(html)

    def __str__(self):
        """
        String representation of the Article class
        """
        return f"Article (title = {self.title}, size = {self.size})"

    def __repr__(self):
        return str(self)

    def get_html(self) -> str:
        """
        extracts the raw html code of the article
        Returns:
            str: raw html code of the article
        """
        return self.raw_html

    def get_comments(self) -> List[str]:
        """
        extract the comments from a BeautifulSoup object.
        Returns:
            List[str]: list of comments
        """
        return self.parsed_html.find_all(text=is_comment)

    def get_headers(self) -> List[str]:
        """
        extract the headers from a BeautifulSoup object.
        Returns:
            List[str]: list of headers
        """
        return [h.text for h in self.parsed_html.find_all(re.compile("^h[1-6]$"))]

    def get_sections(self) -> List[str]:
        """
        extract the article sections from a BeautifulSoup object.
        Returns:
            List[str]: list of section names
        """
        return [section.get_text() for section in self.parsed_html.find_all("section")]

    def get_wikilinks(self) -> List[Wikilink]:
        """
        extract wikilinks from a BeautifulSoup object.
        Returns:
            List[Wikilink]: list of wikilinks
        """
        tag = "a"
        wikilinks = self.parsed_html.find_all(
            tag, attrs={"rel": re.compile("mw:WikiLink")}
        )
        return [Wikilink(w) for w in wikilinks]

    def get_categories(self) -> List[Category]:
        """
        extract categories from a BeautifulSoup object.
        Returns:
            List[Category]: list of categories
        """
        tag = "link"
        categories = self.parsed_html.find_all(
            tag, attrs={"rel": "mw:PageProp/Category"}
        )
        return [Category(c) for c in categories]

    def get_externallinks(self) -> List[ExternalLink]:
        """
        extract external links from a BeautifulSoup object.
        Returns:
            List[ExternalLink]: list of external links
        """
        tag = "a"
        externallinks = self.parsed_html.find_all(
            tag, attrs={"rel": re.compile("mw:ExtLink")}
        )
        return [ExternalLink(e) for e in externallinks]

    def get_templates(self) -> List[Template]:
        """
        extract templates from a BeautifulSoup object.
        Returns:
            List[Template]: list of templates
        """

        # function to extract template with data-mw attribute that contains dictionary with "parts" key
        def criterion(tag):
            return tag.has_attr("data-mw") and "parts" in ast.literal_eval(tag["data-mw"])

        templates = self.parsed_html.findAll(criterion)
        template_values = []
        # Templates appear inside the "template" key of a nested dictionary, unlike the other elements
        # that can be directly extracted from html attributes. Which is why we have traverse the nested
        # dictionary (may have arbitrary depth) to extract the values of the templates.
        for temp in templates:
            try:
                template_item = list(
                    nested_value_extract("template", ast.literal_eval(temp["data-mw"]))
                )
                if len(template_item) != 0:
                    # we have to use a loop because there may be multiple "template" keys in the nested dictionary
                    for item in template_item:
                        template_values.append(
                            (temp, item["target"]))  # storing both the html string and the template values
            except Exception as e:
                print(e)

        return [Template(t[0], t[1]) for t in template_values]

    def get_references(self) -> List[Reference]:
        """
        extract references from a BeautifulSoup object.
        Returns:
            List[str]: list of references
        """
        tag = "span"
        references = self.parsed_html.find_all(tag, attrs={"class": "mw-reference-text"})
        return [Reference(r) for r in references]


    def get_media(self, skip_images = False, skip_audio = False, skip_video = False) -> List[Media] : 
        media_objects = []
        if not skip_images:
            images = self.parsed_html.find_all("img")
            media_objects.extend([Media(m, 1) for m in images])
            for im in images : 
                print(im.parent)
                print("-"*50)
                print(im.parent.parent)
                print("-"*50)
                print(im.parent.parent.find("figcaption"))
                print("#"*50)

        if not skip_audio:
            audio = self.parsed_html.find_all("audio")
            media_objects.extend([Media(m) for m in audio])
            for im in audio : 
                print(im.parent)
                print("-"*50)
                print(im.parent.parent)
                print("-"*50)
                print(im.parent.find("figcaption"))
                print("#"*50)
        if not skip_video:
            video = self.parsed_html.find_all("video")
            media_objects.extend([Media(m) for m in video])
            for im in video : 
                print(im.parent)
                print("-"*50)
                print(im.parent.parent)
                print("-"*50)
                print(im.parent.find("figcaption"))
                print("#"*50)

        return media_objects
        