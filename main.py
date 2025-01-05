import src

import os
import argparse

def do_example():
    src.example.run(
'''
Transform this image into a simple children's drawing.
'''
,
"Make this image simpler.",
"Make this image simpler.",
"Make this image simpler.",
"Restrict this image to only use solid black and solid white."
)

def main():
    parser = argparse.ArgumentParser(description="CLI for generating or editing images using Stable Diffusion models.")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Sub-command for image generation
    generate_parser = subparsers.add_parser("generate", help="Generate a new image from a prompt.")
    generate_parser.add_argument("--prompt", type=str, required=True, help="Text prompt for image generation.")
    generate_parser.add_argument("--output", type=str, default="generated_image.png", help="Output file name for the generated image.")

    # Sub-command for image editing
    edit_parser = subparsers.add_parser("edit", help="Edit an existing image based on a prompt.")
    edit_parser.add_argument("--input", type=str, required=True, help="Path to the input image for editing.")
    edit_parser.add_argument("--prompt", type=str, required=True, help="Text prompt for image editing.")
    edit_parser.add_argument("--output", type=str, default="edited_image.png", help="Output file name for the edited image.")

    args = parser.parse_args()

    do_example()

    #TODO
    #parser.print_help()

if __name__ == "__main__":
    main()


