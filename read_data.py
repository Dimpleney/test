# 1.Dataset:提供一种方式获取数据机器label
# 1.1 如何获取一个数据及其lable
# 1.2
# Dataloader

from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):
    def __int__(self,root_dir,lable_dir):
        self.root_dir = root_dir
        self.lable_dir = lable_dir
        self.path = os.path.join(self.root_dir,self.lable_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir,self.lable_dir,img_name)
        img = Image.open(img_item_path)
        lable = self.lable_dir
        return img,lable

    def __len__(self):
        return len(self.img_path)

root_dir = "dataset/train"
ants_lable_dir = "ants"
bees_lable_dir = "bees"
ants_dataset = MyData(root_dir,ants_lable_dir)
bees_dataset = MyData(root_dir,bees_lable_dir)
img,lable = ants_dataset[1]
img.show()