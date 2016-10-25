# Percantage Increase , Percentage Decrease

def increasePercent(increase , origValue):
    iPercent = increase / origValue * 100
    return(str(iPercent) + '%')

def decreasePercent(decrease , origValue):
    dPercent = decrease / origValue * 100
    return(str(dPercent) + '%')

print('Hello\n')
print('Press Enter To Exit ')
incOrDec = str(input('Increase or Decrease : '))
if incOrDec == 'Increase':
    getInc = float(input('Increased Value : '))
    orignal = float(input('Orignal Value : '))
    print(increasePercent(getInc , orignal))
elif incOrDec == 'Decrease':
    getDec = float(input('Increased Value : '))
    orignal = float(input('Orignal Value : '))
    print(increasePercent(getDec , orignal))
else:
    quit()
