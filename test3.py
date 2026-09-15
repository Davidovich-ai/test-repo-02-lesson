user_input = input("February 2026: ")

parts = user_input.split()

if len(parts) != 2:
    print("Input error")
else:
    month = parts[0].capitalize()  
    year_str = parts[1]

    if not year_str.isdigit():
        print("Input error")
    else:
        year = int(year_str)

        months_31 = ["January", "March", "May", "July", "August", "October", "December"]
        months_30 = ["April", "June", "September", "November"]

        if month in months_31:
            print(31)
        elif month in months_30:
            print(30)
        elif month == "February":
            # Проверка на високосный год
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(29)  
            else:
                print(28) 
        else:
            print("Input error")  
