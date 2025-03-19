import streamlit as st
import requests

st.title("📊 Data Analyst Agent")

uploaded_file = st.file_uploader("Upload a document (.doc, .txt, .xlsx, .csv, .pdf, image file)")

if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
    response = requests.post("http://127.0.0.1:8000/upload/", files=files)

    if response.status_code == 200:
        data = response.json()
        st.session_state["uploaded_data"] = data
        st.write(data)
    else:
        st.error(f"Failed to process the file. Server response: {response.text}")

st.subheader("Ask Questions to the LLM")
question = st.text_input("Enter your question:")

if st.button("Ask"):
    if "uploaded_data" in st.session_state and "content" in st.session_state["uploaded_data"]:
        response = requests.post(
            "http://127.0.0.1:8000/analyze/",
            data={"question": question, "text": st.session_state["uploaded_data"]["content"]}
        )

        # ✅ Debugging: Print API response before parsing JSON
        print(f"Raw API Response: {response.text}")  # Log output
        st.text(f"Raw API Response: {response.text}")  # Show in Streamlit UI

        try:
            result = response.json()
            st.write(result)
        except requests.exceptions.JSONDecodeError:
            st.error(f"Error parsing JSON. Server response: {response.text}")
    else:
        st.error("No extracted text found. Upload a file first.")
