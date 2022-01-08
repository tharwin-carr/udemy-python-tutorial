'''
Reading and Writing to a .txt file
'''

#Context Managers will open and close automatically

#Prints the lines of the .txt file
with open('text.txt', 'r') as f:
    print(f.read())
    # for line in f:
    #     print(line, end='')