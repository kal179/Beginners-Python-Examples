# Writing files

# Enter file name which is in same directory as that of the program
fileName = str(input('File name : ')) 
fileToWrite = open(fileName, 'w') # 'w' writes to the file
textToWrite = str(input('Text to write : '))
fileToWrite.write(textToWrite) # writing file
fileToWrite.close() # closing the file
