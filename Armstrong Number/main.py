def Armstrong_Number(num):
    #print(num)
    original = num
    armstrong_sum = 0
    length = len(str(num))
    
    while num > 0:
        digit = num % 10
        armstrong_sum = armstrong_sum + digit**length
        num //= 10
    
    if armstrong_sum == original:
        print(original, "is an Armstrong Number")
    else:
        print(original, "is not an Armstrong Number")
    
def main():
    input_number= int(input("Enter the Integer number= "))
    if (input_number>0):
        Armstrong_Number(input_number)
    else:
        print("Wrong")
    
if __name__ == "__main__":
  main()