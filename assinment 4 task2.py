file = open('output.txt','a+')
first_data = input("Enter text to wirte in the file :"+"\n")
file.write(first_data +"\n"*2)
print("Data successfully writen in output.txt.\n")
file.seek(0)

#file.read()
for line in file:
    print(line.strip(),"\n")
while True:
    print(" If you want add additional data to file select option.\n")
    print("option : 1  (for add text in file )\n  option : 2 (for exit from file)")
    a = int(input())
    if a == 1:
       data_append= input("Enter data to add in output.txt :  "+"\n")
       file.write(data_append +"\n"*2)
       file.seek(0)
       print("data successfully appended")
    else:
        file.seek(0)
        print("final content of output.txt\n")
        for line in file:
            print(line.strip())

        break

file.close()