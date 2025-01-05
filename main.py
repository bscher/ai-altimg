import os
# import argparse
import sys

# Type hints are saving Python's future...
assert (3, 6) <= sys.version_info[:2], "Python 3.6 or greater is required."

# This library
import src

THIS_PATH =  os.path.realpath(__file__)
THIS_DIR = os.path.dirname(THIS_PATH)
EXAMPLES_DIR = os.path.realpath(f"{THIS_DIR}/examples")

def temp_example():
    src.recursive_prompts.prompt_recursively(
        os.path.join(EXAMPLES_DIR, "valley_and_sky.png"),
        "Transform into a silhouette of the original image.",
        "Restrict to only solid black and solid white.",
    )

def main():
    # parser = argparse.ArgumentParser(description="CLI for generating or editing images using Stable Diffusion models.")
    # subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # # Sub-command for image generation
    # generate_parser = subparsers.add_parser("generate", help="Generate a new image from a prompt.")
    # generate_parser.add_argument("--prompt", type=str, required=True, help="Text prompt for image generation.")
    # generate_parser.add_argument("--output", type=str, default="generated_image.png", help="Output file name for the generated image.")

    # # Sub-command for image editing
    # edit_parser = subparsers.add_parser("edit", help="Edit an existing image based on a prompt.")
    # edit_parser.add_argument("--input", type=str, required=True, help="Path to the input image for editing.")
    # edit_parser.add_argument("--prompt", type=str, required=True, help="Text prompt for image editing.")
    # edit_parser.add_argument("--output", type=str, default="edited_image.png", help="Output file name for the edited image.")

    # args = parser.parse_args()

    # #TODO

    # parser.print_help()

    temp_example()


if __name__ == "__main__":
    main()


