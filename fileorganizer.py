import os
import glob
import shutil

doc_ext = ('.pdf', '.txt', '.doc', '.docx', '.xls', '.xlsx')
img_ext = ('.jpg', '.gif', '.png', '.jpeg')
vid_ext = ('.mp4', '.webm', '.avi', '.flv')

wdir = r'D:/Downloads/'
mig_dir_name = ["Docs", "Images", "Video", "Misc"] 
doc_list = []
image_list = []
vid_list = []
other_list = []

os.chdir(os.path.expanduser(wdir))
current_dir = os.getcwd()

def moveFile(src, dst):
    if (os.path.isfile(src)):
        print("Moving file:",src)
        shutil.copy2(src, dst)
        os.remove(src)

for d in mig_dir_name:
    mig_dir = os.path.join(current_dir, d)
    if (not os.path.isdir(mig_dir)): 
        print("[DEBUG] Directory {0} doesn't exist: ".format(mig_dir))
        print("[DEBUG] Making path:",mig_dir)
        os.mkdir(mig_dir, 0o775)

print("Cleaning up in:",current_dir)

for f in (glob.glob('*.*')):
   if (f.endswith(doc_ext)):
        try:
          moveFile(f, os.path.join(os.getcwd(), mig_dir_name[0]))
        except:
          print("[-] Unable to move file at this time")
          pass
   if (f.endswith(img_ext)):
        try:
          moveFile(f, os.path.join(os.getcwd(), mig_dir_name[1]))
        except:
          print("[-] Unable to move file at this time")
          pass
   if (f.endswith(vid_ext)):
        try:
          moveFile(f, os.path.join(os.getcwd(), mig_dir_name[2]))
        except:
          print("[-] Unable to move file at this time")
          pass
   else:
        try:
          moveFile(f, os.path.join(os.getcwd(), mig_dir_name[3])) 
        except:
          print("[-] Unable to move file at this time")
          pass
 
