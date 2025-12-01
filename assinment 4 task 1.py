#task 1 : Read a File and Handle Errors 
import os
file_handler = open('sample.txt','w+')

file_handler.write("This is a sample.txt file .\n")
file_handler.write("It contain multiple line  .\n")
file_handler.seek(0)





if os.path.exists('sample.txt'):
    print("smaple.txt is exist")
    no =1
    for line in file_handler:
        
         print(f"line {no} : {line.strip()}")
         no += 1
    
else:
        print("file does't exist")
file_handler.close()