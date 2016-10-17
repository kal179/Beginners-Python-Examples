# quadrant determiner
# I(+,+) II(-,+) III(-,-) IV(+,-)

x = float(input('X co-ordinate : '))
y = float(input('Y co-ordinate : '))

if x > 0 and y > 0:
	print('I(+,+)')
elif x < 0 and y > 0:
	print('II(-,+)')
elif x < 0 and y < 0 :
	print('III(-,-)')
elif x > 0 and y < 0 :
	print('IV(+,-)')
else :
	print('Oops Unable to deternine quadrant')				