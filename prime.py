
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(n):
    # Start checking from the next number
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate

# Test the function
number = int(input("Enter a number: "))
next_prime_number = next_prime(number)
print(f"The next prime number after {number} is {next_prime_number}.")
