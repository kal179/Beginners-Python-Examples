def percToDiscount(percent , mp):
    discount = percent / 100 * mp
    return('Discount is : ' + str(discount))

print('Hello\n')
print('Press Enter to exit')
while(True):  # I've put counting discount in a loop cause if you want to count on multiple items
    more = str(input('Count or End : '))
    if more == 'Count':
        disCountPerc = float(input('Discount Percent : '))
        marketPrice = float(input('Market Price : '))
        print(percToDiscount(disCountPerc , marketPrice))
        continue
    else:
        quit()
