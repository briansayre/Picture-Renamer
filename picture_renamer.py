import os
os.chdir("/Users/user/Pictures") #directory of pictures
amount = 0
for filename in os.listdir():
    file_name, file_ext = os.path.splitext(filename)
    if file_ext == ".JPG":
        if amount < 10:
            amount = "0"+str(amount)
        new_name = "Image_"+str(amount)+file_ext
        os.rename(filename, new_name)
        amount = int(amount)
        amount += 1
