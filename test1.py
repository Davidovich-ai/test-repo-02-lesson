user_input = input("123_000_365")

if not user_input.isdigit():
    print("Input error")
else:
    number = int(user_input)
    if number <= 0 or number >= 1000000000:
        print("Input error")
    else:
        max_digit = max(user_input)
        print(max_digit)
