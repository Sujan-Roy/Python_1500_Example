# square n where n is 0 to 9.
square= [n**2 for n in range(10)]
print(square)
# square n where n is 0 to 9 but n should be divide by 2.
square= [n**2 for n in range(10) if n%2==0]
print(square)

squares = []
for n in range(10):
    squares.append(n**2)
print(squares)
