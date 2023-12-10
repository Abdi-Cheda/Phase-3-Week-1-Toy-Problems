def exactly_two_positive(a, b, c):
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

def get_user_input():
    a = int(input("Enter the first integer (a): "))
    b = int(input("Enter the second integer (b): "))
    c = int(input("Enter the third integer (c): "))

    return a, b, c

user_a, user_b, user_c = get_user_input() # Get user input

result = exactly_two_positive(user_a, user_b, user_c) # Determine and display the result
print(result)