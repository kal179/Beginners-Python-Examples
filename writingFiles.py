# Writing files

# Enter file name which is in same directory as that of the program
fileName = str(input('File name : ')) 
fileToWrite = open(fileName, 'w') # 'w' writes to the file
textToWrite = str(input('Text to write : '))
fileToWrite.write(textToWrite) # writing file
fileToWrite.close() # closing the file

# In the above example you have invoke closure on the file descriptor, fileToWrite 
# If some error occurs the file descriptors are not closed and this may cause problems
# One can use context manager with ... as to avoid this (>python 2.5)
# close function is not required as it automatically closes the file once the context is over
# Same as a try ... except ... finally block

textToWrite = str(input('Text to write : '))
fileName = str(input('File name : ')) 
with open(fileName,'w') as fileToWrite:
  fileToWrite.write(textToWrite) 
