import pandas as pd
# For copy/pasting the image files
import shutil


# Function that takes the list of images and saves them in their folder
def save_in_folder(class_num, list_of_imgs):

    # Providing the origin folder path to look into
    origin = 'E:/HackerEarth/dataset/dataset/images/'
    
    if (class_num == 0):
        target = 'E:/HackerEarth/Train Img/0_GRAFFITI/'
    elif (class_num == 1):
        target = 'E:/HackerEarth/Train Img/1_FADED_SIGNAGE/'
    elif (class_num == 2):
        target = 'E:/HackerEarth/Train Img/2_POTHOLES/'
    elif (class_num == 3):
        target = 'E:/HackerEarth/Train Img/3_GARBAGE/'
    elif (class_num == 4):
        target = 'E:/HackerEarth/Train Img/4_CONSTRUCTION_ROAD/'
    elif (class_num == 5):
        target = 'E:/HackerEarth/Train Img/5_BROKEN_SIGNAGE/'
    elif (class_num == 6):
        target = 'E:/HackerEarth/Train Img/6_BAD_STREETLIGHT/'
    elif (class_num == 7):
        target = 'E:/HackerEarth/Train Img/7_BAD_BILLBOARD/'
    elif (class_num == 8):
        target = 'E:/HackerEarth/Train Img/8_SAND_ON_ROAD/'
    elif (class_num == 9):
        target = 'E:/HackerEarth/Train Img/9_CLUTTER_SIDEWALK/'
    elif (class_num == 10):
        target = 'E:/HackerEarth/Train Img/10_UNKEPT_FACADE/'
    

    # Fetching all the files to directory
    for img_name in list_of_imgs:
        #shutil.copy(origin+img_name, target+img_name)
        shutil.copy(origin+img_name, target+img_name)
    print("Files are copied successfully")




"""
Column Name	    Meaning
------------------------------------------------
class	        Class code of the pollution type
image_path	    The name of the .jpg image
name	        Name of visual pollution type
xmax	        Xmax coordinate of bounding box
xmin	        Xmin coordinate of bounding box
ymax	        Ymax coordinate of bounding box
ymin	        Ymin coordinate of bounding box

"""
df = pd.read_csv(r'E:\HackerEarth\dataset\dataset\train.csv')
#print(df['image_path'])

# Get the list of images per class
for i in range(0,11):
    imgs = []
    for index, row in df.iterrows():
        if int((row['class'])) == i:
            imgs.append(row['image_path'])
    print(i, len(imgs))
    save_in_folder(i, imgs)

