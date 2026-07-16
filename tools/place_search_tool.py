import os
from utils.place_info_search import GooglePlaceSearchTool,TavilyPlaceSearchTool
from dotenv import load_dotenv
load_dotenv()
from typing import List
from langchain.tools import tool

class PlaceSearchTool:
    def __init__(self):
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_tool_list = self._setup_tools()
    
    def _setup_tools(self)->List:
        """Setup tools for the google place search tool"""
        @tool
        def search_attractions(place:str)->str:
            """search for the attractions of the place"""
            try:
                attraction_result = self.google_places_search.google_search_restaurents(place)
                if attraction_result:
                    return f"Following are the attractions of the {place}the places are {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurents(place)
                return f"Google cannoot find the details due to{e} and the following results from \n the attractions are{tavily_result}"
            
        @tool
        def search_restautrents(place:str)->str:
            """search for the restaurents in the place"""
            try:
                restaurents_result = self.google_places_search.google_search_attractions(place)
                if restaurents_result:
                    return f"Following restaurents of the {place} are {restaurents_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurents(place)
                return f"Google cannot find the restaurents due to error {e} and the restaurents listed from {tavily_result}"
            
        @tool
        def search_activity(place:str)->str:
            """search activity happeing in the place"""
            try:
                activity_result = self.google_places_search.google_search_activity(place)
                return f"the activities happeing in and around {place} are {activity_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the activities happenig due to {e} and the places are {tavily_result}"
            
        @tool
        def search_transportation(place:str)->str:
            """search for transportation in the place"""
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                return f"the transportation available in the {place} are {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot found transportation due to {e} and the available transportation is {tavily_result}"
        return [search_attractions,search_restautrents,search_activity,search_transportation]         
            
            
            
        
        
