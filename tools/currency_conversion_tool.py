import os
from typing import List,Dict,Any
from utils.currency_converter import CurrencyConverter
from dotenv import load_dotenv
from  langchain.tools import tool


class CurrencyConTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tools_list = self._setup_tools()
        
    def _setup_tools(self)->List:
        """setup tools for the cuurency converter tool"""
        
        @tool
        def convert_currency(amount:float,from_curr:str,to_curr:str):
            """convert currency from one currency to another"""
            return self.currency_service.convert(amount,from_curr,to_curr)
        return [convert_currency]
            
            
    
    
