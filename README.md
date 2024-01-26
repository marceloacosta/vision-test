# GPT-4 Vision Test

This project is a Streamlit application that uses OpenAI's GPT-4 Vision model to analyze images. It provides two modes of operation: 

1. **Camera input test**: This mode allows you to capture an image using your webcam, which is then analyzed by the GPT-4 Vision model.
2. **Upload picture test**: This mode allows you to upload an image file, which is then analyzed by the GPT-4 Vision model.

## Setup

Follow these steps to set up and run the project:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourrepository.git
```
3. Navigate to the project directory:

```bash
cd yourrepository
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```
The requirements.txt file should include:
```
streamlit
cloudinary
openai
python-dotenv
```
4. Set up your environment variables. You'll need to provide your Cloudinary and OpenAI credentials. Create a .env file in the project root and add the following lines:
```
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
OPENAI_API_KEY=your_openai_api_key
```

Replace your_cloudinary_cloud_name, your_cloudinary_api_key, your_cloudinary_api_secret, and your_openai_api_key with your actual credentials.

5. Run the Streamlit application:
```
streamlit run app.py
```
# Usage
Once the application is running, you can select the mode of operation from the sidebar. Depending on the mode you select, you'll either be prompted to capture an image with your webcam or upload an image file. After the image is captured or uploaded, it will be analyzed by the GPT-4 Vision model, and the results will be displayed on the screen.

