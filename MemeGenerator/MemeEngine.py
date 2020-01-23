from PIL import Image,ImageDraw,ImageFont
import random
import os
import requests
from io import BytesIO


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        try:
            os.mkdir(output_dir)
        except:
            pass
        
    def make_meme(self, img_path, text, author, width=500) -> str:
        
        if 'http' in img_path:
            response = requests.get(img_path)
            im = Image.open(BytesIO(response.content))
        else:
            im = Image.open(img_path)

        changed_w = (width / float(im.size[0]))
        height = int((float(im.size[1] * float(changed_w))))
        resized = im.resize((width,height),Image.ANTIALIAS)

        scolor = 'white'
        fcolor = 'black'

        f = ImageFont.truetype("arial.ttf", 25)

        d = ImageDraw.Draw(resized)

        x, y = random.randint(10,200), random.randint(10,200)

        d.text((x,y),text,fill= fcolor,font=f)
        d.text((x,y+25),'-'+author,fill= fcolor,font=f)

        file =  str(random.randint(0,200000))

        final = self.output_dir+'/'+file + ".jpg"

        resized.save(final, "JPEG")

        xyz = str(os.getcwd())
        
        p = xyz.split('\\')

        pqr = p

        return '/'.join(pqr)+'/'+self.output_dir[2:]+'/'+file+'.jpg'

        

        
        
