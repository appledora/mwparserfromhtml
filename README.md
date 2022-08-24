# mwparserfromhtml

`mwparserfromhtml` is a Python library for parsing and mining metadata from the Enterprise HTML Dumps that has been recently made available by the [Wikimedia Enterprise](https://enterprise.wikimedia.com/). The 6 most updated Enterprise HTML dumps can be accessed from [*this location*](https://dumps.wikimedia.org/other/enterprise_html/runs/). The aim of this library is to provide an interface to work with these HTML dumps and extract the most relevant features from an article.

Besides using the HTML dumps, users can also use the [Wikipedia API](https://en.wikipedia.org/api/rest_v1/#/Page%20content/get_page_html__title_) to obtain the HTML of a particular article from their title and parse the HTML string with this library.

## Motivation
When rendering contents, MediaWiki converts wikitext to HTML, allowing for the expansion of macros to include more material. The HTML version of a Wikipedia page generally has more information than the original source wikitext. So, it's reasonable that anyone who wants to analyze Wikipedia's content as it appears to its readers would prefer to work with HTML rather than wikitext. Traditionally, only the wikitext version has been available in the [XML-dumps](https://dumps.wikimedia.org/backup-index.html). Now, with the introduction of the Enterprise HTML dumps in 2021, anyone can now easily access and use HTML dumps (and they should). 

However, parsing HTML to extract the necessary information is not a simple process. An inconspicuous user may know how to work with HTMLs but they might not be used to the specific format of the dump files. Also the wikitext translated to HTMLs by the MediaWiki API have many different edge-cases and requires heavy investigation of the documentation to get a grasp of the structure. Identifying the features from this HTML is no trivial task! Because of all these hassles, it is likely that individuals would continue working with wikitext as there are already excellent ready-to-use parsers for it (such as [mwparserfromhell](https://github.com/earwig/mwparserfromhell)). 
Therefore, we wanted to write a Python library that can efficiently parse the HTML-code of an article from the Wikimedia Enterprise dumps to extract relevant elements such as text, links, templates, etc. This will hopefully lower the technical barriers to work with the HTML-dumps and empower researchers and others to take advantage of this beneficial resource. 

## Features
* Iterate over large tarballs of HTML dumps without extracting them to memory (memory efficient, but not subscriptable unless converted to a list)
* Extract major article metadata like Category, Templates, Wikilinks, External Links, Media, References etc. with their respective type and status information
* Easily extract the content of an article from the HTML dump and customizing the level of detail
* Generate summary statistics for the articles in the dump


## Installation

You can install ``mwparserfromhtml`` with ``pip``:

```bash
   $ pip install mwparserfromhtml
```

## Basic Usage 

* Import the dump module from the library and load the dump:

```python
    from mwparserfromhtml import HTMLDump
    html_file_path = "TARGZ_FILE_PATH"
    html_dump = HTMLDump(html_file_path, max_article=150)
```

* Iterate over the articles in the dump:

```python
    for article in html_dump:
        print(article.title)
```

* Extract the plain text of an article from the dump, i.e. remove anything that is not text (e.g. a link is replaced by its [anchor text](Anchor_text)):

```python
    for article in html_dump:
        print(article.get_plaintext( skip_categories=False, skip_transclusion=False, skip_headers=False))
```

* Extract Templates, Categories, Wikilinks, External Links, Media, References etc. from the dump:

```python
    for article in html_dump:
        print(article.get_templates())
        print(article.get_categories())
        print(article.get_wikilinks())
        print(article.get_external_links())
        print(article.get_media(skip_images=True, skip_video=False, skip_audio=False))
        print(article.get_references())
```

* Parse HTML string of a Wikipedia article (in a file `FILE.html`) and extract features (such as templates) 
```python
    from mwparserfromhtml import Article
    html_string = "".join(open("FILE.html", "r").readlines())
    article = Article(html_string)
    print(article.get_templates())
```

<!-- * Generate summary statistics of the dump:

```python
    from mwparserfromhtml import HTMLDump
    html_file_path = "TARGZ_FILE_PATH"
    html_dump = HTMLDump(html_file_path, max_article=150)
    html_dump.generate_summary_stats()
``` -->
## Project Information 
- [Licensing](https://gitlab.wikimedia.org/repos/research/html-dumps/-/blob/main/LICENSE)
- [Repository](https://gitlab.wikimedia.org/repos/research/html-dumps)
- [Issue Tracker](https://gitlab.wikimedia.org/repos/research/html-dumps/-/issues)
<!-- - Documentation 
- Contribution Guidelines -->
 
## Acknowledgements

This project was started as part of an [Outreachy](https://www.outreachy.org/) internship from May--August 2022. This project has benefited greatly from the work of Earwig ([mwparserfromhell](https://github.com/earwig/mwparserfromhell)) and Slavina Stefanova ([mwsql](https://github.com/mediawiki-utilities/python-mwsql)). 
