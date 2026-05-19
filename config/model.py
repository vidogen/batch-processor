from google.genai.interactions import image_config
from langchain_google_genai import ChatGoogleGenerativeAI
from config.constants import GOOGLE_API_KEY

gemini_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-image",
    api_key=GOOGLE_API_KEY,
    image_config={"aspect_ratio": "16:9"}
)