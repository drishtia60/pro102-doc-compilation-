import os
import shutil

from_dir = "C:/Users/Asus/Downloads"
to_dir = "C:/Users/Asus/Downloads/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        #C:/Users/Asus/Downloads/New_Folder
        path1 = from_dir+'/'+file_name
        #C:/Users/Asus/Downloads/Document_Files
        path2 = from_dir+'/'+ "Document_Files"
        #C:/Users/Asus/Downloads/Document_Files/New_Folder
        path3 = to_dir+'/'+file_name

        if os.path.exists(path2):
            print('Moving'+file_name+'.....')

            shutil.move(path1,path3)
        
        else: 
            os.makedirs(path2)
            print('Moving'+file_name+'.....')

            shutil.move(path1,path3)
