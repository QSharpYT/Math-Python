# Define a function perfect_numbers that takes an integer n as input
def perfect_numbers(n): 
    # Initialize an empty list perfect_nums to store perfect numbers
    perfect_nums = []
    # Iterate over each number in the range from 1 to n (inclusive)
    for num in range(1,  n+1): 
        # Initialize a variable sum to store the sum of divisors of the current number
        sum = 0
        # Iterate over each number in the range from 1 to num (exclusive)
        for i in range(1,  num): 
            # If the current number is divisible by i (i.e., num % i == 0), add i to sum
            if num % i == 0: 
                sum += i
        # If the sum of divisors equals the current number, append it to perfect_nums
        if sum == num: 
            perfect_nums.append(num)
    # Return the list of perfect numbers
    return perfect_nums

# Prompt the user to enter a number to generate perfect numbers up to
generBetw = input("What number do you want to generate perfect numbers up to?: ")
# Call the perfect_numbers function with the user's input and print the result
print(perfect_numbers(int(generBetw)))
