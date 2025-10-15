print('some python code!!!')
print('I commit, I push, and most importantly.. I pull!!!')

input1 = float(input('Enter first number: '))
input2 = float(input('Enter second number: '))

print('Select operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

operation = input('Enter operation (1/2/3/4): ')

if operation == '1':
    print('Result:', input1 + input2)
elif operation == '2':
    print('Result:', input1 - input2)
elif operation == '3':
    print('Result:', input1 * input2)
elif operation == '4':
    if input2 != 0:
        print('Result:', input1 / input2)
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid operation selected.')