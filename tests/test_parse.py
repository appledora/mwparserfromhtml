from context import Article, example_html_one, example_html_two


def test_get_headings_one():
    article = Article(example_html_one)
    expected_headers = []
    assert article.get_headers() == expected_headers


def test_get_headings_two():
    article = Article(example_html_two)
    expected_headers = ["Life", "References"]
    assert article.get_headers() == expected_headers


def test_get_sections_one():
    article = Article(example_html_one)
    number_of_expected_sections = 1
    assert len(article.get_sections()) == number_of_expected_sections


def test_get_sections_two():
    article = Article(example_html_two)
    number_of_expected_sections = 3
    assert len(article.get_sections()) == number_of_expected_sections


def test_get_comments_one():
    article = Article(example_html_one)
    number_of_expected_headers = 0
    assert len(article.get_comments()) == number_of_expected_headers


def test_get_comments_two():
    article = Article(example_html_two)
    number_of_expected_comments = 0
    assert len(article.get_comments()) == number_of_expected_comments


def test_get_wikilinks_one():
    article = Article(example_html_one)
    test_wlink_objs = article.get_wikilinks()
    number_of_expected_wikilinks = 6
    number_of_redirects = 0
    number_of_redlinks = 0
    number_of_disambiguations = 0
    number_of_interwikilinks = 0
    number_of_transclusions = 0
    number_of_namespaces = {0: 5, 12: 1}
    test_redlink = 0
    test_disambiguation = 0
    test_redirect = 0
    test_transclusion = 0
    test_interwiki = 0
    test_namespace = {}
    for item in test_wlink_objs:
        test_namespace[item.namespace_id] = test_namespace.get(item.namespace_id, 0) + 1
        if item.redlink:
            test_redlink += 1
        if item.redirect:
            test_redirect += 1
        if item.disambiguation:
            test_disambiguation += 1
        if item.interwiki:
            test_interwiki += 1
        if item.transclusion:
            test_transclusion += 1
    assert len(test_wlink_objs) == number_of_expected_wikilinks
    assert test_redlink == number_of_redlinks
    assert test_redirect == number_of_redirects
    assert test_disambiguation == number_of_disambiguations
    assert test_interwiki == number_of_interwikilinks
    assert test_transclusion == number_of_transclusions
    assert test_namespace == number_of_namespaces


def test_get_wikilinks_two():
    article = Article(example_html_two)
    test_wlink_objs = article.get_wikilinks()
    number_of_expected_wikilinks = 31
    number_of_redirects = 6
    number_of_redlinks = 2
    number_of_disambiguations = 1
    number_of_interwikilinks = 1
    number_of_transclusions = 1
    number_of_namespaces = {0: 31}
    test_redlink = 0
    test_disambiguation = 0
    test_redirect = 0
    test_transclusion = 0
    test_interwiki = 0
    test_namespace = {}
    for item in test_wlink_objs:
        test_namespace[item.namespace_id] = test_namespace.get(item.namespace_id, 0) + 1
        if item.redlink:
            test_redlink += 1
        if item.redirect:
            test_redirect += 1
        if item.disambiguation:
            test_disambiguation += 1
        if item.interwiki:
            test_interwiki += 1
        if item.transclusion:
            test_transclusion += 1
    assert len(test_wlink_objs) == number_of_expected_wikilinks
    assert test_redlink == number_of_redlinks
    assert test_redirect == number_of_redirects
    assert test_disambiguation == number_of_disambiguations
    assert test_interwiki == number_of_interwikilinks
    assert test_transclusion == number_of_transclusions
    assert test_namespace == number_of_namespaces


def test_get_externallinks_one():
    article = Article(example_html_one)
    test_exlinks_objs = article.get_externallinks()
    number_of_expected_externallinks = 1
    number_of_autolink = 0
    number_of_numbered = 0
    number_of_named = 1
    number_of_transclusion = 0
    test_autolink = 0
    test_named = 0
    test_numbered = 0
    test_transclusion = 0

    for item in test_exlinks_objs:
        if item.autolinked:
            test_autolink += 1
        if item.named:
            test_named += 1
        if item.numbered:
            test_numbered += 1
        if item.transclusion:
            test_transclusion += 1

    assert len(test_exlinks_objs) == number_of_expected_externallinks
    assert test_autolink == number_of_autolink
    assert test_named == number_of_named
    assert test_numbered == number_of_numbered
    assert test_transclusion == number_of_transclusion


def test_get_externallinks_two():
    article = Article(example_html_two)
    test_exlinks_objs = article.get_externallinks()
    number_of_expected_externallinks = 1
    number_of_autolink = 0
    number_of_numbered = 0
    number_of_named = 1
    number_of_transclusion = 0
    test_autolink = 0
    test_named = 0
    test_numbered = 0
    test_transclusion = 0

    for item in test_exlinks_objs:
        if item.autolinked:
            test_autolink += 1
        if item.named:
            test_named += 1
        if item.numbered:
            test_numbered += 1
        if item.transclusion:
            test_transclusion += 1

    assert len(test_exlinks_objs) == number_of_expected_externallinks
    assert test_autolink == number_of_autolink
    assert test_named == number_of_named
    assert test_numbered == number_of_numbered
    assert test_transclusion == number_of_transclusion


def test_get_categories_one():
    article = Article(example_html_one)
    test_categories_objs = article.get_categories()
    number_of_expected_categories = 5
    number_of_transclusion = 3
    test_transclusions = 0
    for item in test_categories_objs:
        if item.transclusion:
            test_transclusions += 1
    assert len(test_categories_objs) == number_of_expected_categories
    assert test_transclusions == number_of_transclusion


def test_get_categories_two():
    article = Article(example_html_two)
    test_categories_objs = article.get_categories()
    number_of_expected_categories = 11
    number_of_transclusion = 5
    test_transclusions = 0
    for item in test_categories_objs:
        if item.transclusion:
            test_transclusions += 1
    assert len(test_categories_objs) == number_of_expected_categories
    assert test_transclusions == number_of_transclusion


def test_get_templates_one():
    article = Article(example_html_one)
    test_templates_objs = article.get_templates()
    number_of_expected_templates = 1
    assert len(test_templates_objs) == number_of_expected_templates


def test_get_templates_two():
    article = Article(example_html_two)
    test_templates_objs = article.get_templates()
    number_of_expected_templates = 6
    assert len(test_templates_objs) == number_of_expected_templates


def test_get_references_one():
    article = Article(example_html_one)
    number_of_expected_references = 0
    assert len(article.get_references()) == number_of_expected_references


def test_get_references_two():
    article = Article(example_html_two)
    number_of_expected_references = 1
    assert len(article.get_references()) == number_of_expected_references


def test_get_media_one():
    article = Article(example_html_one)
    number_of_expected_media = 1
    assert len(article.get_media()) == number_of_expected_media


def test_get_media_two():
    article = Article(example_html_two)
    number_of_expected_media = 1
    assert len(article.get_media()) == number_of_expected_media
