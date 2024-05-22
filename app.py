import streamlit as st

def main():
    st.title("Sample Streamlit App")
    st.write("This is a simple Streamlit app.")
    
    if st.button('Say Hello'):
        st.write("Hello, Streamlit!")

if __name__ == "__main__":
    main()
