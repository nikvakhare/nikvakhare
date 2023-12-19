def check_condition(user_input):
    if user_input % 2 != 0:
        return "Weird"
    else:
        if 2 <= user_input <= 5:
            return "Not Weird"
        elif 6 <= user_input <= 20:
            return "Weird"
        else:()
            return "Not Weird"
print(check_condition(3))  # Replace 3 with any integer you want to check
print(check_condition(10))  # Replace 10 with another integer to check