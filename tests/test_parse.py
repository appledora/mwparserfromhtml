from context import Article, example_html_one, example_html_two

def test_get_headings_one():
    article = Article(example_html_one)
    expected_headers = []
    assert article.get_headers() == expected_headers

def test_get_headings_two():
    article = Article(example_html_two)
    expected_headers = ['Life', 'References']
    assert article.get_headers() == expected_headers

def test_get_sections_one():
    article = Article(example_html_one)
    expected_sections = []
    assert article.get_sections() == expected_sections