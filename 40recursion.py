#1)
# def sample():
#     print("Learning python")
#     sample()
# sample()

#2) factorial by recursion
def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * fact(n - 1)  # Recursive call

n = int(input("Enter a number: "))
print(fact(n))




