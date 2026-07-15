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
        return self.places_tool.run(f"top attractive places in and around{place}")
        
    def google_search_restaurents(self,place:str)->dict:
        """search for the nearby restautrents from the place using google places api"""
        return self.places_tool.run(f"top restaurents in {place}")
    
    def google_search_activity(self,place:str)->dict:
        """ Search for special activity in the search place"""
        return self.places_tool.run(f"Activities in and around{place}")
    def google_search_transportation(self,place:str)->dict:
        """search for the transportation in the place"""
        return self.places_tool.run(f"Available transportation in {place}")
    
class TavilyPlaceSearchTool:
    def __init__(self):
        pass
    
    def tavily_search_attractions(self,place:str)->dict:
        """search for the nearby attractive places using TavilySearch"""
        tavily_tool = TavilySearch(topic = "general",include_answer = "advanced")
        result = tavily_tool.invoke({"query":f"top neraby attractive places in {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurents(self,place:str)->dict:
        """search for the nearby restaurents in the place using TavilySearch"""
        tavily_tool = TavilySearch(topic = "general",include_answer = "advanced")
        result = tavily_tool.invoke({"query":f"top restaurents in the neraby {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self,place:str)->dict:
        """search for any activity going on in the place using TavilySearch"""
        tavily_tool = TavilySearch(topic = "general",include_answer = "advanced")
        result = tavily_tool.invoke({"query":f"Activities going on {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_transportation(self,place:str)->dict:
        """search for the transportation in the place using TavilySearch"""
        tavily_tool = TavilySearch(topic = "general",include_answer = "advanced")
        result = tavily_tool.invoke({"query":f"available transprtation in {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
        
        
        
    
        