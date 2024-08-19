def filterEvenNumbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Test cases
print(filterEvenNumbers([1, 2, 3, 4, 5]))         
print(filterEvenNumbers([10, 15, 20, 25]))        
print(filterEvenNumbers([7, 11, 13]))             
print(filterEvenNumbers([0, -2, -4])) 
