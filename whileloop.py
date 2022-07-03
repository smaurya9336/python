while True:
    response=input("Which Python data type is an ordered sequence?").lower()
    print("You entered:",response)
    if response =="list":
        print("You have cleared the test.")
        break
    
    elif response=="tuple":
        print("You have cleared the test.")
        break
    else:
        print("Your input is wrong. Please try again.")