# don't forget to add a sqlite3 db support
# and also add password encryption and decryption support

# Universal dict for saving passwords
passwords = {}

def addPassword():
    getMoreSite = str(input('Name of Website : '))
    getMorePassword = str(input('Password : '))
    passwords[getMoreSite] = getMorePassword

def showPassword():
    getName = str(input('Name of Website : '))
    try:
        return(getName + ' : ' +  str(passwords[getName]))
    except KeyError:
        print('Password not saved')

def deletePassword():
    toDelete = str(input('Website of Password to delete : '))
    try:
        del passwords[toDelete]
        return('Deleted Successfully.')
    except KeyError:
        print('Invalid site to delete')

def showAll():
    return(passwords)

def showWebsites():
    keys = str(passwords.keys())
    return(keys[9:])

def mainCode(add , view , remove , allwords , allSites):
    while(True):
        start = str(input('Add or View or Delete or Show all or Show sites : '))
        if start.strip() == 'Add':
            print(add())
            continue
        elif start.strip() == 'View':
            print(view())
            continue
        elif start.strip() == 'Delete':
            print(remove())
            continue
        elif start.strip() == 'Show all':
            print(allwords())
            continue
        elif start.strip() == 'Show sites':
            print(allSites())
            continue
        else:
            quit()


# Main code
# Login function
login = str(input('Username : '))
loginPassword = str(input('Password : '))
if login == 'Kalpak' and loginPassword == 'thisisapassword':  # replace with your username or password
    print(mainCode(addPassword , showPassword , deletePassword , showAll , showWebsites))
else :
    quit()
