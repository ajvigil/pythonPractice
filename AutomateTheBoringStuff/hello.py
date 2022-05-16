# This program says hello and asks for your name 

print('Hello World!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


## If, Else and Elif Statements 

name = 'James'
if name == 'James':
    print('Hi James')
print('Done')

# another example

password = 'swordfish'
if password == 'swordfish':
    print('Access Granted')
else:
    print('Wrong Password')

# another 

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12: 
    print('You are not ALice, kiddo.')
elif age > 2000: 
    print('Unlike you, Alice is not an undead, imortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

# while loops

spam = 0 
while spam < 5:
    print('Hello World!')
    spam = spam + 1

# example 2

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# example 3, continue statements 

spam = 0 
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

# for loops 

print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

# example 2

total = 0
for num in range(101):
    total = total + num
print(total)

