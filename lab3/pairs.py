def pairs(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                print(numbers[i] , numbers[j])


numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
pairs(numbers)