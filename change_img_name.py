# importing os module 
import os 

path = '/home/newton/Documents/aim/test_30/images/'
  
# Function to rename multiple files 
def main(): 
         
    for filename in os.listdir(path):

        dst =filename[0:6] + ".png"
        src = path + filename 
        dst = path + dst 

        label= filename[8:12]
        if label is 'input':

            os.remove(src)

        else:

            os.rename(src, dst)           
  

if __name__ == '__main__': 
      
     main() 
