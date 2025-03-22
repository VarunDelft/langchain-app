from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()

model = init_chat_model("gpt-4o-mini", model_provider="openai")
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

model.invoke(messages)