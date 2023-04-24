# write a program where all the input string show in a one line.(like as: Apple, orange)

fruits= ['Apple', 'Orange', 'Mango', 'Peace', 'Pomegranate', 'Pineapple', 'Rambutan']
for fruit in fruits:
    print(fruit)

# The above program shows the output as :
# Apple
# Orange
# Mango
# Peace
# Pomegranate
# Pineapple
# Rambutan
print("Correct results= \n")

fruits= ['Apple', 'Orange', 'Mango', 'Peace', 'Pomegranate', 'Pineapple', 'Rambutan']
for fruit in fruits:
    print(fruit, end=' ')
print("\n")
for i in range(8):
    print(i)