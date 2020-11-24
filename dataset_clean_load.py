import os
import shutil

PATH = os.getcwd()

# read all images names in one txt.
def read_names(file_name):
    images = []
    f = open(file_name, "r")
    for line in f:
        line = line.strip()
        line = line + '.jpg'
        images.append(line)
    f.close()
    #print('find vaild images : {}'.format(images))
    return images

# for all files to list
def read_files(path):
    all = os.listdir(path)
    clean_files = []
    for i in all:
        name = i.strip('.txt')
        if name[-2:] == 'ok' or name[-4:] == 'good':
            clean_files.append(i)
    
    print('find good and ok txt files: {}'.format(len(clean_files)))
    return clean_files

# make a name dir
def madir():
    clean_path = PATH + '/' + 'landmarks' + '/' + 'paris_clean'
    if not os.path.exists(clean_path):
        os.makedirs(clean_path)
    
# read all images
def read(clean_files):
    images = []
    for i in range(len(clean_files)):
        image = read_names(clean_files[i])
        for y in image:
            images.append(y)
    print('found valid images : {}'.format(len(images)))

    return images

# move images
def move(images):

    for i in range(len(images)):
        #print(images[i])
        move1 = '/home/fathersteph34/data/landmarks/paris6k_images' + '/' + images[i]
        move2 = '/home/fathersteph34/data/landmarks/paris_clean/' + images[i]
        try:
            shutil.copyfile(move1, move2)
        except Exception as e:
            print('Reason:', e)
        
            
# move images for classified repository
def move2(images):
    
# open premission
def change1(path):
    import stat
    os.chmod(path, stat.S_IWRITE)

# close
def change2(path):
    import stat
    os.chmod(path, stat.S_IREAD)


    
def main():

    madir()
    os.chdir('/home/fathersteph34/data/landmarks/paris_120310')
    now_path = os.getcwd()
    clean_files = read_files(now_path)
    images = read(clean_files)
    print(images[0])
    #change1('/home/fathersteph34/data/landmarks/paris6k_images')
    #change2('/home/fathersteph34/data/landmarks/paris6k_images')
    move(images)

main()
 
