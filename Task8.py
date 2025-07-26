filename = "output.txt"

with open(filename,'w') as file1:
    content=input("Enter text to write to the file: ")
    file1.write(content)
    print("Data successfully written to output.txt")

with open(filename,'a') as file1:
    content=input("Enter additional text to append: ")
    file1.write(content)
    print("Data sucessfully appended")

with open(filename,'r') as file1:
    print("Final content of output.txt")
    print(file1.read())
