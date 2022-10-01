#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, requests
from typing import Optional
import os
from time import sleep

def get_data() -> Optional[dict]:
    url = "https://api.chucknorris.io/jokes/random"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return json.loads(response.content)
        
    else:
        print(f"Failed to get data from API, error: {response.status_code}")
        return False

def main():
    joke = jokes_data.get("value") 
    print(f"\n{joke}\n")

if __name__ == "__main__":
    main()
