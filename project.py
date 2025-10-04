try:
    age=int(input("enter your age: "))
    print("even" if age %2==0 else"odd")
except:
    print("invalid input!")