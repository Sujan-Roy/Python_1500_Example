# Calculate the largest number using python

def largest_number(num1,num2,num3):
    result= num1
    if(num2>result):
        result= num2
    if (num3>result):
        result = num3
    print("Largest number amonng the 3 input number = {}".format(result))
def main():
    a= int(input("Number1 ="))
    b= int(input("Number1 ="))
    c= int(input("Number1 ="))
    largest_number(a,b,c)

if __name__ == "__main__":
    main()