from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.agent_workflow import GraphBuilder
from utils.save_to_document import save_document
import os
from starlette.responses import JSONResponse
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


class QyeryRequest(BaseModel):
    query :str
    
@app.post("/query")

async def qyery_travel_agent(query:QyeryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()
        
        png_graph = react_app.get_graph().draw_mermaid_png()
        
        with open(png_graph,"wb") as f:
            f.write(png_graph)
            
        print(f"graph saved as 'png_graph.png' in {os.getcwd()}")
        messages = {"messages":[query.question]}
        output = react_app.invoke(messages)
        
        if isinstance (output,dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)
            
        return {"answer":final_output}
    
    except Exception as e:
        return JSONResponse(status_code= 500,content={"error":str(e)})
        
            
        
