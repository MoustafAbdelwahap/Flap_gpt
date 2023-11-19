# Version3

import streamlit as st
import openai

openai.api_type = "azure"
openai.api_base = "https://flaplife.openai.azure.com/"
#openai.api_version = "2023-09-15-preview"
openai.api_key = "6e9a3f23b26e4310b630a3e77ba238f7"

def main():
    st.title("Chat with Flap ; Create your Action plan !!")

    # Create text input boxes for user inputs
    Country = st.text_input("Country where you want to travel!")
    degree_type = st.text_input("What degree are you seeking!")
    field = st.text_input("Field of study!")
    year = st.text_input("Which year are you planning to start studying!")

    Current_Academic_Status = st.text_input("Enter your current academic status:")
    Achievements = st.text_input("Enter academic achievements or awards you'd like to highlight:")
    Universities = st.text_input("Enter specific universities you are interested in applying to:")
    scholarships = st.text_input("Are you seeking financial aid or scholarships? (Yes/No):")
    Your_Country = st.text_input("Enter your country of origin for VISA Requirements:")
    circumstances = st.text_input("Enter any unique circumstances or personal obligations that may affect your application timeline:")

    # Generate description based on user inputs
    if st.button("Generate"):
        with st.spinner("Generating the plan..."):
            prompt = f"""
I want to travel and study in {Country} for {degree_type} degree in {field} in {year}.
I want it to create an action plan highlighting the milestones/roadmap that guides me how to apply setting monthly targets and mention everything that I need to do starting from this month!
To create a highly specific monthly action plan, please consider more details below about the circumstances and goals:
What is your Current Academic Status? {Current_Academic_Status}
Are there any specific academic achievements or awards you'd like to highlight? {Achievements}
Which specific universities are you interested in applying to? {Universities}
Are you seeking financial aid or scholarships? {scholarships}
For Visa Requirements, What is your country of origin? {Your_Country}
Are there any unique circumstances or personal obligations that may affect your application timeline? {circumstances}
Please be specific and to the point. Mention every month (starting from November 2023) in a separate line and below some bullet points with things to do
"""
            response = openai.Completion.create(
                #engine="df",
                engine="gpt-3.5-turbo",
                prompt=prompt,
                temperature=1,
                max_tokens=500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None)
        try:
            #generated_text = response.choices[0].text
            generated_text =response['choices'][0]['text']
            st.subheader("Generated Action Plan:")
            st.write(generated_text)
        except ValueError as e:
            st.error("Failed to generate content.")

if __name__ == "__main__":
    main()
