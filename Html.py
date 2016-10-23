# Getting Html code and parsing it.
import urllib.request

# Function to get the code
def htmlCode(link , name):
    responsive = urllib.request.urlopen(link) # opening link
    receivedHtml = responsive.read() # reading code
    filename = name + '.html' # naming the file
    saveInFile = open(filename , 'w')
    saveInFile.write(str(receivedHtml))
    saveInFile.close()
    # if you want to read the file uncomment this code
    # openFile = open(name, 'r')
    # print(openFile.read())
    # openFile.close()

print('Hello,\n')
# Main code
while(True):
    startOrEnd = str(input('Start or End : '))
    if startOrEnd == 'Start':
        getLink = str(input('Link of Website : '))
        fileNameToSave = str(input('File name : '))
        print(htmlCode(getLink , fileNameToSave))
        continue
    else:
        quit()
