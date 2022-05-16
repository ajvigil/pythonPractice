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