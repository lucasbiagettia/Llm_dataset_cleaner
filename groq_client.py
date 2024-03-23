from langchain_groq import ChatGroq
from langchain.chains import LLMChain


class Chatbot:

    def __init__(self, api_key, prompt_provider):
        self.initialize(api_key, prompt_provider)

    def initialize(self, api_key, prompt_provider ,llm_model="mixtral-8x7b-32768"):
        self.model = self.load_model(api_key = api_key, llm_model = llm_model)
        self.prompt = prompt_provider.get_prompt()
        self.is_initialized = True

    def load_model(self, api_key, llm_model):
        return ChatGroq(groq_api_key=api_key, model_name=llm_model, temperature=0.2, verbose=True)
   

    def make_request(self, context):
        self.qa_chain: LLMChain = LLMChain(llm=self.model, prompt=self.prompt) 
        prediction_msg: dict = self.qa_chain.invoke({'context': context})
        return prediction_msg['text']   
    