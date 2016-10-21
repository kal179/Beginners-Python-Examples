# Reading files

# Enter file name which is in same directory as that of the program
fileName = str(input('File name : ')) 
fileToRead = open(fileName, 'r') # 'r' reads the file
print(fileToRead.read()) # reading file
fileToRead.close() # closing the file
