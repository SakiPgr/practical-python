# bounce.py
#
# Exercise 1.5
height = 100
drop = 0

while drop < 10:
    drop += 1
    height = height * 0.6
    print(drop, round(height, 4))
