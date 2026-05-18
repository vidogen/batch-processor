import base64
from datetime import datetime
import json
from pathlib import Path
import uuid
from langchain.messages import AIMessage
from config.model import gemini_model

GENERATED_IMG_DIR = Path("generated_char_sheets")
GENERATED_IMG_DIR.mkdir(exist_ok=True)

def _get_image_base64(response: AIMessage) -> None:
    try:
        image_block = next(
        block
        for block in response.content
        if isinstance(block, dict) and block.get("image_url")
        )
        image_url = image_block["image_url"].get("url")
        
        if not image_url:
            raise ValueError("No image url found in response")
    
        return image_url.split(",")[-1]

    except StopIteration:
        raise ValueError("No image blovk found in response")
    
    except Exception as e:
        raise RuntimeError(f"Failed to extract image base64: {e}")


def generate_image_from_json(character_json: str) -> str :
    try:
        response = gemini_model.invoke(f"Generate a character sheet on a clear white background for this character: {character_json}")

        image_base64 = _get_image_base64(response)

        image_bytes = base64.b64decode(image_base64)

        project_id = f"proj{uuid.uuid1()}"
        character_id = f"char{uuid.uuid1()}"
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        filename = f"{project_id}-{character_id}-{timestamp}.png"
        file_path = GENERATED_IMG_DIR / filename

        with open(file_path, "wb") as f:
            f.write(image_bytes)

        print(f"Image saved at: {file_path}")

        return str(file_path)

    except base64.binascii.Error:
        raise ValueError("Invalid base64 image data")

    except Exception as e:
        raise RuntimeError(f"Image generation failed: {e}")

def run_img_gen_test():
    with open("mock_char.json", "r") as f:
        jsonData = json.load(f) 

    json_str = json.dumps(jsonData) 
    generate_image_from_json(json_str)


run_img_gen_test()