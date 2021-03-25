temp_command = ""
is_car_stopped = True
while True:
    command = input("> ").upper()
    if command == "START":
        if is_car_stopped == True:
            print("Car started. Ready to go!")
            is_car_stopped = False
        else:
            print("Hey! The car is already running!")
    elif command == "STOP":
        if is_car_stopped == False:
            print("Car stopped.")
            is_car_stopped = True
        else:
            print("Car has already stopped!")
    elif command == "HELP":
        print('''Start - to start the car
Stop - to stop the car
Quit - to quit''')
    elif command == "QUIT":
        break
    else:
        print("I don't understand that...")