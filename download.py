
import os
import zipfile 
import gdown

dicr='weights'
if not os.path.exists(dicr):
  os.makedirs(dicr)

gdown.download('https://drive.google.com/uc?id=1M1LEpx70tJ72AIV2TQKr6NE_7mJ7tLYx', 'weights/rgbadecodernet.pth', quiet=False)
gdown.download('https://drive.google.com/uc?id=1YvZy3NHkJ6gC3pq_j8agcbEJymHCwJy0', 'weights/shader.pth', quiet=False)
gdown.download('https://drive.google.com/uc?id=1AOWZxBvTo9nUf2_9Y7Xe27ZFQuPrnx9i', 'weights/target_pose_encoder.pth', quiet=False)
gdown.download('https://drive.google.com/uc?id=19jM1-GcqgGoE1bjmQycQw_vqD9C5e-Jm', 'weights/udpparsernet.pth', quiet=False)

dicr='short_hair/poses/'
if not os.path.exists(dicr):
  os.makedirs(dicr)
download_path = f'{dicr}/short_hair.zip'
url='https://drive.google.com/uc?id=11HMSaEkN__QiAZSnCuaM6GI143xo62KO'
gdown.download(url, download_path, quiet=False)
with zipfile.ZipFile(download_path, 'r') as ziphandler:
  ziphandler.extractall(dicr)


dicr='double_ponytail/ poses/'
if not os.path.exists(dicr):
  os.makedirs(dicr)
download_path = f'{dicr}/double_ponytail.zip'
url='https://drive.google.com/uc?id=1WNnGVuU0ZLyEn04HzRKzITXqib1wwM4Q'
gdown.download(url, download_path, quiet=False)
with zipfile.ZipFile(download_path, 'r') as ziphandler:
  ziphandler.extractall(dicr)


dicr='poses/'
if not os.path.exists(dicr):
  os.makedirs(dicr)
download_path = f'{dicr}/double_ponytail_images.zip'
url='https://drive.google.com/uc?id=1XMrJf9Lk_dWgXyTJhbEK2LZIXL9G3MWc'
gdown.download(url, download_path, quiet=False)
with zipfile.ZipFile(download_path, 'r') as ziphandler:
  ziphandler.extractall(dicr)

