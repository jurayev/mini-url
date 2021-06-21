import requests
import re

from fastapi import status


def is_valid_url(url: str) -> str:
    """
    Validates url for correctness using regex
    """
    if not url:
        return False

    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)')
    p = re.compile(regex)
    return True if re.search(p, url) else False


def validate_url(url: str) -> None:
    """
    Validates url
    1. Validates for url correctness and misspelling
    2. Validates if website exists
    :raises ValueError if validation is failed



    """
    if not is_valid_url(url):
        raise ValueError(f"Validation Error. Provided url '{url}' is not valid.")
    try:
        response = requests.get(url)
    except Exception as e:
        raise ValueError(f"Validation Error. '{url}' website doesn't exists.")
    else:
        if response.status_code is not status.HTTP_200_OK:
            raise ValueError(f"Validation Error. '{url}' website doesn't exists.")
