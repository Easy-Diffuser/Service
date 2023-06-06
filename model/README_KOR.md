# HOW TO USE EASY-DIFFUSER

![logo](https://github.com/Easy-Diffuser/Service/raw/main/imgs/logo.jfif)

- 생성을 하고 싶은 이미지와 비슷한 Reference 이미지를 사용하여 새로운 이미지 생성에 필요로 하는 알맞은 Postive tag와 Negative tag를 추출합니다.

- 이를 통해 최소한의 시도로 원하는 이미지를 획득할 수 있도록 도움을 주는 소프트웨어입니다.

# Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Support and Feeback](#support-and-feedback)
5. [About Easy Diffuser](#about-easy-diffuser)
6. [Licenses](#licensed)

---

## Features

- run_link: 이미지 링크를 삽입하면 해당 이미지와 관련된 Positive prompt와 Negative prompt를 생성합니다.
- run_image: 이미지 파일을 삽입하면 해당 이미지와 관련된 Positive prompt와 Negative prompt를 생성합니다.
- print_caption: run_link 또는 run_image를 통해 생성된 태그들을 출력합니다.
- send2ui: 생성된 태그들을 WEBUI로 전송합니다. Stable Diffusion이 해당 태그들을 받아 태그와 관련된 이미지를 생성하여 로컬 저장소에 저장합니다.
- input_link: 이미지 링크를 삽입하면 모델이 학습할 수 있는 이미지 형식으로 전처리 해줍니다.
- img2img\_: 선택한 이미지와 비슷한 이미지를 생성합니다.

---

## Installation

1. git clone https://huggingface.co/leeyunjai/img2txt

2. git clone https://github.com/Easy-Diffuser/Model.git

3. Easy-Diffuser/Model 폴더에 있는 Requirements.txt 파일을 사용하여 소프트웨어 버전을 정의합니다.

4. webui-user.bat 파일에 set COMMANDLINE_ARGS=--api 해당 코드를 삽입합니다.

5. 해당 소프트웨어를 사용할 준비가 끝났습니다.

---

## Getting Started

저희 소프트웨어의 기능을 사용하여 다른 제품을 개발을 하고 싶으시면 아래의 설명을 따르시면 됩니다.

1. 사용할 빈 파일을 생성합니다.

2. easy diffuser를 import 해줍니다.

3. easy diffuser에는 start라는 Class가 있습니다. 해당 클래스에는 아래와 같은 메서드들이 있습니다.

| Function      | Function Format             | Description                                                                                          |
| ------------- | --------------------------- | ---------------------------------------------------------------------------------------------------- |
| run_link      | Class_name.run_link(link)   | 이미지 링크를 사용하여 이미지와 관련된 Positive prompt와 Negative prompt tag들을 생성합니다.         |
| run_img       | Class_name.run_img(img)     | 이미지 파일을 사용하여 이미지와 관련된 Positive prompt와 Negative prompt tag들을 생성합니다.         |
| print_caption | Class_name.print_caption()  | run_link 또는 run_image를 통해 생성된 태그들을 출력합니다.                                           |
| input_img     | Class_name.input_img(img)   | local 저장소에 있는 이미지를 클래스 변수에 저장합니다.                                               |
| input_link    | Class_name.input_link(link) | link형식의 이미지를 모델이 학습할 수 있는 이미지 형식으로 전처리 해줍니다.                           |
| send2ui       | Class_name.send2ui()        | 이미지를 통해 얻은 태그들과 stable diffusion 모델을 사용하여 local 저장소에 이미지를 생성합니다.     |
| img2img\_     | Class*name.img2img*(link)   | 선택한 이미지와 비슷한 이미지를 stable diffusion 모델을 사용하여 local 저장소에 이미지를 생성합니다. |

---

## Support and Feedback

Easy Diffuser is implemented by [박찬호](https://github.com/charlieppark), [허찬용](https://github.com/H-ChanY).

If there's any need for support or feedback, feel free to add issues in the corresponding repository.

Or you can freely contact via email:

박찬호 : chanho.park@dankook.ac.kr

허찬용 : chanyong@dankook.ac.kr

---

## About Easy Diffuser

- 크기가 큰 모델이기에 태그를 출력하는 경우 시간이 약 3초 정도 걸립니다.
- 이미지와 관련된 Main keyword 들을 잘 추출합니다.
- Stable Diffusion 모델에 따라 사용자의 취향에 맞는 이미지를 생성해줍니다.
- 개발자를 위해 여러 기능들이 구현이 되어있습니다.
- 기능별로 잘게 나누어져 있어 또 다른 소프트웨어를 만드는 데 용이합니다.

### Easy Diffuser는 아래와 같은 문제 사항들을 해결하기 위해 개발이 되었습니다.

#### 1. diffusion 이미지 생성을 위해 사용자는 많은 시간을 소모해야 한다.

#### 2. 둘째로, 반복된 diffusion 이미지 생성은 많은 컴퓨팅 자원과 전력을 소모한다

#### 3. 이미지 생성 과정의 경험이 사용자 간에 공유되기 어렵다.

해당 문제를 해결하기 위해 저희 Easy Diffuser는 아래와 같은 2가지 기능을 수행합니다.

    1.	Reference 이미지로부터 생성 조건을 추출하는 기능
    사용자는 Reference 이미지를 불러와 추출 기능을 작동시킨다. Easy Diffuser는 입력된 이미지를 OpenAI의 CLIP을 거쳐 텍스트로 변환하고, transformer 기반의 번역기를 사용해 태그 조합으로 번역을 수행한다. 결과물로 도출된 태그 조합은 사용자가 WebUI에서 txt2img의 입력으로 사용할 수 있다.

    2.	Reference 이미지를 입력하여 img2img 생성을 수행하는 기능
    기존의 img2img 생성 기능은 사용자가 이미지를 찾고, 저장하고, 불러오는 등의 단계를 거쳐 동작하거나, txt2img로 생성한 이미지를 불러와 사용할 수 있었다. Easy Diffuser는 웹 페이지의 이미지를 바로 WebUI의 img2img 생성으로 불러올 수 있도록 간편한 메뉴를 지원한다.

---

## Citation

[link] https://github.com/AUTOMATIC1111/stable-diffusion-webui (WEBUI API)

[link] https://huggingface.co/leeyunjai/img2txt (IMG2TXT MODEL)

[link] https://arxiv.org/pdf/2103.00020.pdf (Learning Transferable Visual Models From Natural Language Supervision)

[link] https://arxiv.org/pdf/1706.03762.pdf (Attention is all you need)

---

## Licenses

[link] https://github.com/Easy-Diffuser/Model/blob/main/LICENSE.md
