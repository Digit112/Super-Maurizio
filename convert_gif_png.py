from PIL import Image
import sys
import os

j = 1

for i in os.listdir('assets/img/'):
    if '.gif' in i:
        with Image.open('assets/img/'+i) as im:
            info = im.info

            for k in range(im.n_frames):
                im.seek(k)
                im.save(f"assets/img/frames/{i}_frame{k}.png", **info)

        j += 1