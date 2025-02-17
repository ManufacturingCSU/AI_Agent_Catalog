import streamlit as st
import base64
import requests

st.title("This is my stubbed page")
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

uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True, type=["docx", "pptx", "xlsx", "jpg", "png"])
if uploaded_files is not None:
    if "image_urls" not in st.session_state:
        st.session_state["image_urls"] = []

    # file_data = [("files", (f.name, f.getvalue(), f.type)) for f in uploaded_files]
    # response = requests.post("http://127.0.0.1:8000/receive_binary_files", files=file_data)
    
    print(f"what is uploaded_files: {type(uploaded_files)}")

    payload = {"binary_files": uploaded_files}
    response = requests.post("http://127.0.0.1:8000/receive_binary_files", data=payload)

    st.write(f"Response: {response.status_code}")
    if response.ok:
        results = response.json()
        print(results)



    for f in uploaded_files:
        if f.type in ["image/png", "image/jpeg", "image/jpg"]:
            encoded_data = base64.b64encode(f.getvalue()).decode("utf-8")
            st.session_state["image_urls"].append(encoded_data)


    
    st.write(f"The number of files converted to base64 is {len(st.session_state['image_urls'])}")
    
    for image_url in st.session_state["image_urls"]:
        st.markdown(
            f"""
            <div class="image-container">
                <img src="data:image/png;base64,{image_url}" />
            </div>
            """,
            unsafe_allow_html=True
        )        
        # st.image(f"data:image/png;base64,{image_url}").resize(300, 300)


        # image_urls.append(f"data:image/png;base64,{img_base64}")
        # await workwithbase64encodedimages(image_urls)
        # async def workwithbase64encodedimages(image_urls:list):