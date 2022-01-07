colors = {'red', 'blue', 'green', 'pink', 'purple'}

#Prints the length of colors
print(len(colors))

# Removes green from the colors set
colors.remove('green')

# Adds black and white to the colors set
colors.update(['black', 'white'])

print(colors)

numbers = {1, 2, 3}

# Combines the colors set and numbers set together
set_three = colors.union(numbers)

print(set_three)