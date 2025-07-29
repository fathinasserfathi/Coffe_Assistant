import streamlit as st
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

# تحميل مفتاح OpenAI من .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("🔑 API KEY:", api_key)

# تهيئة GPT
chat = ChatOpenAI(openai_api_key=api_key, model="gpt-4", temperature=0.6)

st.set_page_config(page_title="Coffee Shop Assistant ☕️")
st.title("☕️ Coffee Shop Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="أنت مساعد داخل كوفي شوب. ساعد العميل يختار مشروب. اسأله عن الحرارة، درجة السكر، والإضافات. سجل الطلب وارجع له رسالة تأكيد."
        )
    ]

user_input = st.chat_input("كيف أقدر أخدمك اليوم؟")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    response = chat(st.session_state.messages)
    st.session_state.messages.append(response)

for msg in st.session_state.messages[1:]:
    if isinstance(msg, HumanMessage):
        st.write(f"🧑: {msg.content}")
    else:
        st.write(f"🤖: {msg.content}")
