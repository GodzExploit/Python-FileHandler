import time

#Files Directory
file = ("C:\\Users\Owner\Desktop\openme.txt")
print ("Opening...", file)
time.sleep(2)

#Settings file to be writtable and openable
x = open(file,"w")
x.write("Sucessfully wrote") #you can change this to anything you want

#Settings file to be readable and printable
x = open(file,"r")
print(x.read())
x.close()
