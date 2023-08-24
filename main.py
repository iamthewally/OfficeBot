# filename: main.py

from file_operations import load_systems, load_characters, load_models, setup_openai
from chat_operations import display_chat_history, calculate_token_count
from interaction_handlers import handle_user_input, process_user_interaction

import streamlit as st

def initialize_app():

    st.set_page_config(layout="wide")
    characters = load_characters()
    models_config = load_models()
    systems = load_systems()

    st.markdown("<h1 style='text-align: center;'>WolfieChat</h1>", unsafe_allow_html=True)

    # Define a default character_key
    character_key = list(characters.keys())[0] # or any other logic to select a default key

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [(characters[character_key]['greeting'], characters[character_key]['name'])]
        st.session_state.token_count = 0

    setup_openai(models_config['api_key'])

    return characters, systems, models_config


def end_app(character, characters):
    display_chat_history(st.session_state.chat_history, characters[character])
    st.sidebar.markdown(f"Total Tokens: {st.session_state.token_count}")


def main():
    print("Starting main function")

    characters, systems, models_config = initialize_app()
    default_model_key = models_config['default']

    character_key = st.sidebar.selectbox('Character:', options=list(characters.keys()))
    model_key = st.sidebar.selectbox('Model:', options=list(models_config['openai_models'].keys()), index=list(models_config['openai_models'].keys()).index(default_model_key))
    selected_system_keys = st.sidebar.multiselect('Knowledge domains:', options=list(systems.keys()))

    process_user_interaction(character_key, characters, systems, models_config, model_key, selected_system_keys)
    end_app(character_key, characters)


if __name__ == "__main__":
    main()