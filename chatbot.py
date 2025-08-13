 bot_name= 'Smoke'
print(f"Hello! I'm {bot_name}. How can I help you?")

while True:
    user_input = input("You: ").lower()

    if user_input in ['hi', 'hello', 'hey']:
        print(f"{bot_name}: Hi there! How can I help you?")

    elif user_input in ['bye', 'goodbye']:
        print(f"{bot_name}: Goodbye, have a great day!")
        break  # End the program

    elif user_input in ['+', 'add', '-', 'subtract']:
        print(f"{bot_name}: Please enter two numbers.")8
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))

            if user_input in ['+', 'add']:
                print(f"{bot_name}: The sum is: {num1 + num2}")
            elif user_input in ['-', 'subtract']:
                print(f"{bot_name}: The difference is: {num1 - num2}")

        except ValueError:
            print(f"{bot_name}: Invalid input. Please enter valid numbers.")

    else:
        print(f"{bot_name}: Sorry, I didn't understand that.")
