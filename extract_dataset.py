import zipfile
import os

# Path to the dataset ZIP file
local_zip = r"C:\Users\forsi\Desktop\FaceLivenessDetection\Dataset 59 Images.zip"

# Extract the dataset
with zipfile.ZipFile(local_zip, 'r') as zip_ref:
    zip_ref.extractall("Dataset")

print("Dataset extracted successfully!")
print(os.listdir("Dataset"))
