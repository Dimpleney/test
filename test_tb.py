from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image


writer = SummaryWriter("logs")
# image_path = "dataset/train/ants/0013035.jpg"
image_path = "dataset/train/bees/16838648_415acd9e3f.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)
writer.add_image("test",img_array,2,dataformats='HWC')

#  y = x
for i in range(100):
    writer.add_scalar("y=2x",i*2,i)
# writer.add_scalar()
writer.close()