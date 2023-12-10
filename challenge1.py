def convert_to_24_hour_format(hour, minute, period):
    if period.lower() == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return "{:02d}{:02d}".format(hour, minute)

def get_user_input():
    hour = int(input("Enter the hour (1-12): "))
    minute = int(input("Enter the minute (0-59): "))
    period = input("Enter 'am' or 'pm': ").lower()

    return hour, minute, period

user_hour, user_minute, user_period = get_user_input() #Get user input

result = convert_to_24_hour_format(user_hour, user_minute, user_period) # Convert to 24-hour format

print("The time in 24-hour format is:", result) # Display the result