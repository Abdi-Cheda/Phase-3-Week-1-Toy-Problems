def solve(s):
    vowels = "aeiou"
    consonant_values = {char: ord(char) - ord('a') + 1 for char in "abcdefghijklmnopqrstuvwxyz" if char not in vowels}

    def calculate_value(substring):
        return sum(consonant_values[char] for char in substring)

    max_value = 0
    current_substring = ""

    for char in s:
        if char not in vowels:
            current_substring += char
        else:
            max_value = max(max_value, calculate_value(current_substring))
            current_substring = ""

    max_value = max(max_value, calculate_value(current_substring)) # Check the last substring

    return max_value

def get_user_input():
    user_input = input("Enter a lowercase string with alphabetic characters only: ")
    return user_input

user_string = get_user_input() # Get user input

result = solve(user_string) # Determine and display the result
print(result)