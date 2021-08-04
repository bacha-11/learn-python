max_length = 12
stars = '*'
diff = 2

while len(stars) <= max_length:
    space = 2*max_length - diff
    print(' '*space, stars)
    stars += '*'
    diff += 1


while len(stars) > 0:
    space = 2*max_length - diff
    print(' '*space, stars)
    stars = stars[:-1]
    diff -= 1


print('------------------------------')


max_length = 11
stars = "*" 
diff = 2

while len(stars) < max_length:
    space = 2*max_length - diff
    res = len(stars) % 2
    if res == 1:
        print(' '*space, stars)
        stars += '*'
        diff += 1
    else:
        stars += '*'


while len(stars) > 0:
    space = 2*max_length - diff
    res = len(stars) % 2
    
    if res == 1:
        print(' '*space, stars)
        stars = stars[:-1]
        diff -= 1
    else:
        stars = stars[:-1]