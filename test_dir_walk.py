import os  
import sys  
  
def walk_dir(dir, topdown = True):  
    for root, dirs, files in os.walk(dir, topdown):  
        for name in files:  
            print os.path.join(root, name)  
        for name in dirs:  
            print os.path.join(root, name)  
walk_dir(sys.argv[1])  
