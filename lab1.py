personName = input("please enter a name: ")
numDisplay = int(input("Please enter an integer from 0 to 5: "))
for i in range(numDisplay):
	if personName.lower() == 'martin':
		print('Hello Martin!')
	elif personName == 'mary' or personName == 'Mary':
		print('Hi Mary ;)')
	else:
		print('I don\'t know you ' + personName )