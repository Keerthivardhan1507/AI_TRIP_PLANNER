import os
from typing import List,Any,Dict
from utils.expense_calculator import Calculator
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()
        
    def _setup_tools(self) ->List:
        """setup tools for the ClculatorTool"""
        @tool
        def estimate_hotel_cost(price_per_night:str,total_days:float)->float:
            """Claculate total hotel cost"""
            return self.calculator.multiply(price_per_night,total_days)
        
        @tool
        def calculate_total_expense(*cost:float) -> float:
            """claculate total expense"""
            return self.calculator.calculate_total(*cost)
        
        @tool
        def calculate_daily_budget(total_cost:float,total_days:int)-> float:
            """calculate daily cost"""
            return self.calculator.calculate_daily_budget(total_cost,total_days)
        
        return[estimate_hotel_cost,calculate_total_expense,calculate_daily_budget]
