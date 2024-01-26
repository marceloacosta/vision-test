import streamlit as st
import cloudinary.uploader
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
_ = load_dotenv(find_dotenv())

# Initialize OpenAI client
client = OpenAI()

# Cloudinary configuration
cloudinary.config(
  cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'), 
  api_key = os.getenv('CLOUDINARY_API_KEY'),
  api_secret = os.getenv('CLOUDINARY_API_SECRET')
)

def camera_input():
    st.title("GPT-4 Vision camera input test")

    # Webcam input
    captured_image = st.camera_input("Take a picture")

    if captured_image is not None:
        # Convert the captured image to bytes
        image_bytes = captured_image.getvalue()

        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(image_bytes, folder="streamlit-uploads/")
        image_url = upload_result['url']
        
        # Display the uploaded image
        st.image(image_url, caption="Captured Image", use_column_width=True)

        # Make a request to OpenAI API
        try:
            response = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "extract all the text in the picture and describe the rest which is not text"},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_url,
                                },
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )
            st.write(response.choices[0])
        except Exception as e:
            st.error(f"An error occurred: {e}")

def file_upload():
    st.title("GPT-4 Vision uploading picture test")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Upload the image to Cloudinary
        upload_result = cloudinary.uploader.upload(uploaded_file, folder="streamlit-uploads/")
        image_url = upload_result['url']
        
        # Display the uploaded image
        st.image(image_url, caption="Uploaded Image", use_column_width=True)

        # Make a request to OpenAI API
        try:
            response = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "extract all the text in the picture and describe the rest which is not text"},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_url,
                                },
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )
            st.write(response.choices[0])
        except Exception as e:
            st.error(f"An error occurred: {e}")

def main():
    st.sidebar.title("GPT-4 Vision Test")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Camera input test", "Upload picture test"])
    if app_mode == "Camera input test":
        camera_input()
    elif app_mode == "Upload picture test":
        file_upload()

if __name__ == "__main__":
    main()