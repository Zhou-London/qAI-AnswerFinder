"""
Configuration file for Manticore Search
"""

import manticoresearch
from dotenv import load_dotenv
import os

# Get Manticore host
load_dotenv()
manticore_host = os.getenv("MANTICORE_HOST")
config = manticoresearch.Configuration(host=manticore_host)


class Agent:
    def __init__(self):
        self.client = manticoresearch.ApiClient(config)
        self.index_api = manticoresearch.IndexApi(self.client)
        self.search_api = manticoresearch.SearchApi(self.client)
        self.util_api = manticoresearch.UtilsApi(self.client)


manticore_agent = Agent()
