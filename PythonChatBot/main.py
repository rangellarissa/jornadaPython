import streamlit as st
from openai import OpenAI

model = OpenAI()

st.write("Chatbot com IA")

user_text = st.chat_input("Digite sua mensagem")

if "message_list" not in st.session_state:
    st.session_state["message_list"] = []

for message in st.session_state["message_list"]:
    st.chat_message(message["role"]).write(message["content"])

if user_text:
    st.chat_message("user").write(user_text)
    user_message = {
        "role": "user",
        "content": user_text
    }
    st.session_state["message_list"].append(user_message)

    answer_ai = model.chat.completions.create(
        messages = st.session_state["message_list"],
        model = "gpt-4o-mini"
    )

    answer_ai_text = answer_ai.choices[0].message.content
    st.chat_message("assistant").write(answer_ai_text)
    message_ai = {
        "role": "assistant",
        "content": answer_ai_text
    }
    st.session_state["message_list"].append(message_ai)

