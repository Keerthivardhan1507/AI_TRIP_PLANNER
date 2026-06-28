from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent_workflow import GraphBuilder
import os
from starlette.responses import JSONResponse
app = FastAPI()


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
            
        print(f"graph saved as png_graph in {os.getcwd()}")
        messages = {"messages":[query.question]}
        output = react_app.invoke(messages)
        
        if isinstance (output,dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)
            
        return {"answer":final_output}
    
    except Exception as e:
        return JSONResponse(status_code= 500,content={"error":str(e)})
        
            
        
