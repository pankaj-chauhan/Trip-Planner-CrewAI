import json
import os

import requests
from langchain.tools import tool


class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        