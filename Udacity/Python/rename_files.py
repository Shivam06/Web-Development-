import os
import re
file_list = os.listdir(r"C:\Users\SHIVAM MAHAJAN\Desktop\prank")
print file_list
path = "C:\Users\SHIVAM MAHAJAN\Desktop\prank"
for f in file_list:
    a = re.findall("^[0-9]+(.*)",f)
    if len(a) > 0:
        os.rename(path + '\\' + f, path + '\\' + a[0])
