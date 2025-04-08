def numeric_input():
    while True:
        user_input = input("Enter a numeric value: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a numeric value.")

def reverse_number(n):
    return int(str(n)[::-1])

def main():
    num = numeric_input()
    result_array = []

    if 0 < num < 500:
        reversed_num = reverse_number(num)
        result_array.append(reversed_num)
    elif 500 < num < 1000:
        half = num / 2
        reversed_half = reverse_number(int(half))
        result_array.append(reversed_half)
    else:
        print("Number does not in ranges.")

    print("Result array:", result_array)

if _name_ == "_main_":  # <-- fixed this line
    main()