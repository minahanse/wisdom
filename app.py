#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from time import sleep
from typing import Any, Tuple

import requests

URL = "http://api.forismatic.com/api/1.0/"


def get_data() -> Tuple[Any, Any]:
    response = requests.post(
        URL, data={"method": "getQuote", "format": "json", "lang": "en"}
    )

    if response.status_code == 200:
        data = response.json()
        return data.get("quoteText"), data.get("quoteAuthor")

    print(f"Failed to get data from API, error: {response.status_code}")
    return None, None


def main():
    number_of_quotes = int(os.getenv("QUOTES", 1))
    quote, author = get_data()

    # Limit maximum to 5 to prevent API overload.
    if number_of_quotes > 5:
        number_of_quotes = 5

    for _ in range(number_of_quotes):
        quote, author = get_data()

        if quote and author:
            if number_of_quotes > 1:
                sleep(1)
            print(f"\n{quote} - {author}\n")


if __name__ == "__main__":
    main()
