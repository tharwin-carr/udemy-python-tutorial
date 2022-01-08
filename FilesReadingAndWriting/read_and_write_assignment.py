with open('new_text_file.txt', 'w') as assignment_file:
    assignment_file.write('this is a new text file')

with open('new_text_file.txt', 'r') as assignment_file2:
    print(assignment_file2.read())
