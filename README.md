# mwparserwithlove

`mwparserwithlove` is a Python library for parsing and mining metadata from the Enterprise HTML Dumps that has been recently made available by the [Wikimedia Enterprise](https://enterprise.wikimedia.com/). The 6 most updated Enterprise HTML dumps can be accessed from [*this location*](https://dumps.wikimedia.org/other/enterprise_html/runs/). The aim of this library is to provide an interface to work with these html dumps and extract the most relevant features from an article.

Besides using the HTML dumps, users can also use the [Wikipedia API](https://en.wikipedia.org/api/rest_v1/#/Page%20content/get_page_html__title_) to obtain the HTML of a particular article from their title and parse the HTML string with this library.

## Motivation
When rendering contents, MediaWiki converts wikitext to HTML, allowing for the expansion of macros to include more material. The HTML version of a Wikipedia page generally has more information than the original source wikitext . So, it's reasonable that academics who want to look at Wikipedia through the eyes of its users would prefer to work with HTML rather than wikitext. The introduction of the Enterprise HTML dumps somewhat mitigates the drawbacks of utilising wikitext for corpus development and other research. Researchers can now use HTML dumps (and they should). 

However, parsing HTML to extract the necessary information is not a simple process. An inconspicuous user may know how to work with HTMLs but they might not be used to the specific format of the dump files. Also the wikitext translated to HTMLs by the MediaWiki API have many different edge-cases and requires heavy investigation of the documentation to get a grasp of the structure. Identifying the features from this HTML is no trivial task! Because of all these hassles, it is likely that individuals would continue working with wikitext as there are already ready-to-use parsers for it and consequently face the misrepresentation of information. This is why we provide an accessible HTML parser to decrease the technological barrier, so that more users may utilise this resource. 

## Features
* Iterate over large tarballs of HTML dumps without extracting them to memory (memory efficient, but not subscriptable unless converted to a list)
* Extract major article metadata like Category, Templates, Wikilinks, External Links, Media, References etc. with their respective type and status information
* Smoothly extract the content of an article from the HTML dump and customizing the level of detail
* Generate Summary Statistics for the articles in the dump


## Installation

You can install ``mwparserwithlove`` with ``pip``:

```bash
   $ pip install mwparserwithlove
```

## Basic Usage 

* Import the dump module from the library and load the dump:

```python
    from mwparserwithlove import dump
    html_file_path = "TARGZ_FILE_PATH"
    html_dump = mwp.dump.HTMLDump(html_file_path, max_article=150)
```

* Iterate over the articles in the dump:

```python
    for article in html_dump:
        print(article.title)
```

* Extract the content of an article from the dump:

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

* Parse HTML string to extract metadata 
```python
    from mwparserwithlove import parse
    html_string = "".join(open("FILE.html", "r").readlines())
    article = parse.Article(html_string)
    print(article.get_templates())
```

* Generate Summary Statistics of the dump:

```python
    from mwparserwithlove import dump
    html_file_path = "TARGZ_FILE_PATH"
    html_dump = mwp.dump.HTMLDump(html_file_path, max_article=150)
    html_dump.generate_summary_stats()
```
## Project Information 

## Acknowledgements