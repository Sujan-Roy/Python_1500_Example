num = int(input("Enter Number= "))
reverse_num = 0
while num>0:
    remainder = num % 10
    reverse_num = (reverse_num*10)+remainder
    num= num//10
print("Reverse Number= ", reverse_num)
