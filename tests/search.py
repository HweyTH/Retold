"""
Retold

Functions for searching MangaDex's API.
"""


import requests


URL = "https://api.mangadex.org"


def search_title(title: str, limit: int, page: int) -> list[dict]:
    """
    Search for manga.
    :param title: The title of the manga to be searched for.
    :param limit: The maximum number of results that are returned per page.
        limit >= 1
    :param page: The page of results from
        [(page - 1) * limit] to [page * limit]. page >= 1
    :return: The data from the json-encoded content of the response. MangaDex
        represents this data as a list of dictionary objects.
    """
    if title == "":
        raise Exception("Invalid title.")
    if limit < 1:
        raise Exception("Invalid limit.")
    if page < 1:
        raise Exception("Invalid page.")

    params = {"title": title, "limit": limit, "offset": limit * (page - 1)}
    request = requests.get(f"{URL}/manga", params=params)
    result = request.json()["data"]

    return result
