from diffusers import StableDiffusionInstructPix2PixPipeline
import torch
from PIL import Image
import os
from datetime import datetime
from typing import List

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_DIR = os.path.abspath(f"{THIS_DIR}/../examples")
EXAMPLES_DIR = os.path.abspath(f"{THIS_DIR}/../examples")

# Define the model to use from Hugging Face
MODEL_NAME = "timbrooks/instruct-pix2pix"  # Model for image manipulation

def run(*prompt_list: List[str]):
    os.makedirs(EXAMPLES_DIR, exist_ok=True)

    # Load the model pipeline
    print("Downloading model and initializing pipeline...")
    pipeline = StableDiffusionInstructPix2PixPipeline.from_pretrained(MODEL_NAME, torch_dtype=torch.float16)
    pipeline = pipeline.to("cuda")  # Use GPU for better performance

    for prompt_id, prompt_text in enumerate(prompt_list):
        prompt_key = str(int(datetime.now().timestamp()))[:-5]

        image_in_path: str
        if prompt_id == 0:
            image_in_path = f"{EXAMPLES_DIR}/image.png"
        else:
            image_in_path = f"{EXAMPLES_DIR}/{prompt_key}.{prompt_id - 1}.g.png"
            
        # Load image
        print(f"[{prompt_id}]: Loading image {image_in_path} ...")
        input_image = Image.open(image_in_path).convert("RGB")

        # Image manipulation
        print(f"[{prompt_id}]: Performing prompt -->> {prompt_text}")
        edited_image = pipeline(prompt=prompt_text, image=input_image).images[0]

        # Save edited image to file
        image_out_path = f"{EXAMPLES_DIR}/{prompt_key}.{prompt_id}.g.png"
        print(f"[{prompt_id}]: Saving the edited image as {image_out_path} ...")
        edited_image.save(image_out_path)

    print("Done!")