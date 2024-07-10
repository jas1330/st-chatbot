# Save the script as app.py in the colab environment
with open('app.py', 'w') as f:
    f.write('''
import streamlit as st

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Define the Home page
def home():
    st.title("Home")
    st.write("Welcome to the Chatbot App!")

# Define the Chat page
def chat():
    st.title("Chat")
    user_input = st.text_input("You: ", "")

    if user_input:
        # Simulate a chatbot response
        response = f"Bot: You said '{user_input}'"
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

    if st.session_state.chat_history:
        st.write("Chat History:")
        for speaker, message in st.session_state.chat_history:
            st.write(f"{speaker}: {message}")

# Define the Login page
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# Define the History page
def history():
    st.title("History")
    if st.session_state.chat_history:
        st.write("Chat History:")
        for speaker, message in st.session_state.chat_history:
            st.write(f"{speaker}: {message}")
    else:
        st.write("No chat history available.")

# Main function to handle navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Home", "Chat", "Login", "History"])

    if page == "Home":
        home()
    elif page == "Chat":
        chat()
    elif page == "Login":
        login()
    elif page == "History":
        history()

if __name__ == "__main__":
    main()
    ''')
