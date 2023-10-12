import openai
import streamlit as st
import requests

def generate_description(input_text):
    url = "https://chatgptapifree.herokuapp.com/generate"
    payload = {
        "model": "text-davinci-003",
        "prompt": f"Write a product description based on the below information.\n\n{input_text}\n\nDescription:",
        "temperature": 0.7,
        "max_tokens": 256,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get("choices", [])[0].get("text", "")
    else:
        return "Failed to generate description. Please try again."

def main():
    st.title("Product Description Generator")
    notes = st.text_area("Enter product information:")

    if st.button("Generate description"):
        with st.spinner("Generating description..."):
            description = generate_description(notes)
            st.subheader("Generated description:")
            st.write(description)

if __name__ == "__main__":
    main()
