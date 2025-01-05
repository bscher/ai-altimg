from diffusers import StableDiffusionInstructPix2PixPipeline
import torch
from PIL import Image
import os
from datetime import datetime
from typing import List

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
EXAMPLES_DIR = os.path.abspath(f"{THIS_DIR}/../examples")
OUT_DIR = os.path.abspath(f"{THIS_DIR}/../out")

# Define the model to use from Hugging Face
MODEL_NAME = "timbrooks/instruct-pix2pix"  # Model for image manipulation

def prompt_recursively(initial_image_path: str, *prompt_list: List[str]):

    # Check if initial image exists
    initial_image_path = os.path.abspath(initial_image_path)
    assert os.path.exists(initial_image_path), f"Initial image not found at {initial_image_path}!"
    print(f"Initial image found at {initial_image_path}")

    # Load the model pipeline
    print("Downloading and initializing model pipeline...")
    pipeline = StableDiffusionInstructPix2PixPipeline.from_pretrained(MODEL_NAME, torch_dtype=torch.float16)

    # Use CUDA for better performance if supported
    if torch.cuda.is_available():
        print("Using CUDA.")
        pipeline = pipeline.to("cuda")
    else:
        print("WARNING: Using CPU because CUDA is not available! Processing time will be significantly longer.")
        pipeline = pipeline.to("cpu")

    # A unique key to differentiate between runs. Currently using the trailing digits of the `now()` timestamp.
    prompt_key = str(int(datetime.now().timestamp()))[:-6]

    print(f"Processing image recursively through {len(prompt_list)} prompts ...")
    current_image_path: str = initial_image_path

    for prompt_id, prompt_text in enumerate(prompt_list):
        print(f"== Prompt: {prompt_id} / {len(prompt_list)}")

        # Each iteration will have the previous image as the input
        prev_image_path = current_image_path
        gen_image_path = f"{EXAMPLES_DIR}/{prompt_key}.{prompt_id}.g.png"
            
        # Load image
        print(f"[{prompt_id}]: Loading image {prev_image_path} ...")
        input_image = Image.open(prev_image_path).convert("RGB")

        # Image manipulation
        print(f"[{prompt_id}]: Performing prompt \n-----\n{prompt_text}\n-----\n...")
        edited_image = pipeline(prompt=prompt_text, image=input_image).images[0]

        # Save edited image to file
        print(f"[{prompt_id}]: Saving the edited image as {gen_image_path} ...")
        edited_image.save(gen_image_path)

    print("Done!")