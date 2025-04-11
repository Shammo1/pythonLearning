numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
odds = []

#for num in numbers:
   # if num % 2 == 1 and num % 5 == 0:
   #     odds.append(num)


       # odds.append(num)


#insted of using if else we can direct use this
""""Copyodd_numbers = [num for num in numbers if num % 2 == 1 if num % 5 == 0]

for num in numbers :
    print(Copyodd_numbers)"""
    
    
players = ['sakib', 'musfik', 'liton']
ages = [38, 37, 32]

age_comb = []
for player in players:
    for age in ages:
        age_comb.append([player, age])
        
print(age_comb)

