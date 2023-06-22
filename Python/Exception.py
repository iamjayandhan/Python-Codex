from time import sleep
try:
    fh=open("Sample.txt","w")
    fh.write("Hello world")
except IOError:
    print("Hey! Error found")
else:
    sleep(2.0)
    print("Content written successfully!")
    fh.close()