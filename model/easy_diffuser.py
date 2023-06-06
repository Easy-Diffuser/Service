import time
import model_ as m
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import urllib.request
import base64
from io import BytesIO
from urllib import request
import uuid

class start():
  def __init__(self,link=None,img=None) :
    self.model = m.Model()
    self.img=img
    self.link=link
    if link !=None:
      self.link=self.input_link(link)
    self.pos=None
    self.neg=None
    
  def run_link(self,link):
    self.input_link(link)
    if self.link!=None:
      self.pos,self.neg = self.model.predict(self.link)
      #self.print_caption()
      
  
  def run_img(self,img):
    self.img=img
    self.pos,self.neg = self.model.predict(self.img)
    
      
  def print_caption(self):
    print(self.pos, self.neg)
  
  def input_img(self,img):
    self.img=img
  
  def input_link(self,link):
    req = urllib.request.Request(link, headers = {"User-Agent" : "Mozilla/5.0"})
    res = urllib.request.urlopen(req).read()
    self.link = Image.open(BytesIO(res))
    
  
  def send2ui(self):
      
    url = "http://127.0.0.1:7860"
    
    payload = {
      "prompt": "{}".format(self.pos),
      "neg_prompt":"{}".format(self.neg),
      "steps": 50  
    }
      
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    image = Image.open(io.BytesIO(base64.b64decode(str(r['images']).split(",",1)[0])))
    image.save('output.png')
  
  def img2img_(self,link):
    url = "http://127.0.0.1:7860"
    img_url=link
    file_name=str(uuid.uuid4()) 
    res = request.urlopen(link).read()

    img = Image.open(BytesIO(res))
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_base64=base64.b64encode(img_bytes.getvalue()).decode('utf-8')

    payload = {
        "init_images":[img_base64],
      "prompt": "{}".format(self.pos),
      "neg_prompt":"{}".format(self.neg),
      "steps": 50  
    }

    response = requests.post(url=f'{url}/sdapi/v1/img2img', json=payload)

    r = response.json()
    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save('../chrome-extension/local/output/output.png', pnginfo=pnginfo)