import re
import sys
from typing import List
from bs4 import BeautifulSoup

from .utils import is_comment
from .elements import Wikilink, ExternalLink, Category
class Article:
    """
    Class file to create instance of a Wikipedia article from the dump
    """

    def __init__(
            self,
            html: str
    ) -> None:
        """
        Constructor for Article class
        """
        self.raw_html = html
        self.parsed_html = BeautifulSoup(html, "html.parser")
        self.title = self.parsed_html.title.text
        self.address = self.parsed_html.find("link", {"rel":"dc:isVersionOf"})["href"]
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
        return [l.get_text() for l in self.parsed_html.find_all("section")]

    def get_wikilinks(self) -> List[Wikilink]:
        """
        extract wikilinks from a BeautifulSoup object.
        Returns:
            List[Wikilink]: list of wikilinks
        """
        tag = "a"
        wikilinks = self.parsed_html.find_all(tag, attrs= {"rel": re.compile("mw:WikiLink")})
        return [Wikilink(w) for w in wikilinks]         


    def get_categories(self) -> List[Category]:
        """
        extract categories from a BeautifulSoup object.
        Returns:
            List[Category]: list of categories
        """
        tag = "link"
        categories = self.parsed_html.find_all(tag, attrs= {"rel": "mw:PageProp/Category"})
        return [Category(c) for c in categories]


    def get_externallinks(self) -> List[ExternalLink] :
        """
        extract external links from a BeautifulSoup object.
        Returns:
            List[ExternalLink]: list of external links
        """
        tag = "a"
        externallinks = self.parsed_html.find_all(tag, attrs= {"rel": re.compile("mw:ExtLink")})
        return [ExternalLink(e) for e in externallinks]           
