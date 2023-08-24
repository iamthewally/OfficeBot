# filename: interaction_handlers.py

import streamlit as st
from chat_operations import calculate_token_count, trim_chat_history, generate_response
from file_operations import load_models, load_systems, load_characters


def handle_user_input(user_input, character, discussion_text, selected_systems_data, model_specs):
    context_length = model_specs['context_length']
    model_name = model_specs['name']

    # Add a tag to the discussion text
    discussion_tag = "Attached Document: " if discussion_text else ""
    discussion_text_with_tag = discussion_tag + discussion_text

    user_input_with_discussion = user_input + " " + discussion_text_with_tag
    current_token_count = calculate_token_count(user_input_with_discussion)

    # Make a copy of the chat history so the original remains intact
    chat_history_to_process = st.session_state.chat_history.copy()

    # Trim the copied chat history
    chat_history_to_process = trim_chat_history(chat_history_to_process, context_length - current_token_count, character['prompt'], character, selected_systems_data, discussion_text)

    st.sidebar.markdown(f"Current Tokens: {current_token_count}")

    if user_input:
        st.session_state.chat_history.append((user_input, "Human"))
        bot_response = generate_response(user_input_with_discussion, chat_history_to_process, model_name, character, selected_systems_data, discussion_text)
        st.session_state.token_count += current_token_count
        st.session_state.chat_history.append((bot_response, character['name']))


def process_user_interaction(character_key, characters, systems, models_config, model_key, selected_system_keys):
    user_input = st.chat_input(characters[character_key]['greeting'], key='user_input') or ""
    discussion_text = st.sidebar.text_area("Discussion", key='discussion_text').strip()

    if 'last_user_input' not in st.session_state:
        st.session_state.last_user_input = ""

    if user_input != st.session_state.last_user_input:
        st.session_state.last_user_input = user_input
        selected_systems_data = "".join([systems[key]['data'] for key in selected_system_keys])

        model_specs = models_config['openai_models'][model_key]

        handle_user_input(user_input, characters[character_key], discussion_text, selected_systems_data, model_specs)