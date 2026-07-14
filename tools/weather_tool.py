import os
from dotenv import load_dotenv
from langchain.tools import tool
from utils.weather_info import WeatherForecastTool


class WeatherInformationTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list  = self._setup_tools()
        
    def _setup_tools(self):
        """setup all the tools for the weather Forecast"""
        @tool
        def get_current_weather(city:str) ->str:
            """Get the current weather of the city"""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main',{}).get('temp','N/A')
                desc = weather_data.get('weather',[{}])[0].get('description','N/A')
                return f"current weather in{city}:{temp}C,{desc}"
            return f"could not fetch current weather in {city}"
        
        @tool
        def get_forecast_weather(city:str)-> str:
            """Get the forecast weather of the city"""
            forecast_data = self.weather_service.forecast_weather(city)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = item['dx_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}:{temp},degree celcious,{desc}")
                return f" weather forecast of the {city}:\n" + "\n".join(forecast_summary)
            return f"could not fetch the weather forecast for the city"
        
        return [get_current_weather,get_forecast_weather]
                    
        

