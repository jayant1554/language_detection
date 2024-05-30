import streamlit as st
import requests

# Function to make a request to the Flask API
def detect_language(text):
    url = 'http://localhost:5000/detect_language'  # Adjust the URL if necessary
    payload = {'text': text}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['language']
    else:
        return None

# Streamlit app
def main():
    st.title('Language Detection')

    # Input text box
    text_input = st.text_area('Enter text:', '')

    # Button to detect language
    if st.button('Detect Language'):
        if text_input:
            # Call the detect_language function to get the predicted language
            predicted_language = detect_language(text_input)
            if predicted_language:
                st.success(f'Predicted language: {predicted_language}')
            else:
                st.error('Language detection failed. Please try again.')
        else:
            st.warning('Please enter some text.')

if __name__ == '__main__':
    main()