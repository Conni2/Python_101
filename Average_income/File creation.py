# 17th Project: File creation
# Purpose: Practice creating files

with open('Average_income/October_profit.txt', 'w') as f:
    day = 1
    while day < 32:
        revenue = int(input("October {} revenue: ".format(day)))
        f.write('October {}: {}\n'.format(day, revenue))
        day += 1