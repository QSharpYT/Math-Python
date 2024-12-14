#PrimeApe prime num gen
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    prime_nums = []
    for number in range(2, limit + 1):
        if is_prime(number):
            prime_nums.append(number)
    return prime_nums

limit = int(input("Generate prime numbers up to:"))
print("PrimeApe (script) ^is_prime^ from <^get_primes^>")
prime_nums = get_primes(limit)
print(f"PrimeApe  {limit}: {prime_nums}")
print("Execution complete")