for number in range(1,100): #perfect numbers: numbers that are equal to the sum of their nontrivial factors
        sum = 0
        for factor in range(1,number):
            if number % factor == 0:
                sum += factor
        if sum == number:
            print(number)
