# int() = converting string to integer
# float() =      "     "     " float or a number with decimal point.
# bool() =       "     "     into a boolean value.
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2025 - int(birth_year) #This is how to convert the string into integer.
# print(type(age))
# print(age)

#Exercise

weight_into_pounds = input('What is your weight into pound? ')
print(type(weight_into_pounds))
weight_into_kgs = int(weight_into_pounds) * 0.45  #convertion of pounds to kilograms
print(type(weight_into_kgs))
print(weight_into_kgs)
print(f'Hi your weight in kg is {weight_into_kgs}')
