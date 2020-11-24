import os
from PIL import Image

root = os.getcwd()
for folders in os.listdir(root):
    os.chdir(root+'/'+folders)
    for filenames in os.listdir():
        if filenames.endswith('.jpg'):
            try:
                img = Image.open(root+'/'+folders+'/'+filenames)
                img.verify()
            except(IOError,SyntaxError)as e:
                print('Bad file  :  '+filenames)
                os.remove(root+'/'+folders+'/'+filenames)
