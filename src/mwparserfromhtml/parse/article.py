import ast
import json
import re
import sys
from bs4 import BeautifulSoup
from typing import List

from .elements import ExternalLink, Media, Reference, Template, Wikilink, Category
from .utils import get_metadata, is_comment, map_namespace, nested_value_extract, dfs


class Article:
    """
    Class file to create instance of a Wikipedia article from the dump
    """

    def __init__(self, body: json) -> None:
        """
        Constructor for Article class
        """
        self.raw_html = body["article_body"]["html"]
        self.wikitext = body["article_body"]["wikitext"]
        self.parsed_html = BeautifulSoup(self.raw_html, "html.parser")
        self.title = self.parsed_html.title.text
        self.address = self.parsed_html.find("link", {"rel": "dc:isVersionOf"})["href"]
        self.size = sys.getsizeof(self.raw_html)
        self.language = self.parsed_html.find(
            "meta", {"http-equiv": "content-language"}
        )["content"]
        self.page_namespace_id = self.parsed_html.find(
            "meta", {"property": "mw:pageNamespace"}
        )["content"]
        self.wiki_db = self.parsed_html.find("base")["href"].split(".")[0].strip("//")
        self.metadata = get_metadata(body)

    def __str__(self):
        """
        String representation of the Article class
        """
        return f"Article (title = {self.title}, HTML size = {self.size}, additional dump metadata = {self.metadata})"

    def __repr__(self):
        return str(self)

    def get_html(self) -> str:
        """
        extracts the raw html code of the article
        Returns:
            str: raw html code of the article
        """
        return self.raw_html

    def get_wikitext(self) -> str:
        """
        Returns:
            str: wikitext code of the article
        """
        return self.wikitext

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
            tag,
            attrs={
                "rel": re.compile("mw:WikiLink")
            },  # using re.compile here because we also want to capture mw:WikiLink/interwiki
        )
        return [Wikilink(w, self.wiki_db) for w in wikilinks]

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
            return tag.has_attr("data-mw") and "parts" in ast.literal_eval(
                tag["data-mw"]
            )

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
                            (temp, item["target"])
                        )  # storing both the html string and the template values
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
        references = self.parsed_html.find_all(
            tag, attrs={"class": "mw-reference-text"}
        )
        return [Reference(r) for r in references]

    def get_media(
        self, skip_images=False, skip_audio=False, skip_video=False
    ) -> List[Media]:

        """
        extract image, video and audio information from a Beautifulsoup object.
        Media not appearing inside `img`, `video` or `audio` html  tag won't be
        captured by this method.
        Args:
            skip_images: boolean. If true doesn't include Image data.
            skip_audio: boolean. If true, doesn't include audio data.
            skip_video: boolean. If true, doesn't include video data.

        Returns:
            List[Media]: a list of media objects.
        """
        media_objects = []
        # captions are not consistent for media files, that's why we can
        # only extract them if they exist in parent tags
        if not skip_images:
            images = self.parsed_html.find_all("img")
            image_captions = []
            for im in images:
                image_captions.append(
                    im.parent.parent.find("figcaption").text
                    if im.parent.parent.find("figcaption")
                    else ""
                )
            media_objects.extend(
                [
                    Media(html_string=m[0], media_type=1, caption=m[1])
                    for m in zip(images, image_captions)
                ]
            )

        if not skip_audio:
            audio = self.parsed_html.find_all("audio")
            audio_captions = []

            for im in audio:
                audio_captions.append(
                    im.parent.parent.find("figcaption").text
                    if im.parent.parent.find("figcaption")
                    else ""
                )
            media_objects.extend(
                [
                    Media(html_string=m[0], caption=m[1])
                    for m in zip(audio, audio_captions)
                ]
            )
        if not skip_video:
            video = self.parsed_html.find_all("video")
            video_captions = []
            for im in video:
                video_captions.append(
                    im.parent.parent.find("figcaption").get_text()
                    if im.parent.parent.find("figcaption")
                    else ""
                )
            media_objects.extend(
                [
                    Media(html_string=m[0], caption=m[1])
                    for m in zip(video, video_captions)
                ]
            )

        return media_objects

    def get_plaintext(
        self, skip_categories=False, skip_transclusion=False, skip_headers=False
    ) -> str:
        """
        extract plaintext from the HTML object in a depth-first manner.
        Args:
            skip_categories : boolean. If true, the generated plaintext won't include Category titles.
            skip_transclusions : boolean. If true, the generated plaintext won't include transcluded elements.
            skip_headers : boolean. If true, the generated plaintext won't include section headers.

        Returns:
            str: the visible plaintext of an article.
        """
        return "".join(
            dfs(
                self.parsed_html.body,
                skip_categories=skip_categories,
                skip_transclusion=skip_transclusion,
                skip_headers=skip_headers,
            )
        )
