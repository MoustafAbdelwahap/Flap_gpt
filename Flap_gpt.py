import streamlit as st
import requests
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://flaplife.openai.azure.com/" 
openai.api_version = "2023-09-15-preview"
openai.api_key = "6e9a3f23b26e4310b630a3e77ba238f7" 

def main():
    st.title("Chat with Flap")
    notes = st.text_area("Enter your text:")
    if st.button("Generate description"):
        with st.spinner("Generating description..."):
          response = openai.Completion.create(
              engine="df",
              prompt=f"Write a product description based on the below information.\n\n{notes}\n\nDescription:",
              temperature=1,
              max_tokens=500,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0,
              stop=None)
          
        try:
          generated_text = response.choices[0].text
          print("Generated Description:")
          print(generated_text)
        except ValueError as e:
          print("Failed to Generated content:")       

        st.subheader("Generated text:")
        st.write(generated_text)

if __name__ == "__main__":
    main()
