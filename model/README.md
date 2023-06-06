# HOW TO USE EASY-DIFFUSER

![logo](https://github.com/Easy-Diffuser/Service/raw/main/imgs/logo.jfif)

[README_KOR](https://github.com/Easy-Diffuser/Model/blob/main/README_KOR.md)

Easy Diffuser is a software that helps generate new images by extracting appropriate positive and negative tags required for image generation using a reference image similar to the image you want to create. It assists in obtaining the desired image with minimal effort.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Support and Feedback](#support-and-feedback)
5. [About Easy Diffuser](#about-easy-diffuser)
6. [Licenses](#licenses)

---

## Features

- `run_link`: Generates positive and negative prompts related to the input image link.
- `run_image`: Generates positive and negative prompts related to the input image file.
- `print_caption`: Prints the generated tags from `run_link` or `run_image`.
- `send2ui`: Sends the generated tags to the WEBUI. Stable Diffusion uses these tags to generate images related to the tags and saves them in the local repository.
- `input_link`: Preprocesses the image link into a format that the model can learn.
- `img2img_`: Generates similar images to the selected image.

---

## Installation

1. Clone the repository: `git clone https://huggingface.co/leeyunjai/img2txt`
2. Clone the Easy Diffuser model: `git clone https://github.com/Easy-Diffuser/Model.git`
3. Define the software version using the `Requirements.txt` file in the `Easy-Diffuser/Model` folder.
4. Insert the following code into the `webui-user.bat` file: `set COMMANDLINE_ARGS=--api`
5. The installation is now complete.

---

## Getting Started

To develop other products using the features of our software, follow these steps:

1. Create an empty file to work with.
2. Import Easy Diffuser into your project.
3. The Easy Diffuser package includes a class called `start`, which provides the following methods:

| Function        | Function Format               | Description                                                                                                             |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `run_link`      | `Class_name.run_link(link)`   | Generates positive and negative prompt tags related to the image using the image link.                                  |
| `run_img`       | `Class_name.run_img(img)`     | Generates positive and negative prompt tags related to the image using the image file.                                  |
| `print_caption` | `Class_name.print_caption()`  | Prints the generated tags from `run_link` or `run_image`.                                                               |
| `input_img`     | `Class_name.input_img(img)`   | Saves the image from the local repository in the class variable.                                                        |
| `input_link`    | `Class_name.input_link(link)` | Preprocesses the link-formatted image into a format that the model can learn.                                           |
| `send2ui`       | `Class_name.send2ui()`        | Generates images based on the obtained tags and the stable diffusion model and saves them in the local repository.      |
| `img2img_`      | `Class_name.img2img_(link)`   | Generates similar images to the selected image using the stable diffusion model and saves them in the local repository. |

---

## Support and Feedback

Easy Diffuser is implemented by [박찬호](https://github.com/charlieppark), [허찬용](https://github.com/H-ChanY).

If there's any need for support or feedback, feel free to add issues in the corresponding repository.

Or you can freely contact via email:

박찬호 : chanho.park@dankook.ac.kr

허찬용 : chanyong@dankook.ac.kr

---

## About Easy Diffuser

- Outputting tags may take approximately 3 seconds due to the large model size.
- The software accurately extracts main keywords related to the image.
- It generates images according to the user's preferences based on the Stable Diffusion model.
- Various features have been implemented for developers.
- The software is divided into fine-grained functions, making it easy to create other software.

### Easy Diffuser was developed to address the following issues:

1. Users spend a lot of time generating diffusion images.
2. Repeated generation of diffusion images consumes a lot of computing resources and power.
3. It is difficult to share the experience of the image generation process among users.

### To solve these problems, Easy Diffuser provides the following two functions:

1. Extraction of generation conditions from a reference image:

   - Users can load a reference image and extract generation conditions. Easy Diffuser converts the input image into text using OpenAI's CLIP and translates it into tag combinations using a transformer-based translator. The resulting tag combinations can be used as inputs for `txt2img` in the WebUI.

2. Image-to-image generation using a reference image:
   - The existing image-to-image generation functionality requires users to go through steps such as finding, saving, and loading images, or using images generated with `txt2img`. Easy Diffuser provides a convenient menu to directly load images from web pages into the WebUI's `img2img` generation.

---

## Citation

- WEBUI API: https://github.com/AUTOMATIC1111/stable-diffusion-webui
- IMG2TXT MODEL: https://huggingface.co/leeyunjai/img2txt
- Learning Transferable Visual Models From Natural Language Supervision: https://arxiv.org/pdf/2103.00020.pdf
- Attention is All You Need: https://arxiv.org/pdf/1706.03762.pdf

---

## Licenses

- [License](https://github.com/Easy-Diffuser/Model/blob/main/LICENSE.md)
