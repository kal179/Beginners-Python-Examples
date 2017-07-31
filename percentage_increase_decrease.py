# Percantage Increase , Percentage Decrease

def increasePercent(increase , origValue):
    return(str(increase / origValue * 100) + '%')

def decreasePercent(decrease , origValue):
    return(str(decrease / origValue * 100) + '%')

print('Hello,\nPress Enter To Exit')
incOrDec = str(input('increase or decrease: ')).strip().lower()
if incOrDec == 'increase':
    print(increasePercent(float(input('Increased Value : ')) ,  float(input('Orignal Value : '))))
elif incOrDec == 'decrease':
    print(increasePercent(float(input('Increased Value : ')), float(input('Orignal Value : '))))
else:
    quit()
