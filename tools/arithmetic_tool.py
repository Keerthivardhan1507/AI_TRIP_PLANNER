import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

@tool
def multiply(a:int,b:int)->int:
    """Multiply the numbers

    Args:
        a (int): The first integer
        b (int): The Secomnd interger

    Returns:
        int: Product of a and b
    """
    return a*b

@tool
def addition(a:int,b:int)->int:
    """Addition of the numbers

    Args:
        a (int): The first integer
        b (int): The Second integer

    Returns:
        int: Sum of a and b
    """
    return a+b


@tool
def currency_converter(from_curr:str,to_curr:str,value:float)-> float:
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv('ALPHAVANTAGE_API_KEY')
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_curr,to_curr)
    exchange_rate = response['Realtime currency Exchaneg Rate']['5. Exchange Rate']
    return value*float(exchange_rate)
    
    