import streamlit as st
import textwrap
from IPython.display import Markdown
import google.generativeai as genai

# Helper function to display response in Markdown format
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Set up GenerativeAI API key
genai.configure(api_key='AIzaSyC5fgNcnuHC3uJDPlxWwD8Kj-05m1eGSDc')  # Replace with your API key

# Function to generate response using Gemini model
def generate_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

# Streamlit app
def main():
    st.title('Gemini Model - Input and Response')

    # Text input for user
    input_text = st.text_area('Enter your input here:', value='')

    if st.button('Generate Response'):
        if input_text:
            # Generate response using the Gemini model
            response = generate_response(input_text)
            st.markdown('**Response:**')
            st.markdown(response)
            # print(response)
        else:
            st.warning('Please enter some text.')

if __name__ == '__main__':
    main()

# import google.generativeai as genai
# genai.configure(api_key='AIzaSyC5fgNcnuHC3uJDPlxWwD8Kj-05m1eGSDc')
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
# model = genai.GenerativeModel('gemini-pro')