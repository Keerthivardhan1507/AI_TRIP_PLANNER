import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool,GooglePlacesAPIWrapper

class GooglePlaceSearchTool:
    def __init__(self,api_key:str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)
        
        
    def google_search_attractions(self,place:str)->dict:
        """search for the attractive places near the place using googleplaces api"""
        self.places_tool.run(f"top attractive places in and around{place}")
        
    
        