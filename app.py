#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
from time import sleep
from typing import Optional

import requests

URL = "http://api.forismatic.com/api/1.0/"


def get_data() -> Optional[dict]:
    response = requests.post(
        URL, data={"method": "getQuote", "format": "json", "lang": "en"}
    )

    if response.status_code == 200:
        return response.json()

    else:
        print(f"Failed to get data from API, error: {response.status_code}")
        return False


def main():
    data = get_data()
    print(f"\n{data.get('quoteText')} - {data.get('quoteAuthor')}\n")


if __name__ == "__main__":
    main()
