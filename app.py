from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()


if "chat_history" not in st.session_state:
    st.session_state.chat_history =[]


st.set_page_config(page_title="Streming Bot")

st.title("Streaming Bot")

user = st.chat_input("Your Message")
if user is not None and user !="":
    st.session_state.chat_histpry.append(HumanMessage(user))

    with st.chat_message("Human"):
        st.markdown(user)




