import json
import os
import tarfile
from pathlib import Path
from typing import Any, Iterator, List, Optional, Union

from ..parse.article import Article

PathObject = Union[str, Path]


class HTMLDump:
    """
    Class file to create instances of Wikimedia Enterprise HTML Dumps
    """

    def __init__(
        self, filepath: str, encoding: Optional[str] = "utf-8", max_article: int = 100
    ) -> None:
        """
        Contructor for HTMLDump class
        Args:
            encoding (str, optional): encoding of the file. Defaults to "utf-8".
        """
        self.encoding = encoding
        self.file_path = filepath
        self.size = os.path.getsize(self.file_path) / (1024 * 1024 * 1024)
        self.database = str(Path(self.file_path).name).split("-")[0]
        self.max_article = max_article

    def __str__(self) -> str:
        """
        String representation of the HTMLDump class
        """
        return f" HTMLDump (database = {self.database}, size = {self.size} GB, encoding = {self.encoding})"

    def __repr__(self) -> str:
        """
        String representation of the HTMLDump class
        """
        return str(self)

    def __iter__(self):
        """
        Iterator of the Article class
        """
        return self.read_dump_local(
            filepath=self.file_path, max_article=self.max_article
        )

    def read_dump_local(
        self, filepath: str, max_article: int = -1
    ) -> Iterator[List[Any]]:
        """
        Reads a local dump file and returns an iterator of the rows.
        Args:
            filepath (str): path to the dump file
            max_article (int, optional): maximum number of articles to return. Defaults to -1, which means we will iterate over the entire dump file.
        Returns:
            Iterator[List[Any]]: iterator of the rows
        """

        source_path = filepath
        tar_file_ = tarfile.open(source_path, mode="r:gz")
        count = 0
        while True:
            html_fn = tar_file_.next()
            if html_fn != None:
                with tar_file_.extractfile(html_fn) as file_input:
                    for line in file_input:
                        if count == max_article:
                            tar_file_.close()
                            return
                        article = json.loads(line)
                        count += 1
                        yield Article(article)
            else:
                tar_file_.close()
                return
