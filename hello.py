attendance= int(input("Enter your attendance"))
if attendance>75:
    print("You are safe")
elif attendance>35 and attendance<74:
    print("You are in danger")    
elif attendance<35:
    print("go home")
else:
    print("Enter a valid attendance")    