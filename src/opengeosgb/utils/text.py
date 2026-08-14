from bs4 import BeautifulSoup
from html import unescape


def remove_html_and_unescape(text: str) -> str:
    """
    Remove conteúdo HTML escapado e tags.

    Args:
        text (str): conteúdo em html

    Returns:
        str: texto decodificado em sem html
    """
    return BeautifulSoup(unescape(text), 'html.parser').get_text()
