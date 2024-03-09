#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("99", end='\n')
        break
    print(str(num).zfill(2), end=', ')
