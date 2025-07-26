filename = "sample.txt"
try:
    with open(filename,'r') as file1:
        print(file1.read())
except FileNotFoundError:
    print("The file ", filename, " was not found")