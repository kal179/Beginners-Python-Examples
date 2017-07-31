# Tested in python2.7
# Getting Html text and saving it to a file.
import urllib

def get_html(url , fname):
    try:
        responsive = urllib.urlopen(url)
        save_file = open(fname + '.html' , 'w')
        save_file.write(responsive.read())
        save_file.close()
    except IOError:
        return "Make sure url entered is correct and valid!"
    except Exception as e:
        return "An Error occured, make sure information enerted is correct!"
    else:
        return "Html Successfully received and saved in file {}.html".format(fname)
    # if you want to read the file uncomment this code
    # emp = open(name + ".html", 'r').read()
    # openFile.close()
    # return emp

print('Hello,')
while(True):
    start_or_end = str(raw_input('start or end: ')).strip().lower()
    if start_or_end == 'start':
        print(get_html(raw_input('URL: ').strip() , raw_input('file name: ').strip()), "\n")
        continue
    quit()
