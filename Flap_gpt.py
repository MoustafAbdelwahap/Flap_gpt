import openai
import streamlit as st
import requests

import streamlit as st
import chatgpt

import openai
import streamlit as st

openai.api_key="key"

def main():
    st.title("Chat with Flap")
    notes = st.text_area("Enter your text:")
    if st.button("Generate description"):
        with st.spinner("Generating description..."):
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt=f"Write a product description based on the below information.\n\n{notes}\n\nDescription:",
              temperature=0.7,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
        description = response['choices'][0]['text']
        st.subheader("Generated text:")
        st.write(description)

if __name__ == "__main__":
    main()
