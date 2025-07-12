
from streamlit_chat import message
import streamlit as st
import time

import requests




# generate a response
def generate_response_server_revolvIA_tuto(prompt):
    

    # Replace with your actual server URL if different.
    url = "http://fastapi:8000/conversational_agent_ret_sql"

    # Set up your query parameters.
    params = {
        "prompt": prompt,
        "history_messages": st.session_state.messages
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("Response:", response.json())
        data = response.json()

    else:
        print("Error:", response.status_code, response.text)
        data = {"output": "Error: Unable to get a response from the server."}


    return data['output']



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []



# Using object notation
add_selectbox = st.sidebar.selectbox(
    "What you would like to do?",
    ("RevolvIA DevOps Database Assistant")
)


# Using "with" notation
with st.sidebar:

    if 'placeholder' not in st.session_state:
        st.session_state.placeholder = st.empty()


if 'RevolvIA DevOps Database Assistant' in add_selectbox:

    st.title("DevOps RevolvIA Database Assistant")
    st.text("Talk with RevolvIA to learn about the tables!")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    output = None

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        output = generate_response_server_revolvIA_tuto(prompt)
        



    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        
        message_placeholder = st.empty()

                
        full_response = ""
        
        if output is None and len(st.session_state.messages) == 0:
            assistant_response = 'Hello, how can I assist you today?'
        else:
            assistant_response = output

        if assistant_response is not None:

            message_placeholder.markdown(assistant_response)
    
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
