import PIL
import os
from PIL import Image
import time
import argparse
parser = argparse.ArgumentParser(description='Resize Images')
parser.add_argument('path', type=str, default='data/traffic_signs/40mph', help='Path ex:data/traffic_signs/40mph')
start_time = time.time()
args = parser.parse_args()
f = args.path
dirt = os.listdir(f)
for file in dirt:
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((256,256))
    img.save(f_img)
    print(file)
end_time = time.time()
print(f"Took {end_time-start_time} seconds")
time.sleep(2)

