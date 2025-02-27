import streamlit as st
import requests

def main():
    st.title("FastAPI PDF + URL Tester")

    # Text input for URL
    url_input = st.text_input("Enter the Job URL:")

    # File uploader for PDF
    pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])

    # Button to send request
    if st.button("Submit"):
        if url_input and pdf_file:
            with st.spinner("Sending request..."):
                # Prepare multipart/form-data payload
                files = {
                    "source": (pdf_file.name, pdf_file.read(), "application/pdf")
                }
                data = {
                    "url": url_input
                }

                # POST to your FastAPI endpoint
                response = requests.post(
                    "http://localhost:8000/generate",
                    files=files,
                    data=data
                )

                if response.status_code == 200:
                    st.success("Request Successful!")
                    # Display JSON response
                    st.json(response.json())
                else:
                    st.error(f"Request failed with status code {response.status_code}")
                    st.write(response.text)
        else:
            st.warning("Please provide both a URL and a PDF file before submitting.")

if __name__ == "__main__":
    main()
