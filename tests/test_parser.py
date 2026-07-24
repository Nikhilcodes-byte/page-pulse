from utils.parser import analyze_page


def test_example_com():
    result = analyze_page("https://example.com")

    assert result["status"] == 200
    assert result["h1_count"] == 1
    assert result["word_count"] > 0


def test_python_org():
    result = analyze_page("https://www.python.org")

    assert result["status"] == 200
    assert result["h1_count"] > 0
    assert result["word_count"] > 100


def test_non_html_page():
    result = analyze_page("https://www.python.org/static/img/python-logo.png")

    assert result["status"] == 200
    assert result["title"] == "Not an HTML page"
    assert result["word_count"] == 0