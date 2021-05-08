# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as file:
    data = file.readlines()

sum = 0

for line in data[1:]:
    line_data = line.strip().split(',')
    sum += int(line_data[1]) * float(line_data[2])

print(f"Total cost {sum}")
