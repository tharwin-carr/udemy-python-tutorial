'''
Reading and Writing to a .txt file
'''

with open('text.txt', 'r') as read_file:
    with open('text2.txt', 'w') as write_file:
        write_file.write(read_file.read())


# with open('text2.txt', 'w') as f:
#     f.write('This is a new file and some text')
#if the file exists it will overwrite the file
#if the files does not exist, it will create a new file