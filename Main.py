import time #needed for sleep()
import os #needed to delete file

#Files Directory
file = ("C:\\Users\Owner\Desktop\openme.txt")
print ("Opening...", file)
time.sleep(2)

#Settings file to be writtable and openable
#Open & Write
x = open(file,"w")
x.write("Sucessfully wrote") #you can change this to anything you want

#Settings file to be readable and printable
#Read
x = open(file,"r")
print(x.read())
x.close()

#Delete
if os.path.exists("C:\\Users\Owner\Desktop\openme.txt"):
  os.remove("C:\\Users\Owner\Desktop\openme.txt")
else:
  print("The file does not exist")
  
  #create new file
  x = open("C:\\Users\Owner\Desktop\newfile.txt","x")
  
