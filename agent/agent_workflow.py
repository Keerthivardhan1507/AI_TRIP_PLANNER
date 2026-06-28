from utils.config_loader import load_config
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph,END,START,MessagesState
from langgraph.prebuilt import ToolNode,tools_condition





class GraphBuilder:
    def __init__(self,model_provider:str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        self.tools = []
    
    def agent_function(self,state:MessagesState):
        """Main Agent Function"""
        user_questions = state["messages"]
        
        pass
    
    
    
    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
    
    def __call__(self):
        pass
