import os  
import sys  
  
def walk_dir(dir, topdown = True):  
    for root, dirs, files in os.walk(dir, topdown):  
        for name in files:  
            print root
            # print os.path.join(root, name)  
        for name in dirs:  
            print root
            # print os.path.join(root, name)  
            print "####"
walk_dir(sys.argv[1])  
