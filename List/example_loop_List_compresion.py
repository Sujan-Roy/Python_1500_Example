# meals=['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam']
# Given a list of meals served over some period of time, return True if the
    #  same meal has ever been served two days in a row, and False otherwise.
#meals=['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam']
def meal_is_boring(meals):
    for n in range(len(meals)-1):
        if meals[n] == meals[n+1]:
            return True
    return False

input1= meal_is_boring(['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam'])
print(input1)
input2= meal_is_boring(['Spam', 'Eggs', 'Rice', 'Spam', 'Bacon', 'Spam'])
print(input2)

