import re
import sys
from typing import List

from bs4 import BeautifulSoup

from .utils import is_comment
from .const import WIKILINK
from .elements import Wikilink
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
        extract the comments from a BeautifulSoup object or Parsed Html
        Returns:
            List[str]: list of comments
        """
        return self.parsed_html.find_all(text=is_comment)

    def get_headers(self) -> List[str]:
        """
        extract the headers from a BeautifulSoup object or Parsed Html
        Returns:
            List[str]: list of headers
        """
        return [h.text for h in self.parsed_html.find_all(re.compile("^h[1-6]$"))]

    def get_sections(self) -> List[str]:
        """
        extract the article sections from a BeautifulSoup object or Parsed Html
        Returns:
            List[str]: list of section names
        """
        return [l.get_text() for l in self.parsed_html.find_all("section")]

    def get_wikilinks(self, soup) -> List[Wikilink]:
        """
        extract wikilinks from a BeautifulSoup object or Parsed Html
        Returns:
            List[str]: list of wikilinks
        """
    
        wikilinks = self.parsed_html.find_all(WIKILINK["tag"], attrs=WIKILINK["attribute"])
        return [Wikilink(w) for w in wikilinks]           

