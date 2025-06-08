#Break & Continue

numbers  =[1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number == 3:
        break # use to pause/exit the loop prematurely
    print(number)


for number in numbers:
    if number == 4:
        continue# used to skip the current iteration of loop & proceed to next one
    print(number)