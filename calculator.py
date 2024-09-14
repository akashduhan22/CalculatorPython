def add(num1,num2):
    # print()
    return f"Your result is {num1+num2}"

def sub(num1,num2):
    return f"Your result is {num1-num2}"

def mul(num1,num2):
    return f"Your result is {num1*num2}"

def div(num1,num2):
    return f"Your result is {num1/num2}"

def again():
    print()
    choice=input("Do you want to calculate something more(Yes/No)").lower()
    if choice=="yes" or choice=="y":
        main()
    elif choice=="n" or choice=="no":
        print("Okay thanks for using calculator")
    else:
        print("Enter proper message")
        again()


def main():
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter second number:"))
    print("Enter the operation you want to perform: \n1.Addition \n2.Subtraction \n3.Multiply \n4.Division")
    user=input("Enter your choice:").lower()
    if user=="1" or user=="add" or user=="addition" or user=="sum":
        print(add(num1,num2)) 
    elif user=="2" or user=="sub" or user=="subtaction" or user=="minus":
        print(sub(num1,num2))
    elif user=="3" or user=="mul" or user=="multiplition" or user=="multiply":
        print(mul(num1,num2))
    elif user=="4" or user=="div" or user=="division" or user=="divide":
        print(div(num1,num2))
    else:
        print()
        print("choose proper operation ")
        print()
        main()
    print()
    again()

main()