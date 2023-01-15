import pandas as pd
# For copy/pasting the image files
import shutil


# Function that takes the list of images and saves them in their folder
def save_in_folder(list_of_imgs):

    # Providing the origin folder path to look into
    origin = 'E:/HackerEarth/dataset/dataset/images/'
    target = 'E:/HackerEarth/Test Img/'
    
    # Fetching all the files to directory
    for img_name in list_of_imgs:
        #shutil.copy(origin+img_name, target+img_name)
        shutil.copy(origin+img_name, target+img_name)
    print("Files are copied successfully")




"""
Column Name	    Meaning
------------------------------------------------
image_path	    The name of the .jpg image

"""
df = pd.read_csv(r'E:\HackerEarth\dataset\dataset\test.csv')

# Get the list of images
imgs = []
for index, row in df.iterrows():
    imgs.append(row['image_path'])
print(len(imgs))
save_in_folder(imgs)