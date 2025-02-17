import streamlit as st
import base64
import requests

st.title("Upload Files and URLs")
st.subheader("This page is designed for identifying images from files and URLs. Currently, you can upload docx, pptx, xlsx, jpg, jpeg, and png files. It is also a good tool for analyzing content from a screenshot.", divider="gray")
st.sidebar.success("Select an agent from the dropdown above.")

# CSS for the image gallery
st.markdown(
    """
    <style>
    .image-gallery {
        display: flex;
        flex-wrap: wrap;
        gap: 10px; /* Adjust the gap between boxes as needed */
    }
    .image-container {
        width: 300px;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid #ddd;
        overflow: hidden;
    }
    .image-container img {
        max-width: 100%;
        max-height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

######################################################
# UPLOAD FILES (Local/Network share)
######################################################

uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, type=["docx", "pptx", "xlsx", "jpg", "png"])
if uploaded_files is not None:
    if "image_urls" not in st.session_state:
        st.session_state["image_urls"] = []

    for file in uploaded_files:
        files = {"file": (file.name, file, file.type)}
        response = requests.post("http://localhost:8000/upload-file", files=files)
        if response.status_code == 200:
            st.success(f"File {file.name} uploaded successfully!")
        else:
            st.error(f"Failed to upload file {uploaded_file.name}.")

    for f in uploaded_files:
        if f.type in ["image/png", "image/jpeg", "image/jpg"]:
            encoded_data = base64.b64encode(f.getvalue()).decode("utf-8")
            st.session_state["image_urls"].append(encoded_data)
    
    st.write(f"The number of images files processed is {len(st.session_state['image_urls'])}")
    
    for image_url in st.session_state["image_urls"]:
        st.markdown(
            f"""
            <div class="image-container">
                <img src="data:image/png;base64,{image_url}" />
            </div>
            """,
            unsafe_allow_html=True
        )        

########################################################
# UPLOAD URL FILE
########################################################

multi_urls_input = st.text_area("Enter multiple URLs (one per line)")
if st.button("Upload Multiple URLs"):
    urls = [u.strip() for u in multi_urls_input.split("\n") if u.strip()]
    for u in urls:
        response = requests.post("http://localhost:8000/url-file", json={"url": u})
        if response.status_code == 200:
            st.success(f"Uploaded {u} successfully!")
        else:
            st.error(f"Failed to upload {u}.")
