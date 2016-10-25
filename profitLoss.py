# Profit Loss Calculator

def profit(sellP , costP):
    profit = sellP - costP
    return(profit)  # Function for calculating profit

def loss(costP , sellP):
    loss = costP - sellP
    return(loss)    # Function for calculating loss

def profitPercent(prof , costP):
    profitPerc = prof / costP * 100
    return(str(profitPerc) + '%') # func to calculate profit percent

def lossPercent(loss , costP):
    lossPerc = loss / costP * 100
    return(str(lossPerc) + '%') # Func to calculate loss percent

print('Hello\n')
print('Press Enter To Exit')
while(True):
    google = str(input('Profit or Loss : '))
    if google.strip() == 'Profit': # condition for profit
        sellPrice = float(input('Selling Price : ')) # getting selling price
        costPrice = float(input('Cost Price : ')) # getting costprice
        if sellPrice > costPrice:   # if selling price is greater than cp
            print('Profit : ' + str(profit(sellPrice , costPrice)))
            print('Profit Percent : ' + str(profitPercent(profit(sellPrice , costPrice) , costPrice)))
            continue
        else: # else if sp is less than cp so it is loss
            print('Cost Price is Greater Than Selling Price')
            print('Try calculating loss\n')
            continue
    elif google.strip() == 'Loss':
        costPrice = float(input('Cost Price : '))
        sellPrice = float(input('Selling Price : '))
        if costPrice > sellPrice:
            print('Loss : ' + str(loss(costPrice , sellPrice)))
            print('Loss Percent : ' + str(lossPercent(loss(costPrice , sellPrice) , costPrice)))
            continue
        else:
            print('Selling Price is Greater Than Cost Price')
            print('Try calculating profit\n')
            continue
    else:
        quit()
