import torch
import caption_model
from transformers import BertTokenizer
import torchvision
from PIL import Image
from configuration import Config
import numpy as np
import matplotlib.pyplot as plt

def under_max(image):
  if image.mode != 'RGB':
    image = image.convert("RGB")

  shape = np.array(image.size, dtype=np.float)
  long_dim = max(shape)
  scale = 299 / long_dim

  new_shape = (shape * scale).astype(int)
  image = image.resize(new_shape)

  return image

class Model(object):
  def __init__(self, gpu=None):
    config = Config()
    config.device = 'cpu' if gpu is None else 'cuda:{}'.format(gpu)
    model, _ = caption_model.build_model(config)   
    checkpoint = torch.load('./checkpoint.pth', map_location='cpu')
    model.load_state_dict(checkpoint['model'])
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    start_token = tokenizer.convert_tokens_to_ids(tokenizer._cls_token)
    end_token = tokenizer.convert_tokens_to_ids(tokenizer._sep_token)

    self.caption = torch.zeros((1, config.max_position_embeddings), dtype=torch.long).to(config.device)
    self.cap_mask = torch.ones((1, config.max_position_embeddings), dtype=torch.bool).to(config.device)
    self.caption_n = torch.zeros((1, config.max_position_embeddings), dtype=torch.long).to(config.device)
    self.cap_mask_n = torch.ones((1, config.max_position_embeddings), dtype=torch.bool).to(config.device)

    self.caption[:, 0] = start_token
    self.cap_mask[:, 0] = False
    self.caption_n[:, 0] = start_token
    self.cap_mask_n[:, 0] = False
    
    self.val_transform = torchvision.transforms.Compose([
      torchvision.transforms.Lambda(under_max),
      torchvision.transforms.ToTensor(),
      torchvision.transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    model.to(config.device)
    self.model = model
    self.config = config
    self.tokenizer = tokenizer
  

  def evaluate(self, im):
    self.model.eval()
    for i in range(self.config.max_position_embeddings - 1):
      predictions = self.model(im.to(self.config.device), self.caption.to(self.config.device), self.cap_mask.to(self.config.device))
      predictions = predictions[:, i, :]
      predicted_id = torch.argmax(predictions, axis=-1).to(self.config.device)
      
      predictions_neg=torch.where(predictions>-90,predictions,1)
      predicted_id_n=torch.argmin(predictions_neg, axis=-1).to(self.config.device)
      
      
      """a=predictions.detach().numpy()
      l=[i for i in range(len(predictions[0]))]
      plt.scatter(l,a)
      plt.show()
      print(predictions[0][predicted_id],predictions[0][predicted_id_n])"""
      if predicted_id[0] == 102:
        return self.caption, self.caption_n

      self.caption[:, i+1] = predicted_id[0]
      self.cap_mask[:, i+1] = False
      self.caption_n[:, i+1] = predicted_id_n[0]
      self.cap_mask_n[:, i+1] = False
    return self.caption, self.caption_n

  
  def predict(self, image_path):
    try:
      image = Image.open(image_path)
      image = self.val_transform(image)
    except:
      image = self.val_transform(image_path)
    image = image.unsqueeze(0)
    pos_output,neg_output = self.evaluate(image)
    return self.tokenizer.decode(pos_output[0].tolist(), skip_special_tokens=True),self.tokenizer.decode(neg_output[0].tolist(), skip_special_tokens=True)

