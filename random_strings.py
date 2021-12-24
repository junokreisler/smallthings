import random, string

len = int(input('Enter the length of the string: '))
again = True
ideas = [] # the names will be stored here, each idea as a separate string in the list

print()
print('Now this program will start giving you strings of length', len)
print('To print another string, press Enter. If you get an idea for a name, press s and register it.')
print('To change string length, press l.')
print('All ideas from each iteration will be saved in nameideas.txt')
proceed = input('Press any key to continue... ')

while again == True:
    # printing a string of chosen length with random lowercase letters
    print(''.join(random.choice(string.ascii_lowercase) for i in range(len)))
    ans = input('Enter/s/l : ')
    if ans == 'l':
        len = int(input('Enter new length: '))
    if ans == 's':
        idea = input('Name idea: ')
        ideas.append(idea)
    if ans != '' and ans != 's' and ans != 'l':
        again = False

print('Name ideas from this iteration:')
print(i for i in ideas)

# appending to the file; will be created if it doesn't exist
with open('nameideas.txt', 'a') as f:
    for i in ideas:
        f.write(i + ' ')
    f.write('\n')

print('File saved.')

