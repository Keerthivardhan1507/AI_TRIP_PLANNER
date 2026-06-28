from langchain_groq import ChatGroq
from utils.config_loader import load_config
from dotenv import load_dotenv
from typing import Literal,Optional,Any
import os
from pydantic import BaseModel,Field



class configloader:
    def __init__(self):
        print(f"loading config.......")
        self.config = load_config()
        
        
    def get_item(self,key):
        return self.config[key]
    
    
class ModelLoader(BaseModel):
    model_provider :Literal["groq"] = "groq"
    config : Optional[configloader] = Field(default=None, exclude=True)
    
    
    def model_post_init(self,__context:Any) -> None:
        self.config = configloader()
        
    class Config:
        artibitary_typrs_allowed = True
        
    def load_llm(self):
        """Load the llm model
        """
        print("loading model")
        print(f"loading llm model {self.model_provider}")
        
        if self.model_provider == "groq":
            print("loading groq model")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model"]
            llm = ChatGroq(model = model_name,api_key=groq_api_key)
        return llm