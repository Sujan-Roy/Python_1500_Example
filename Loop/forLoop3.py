## print all the uppercase letters in s, one at a time

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'

for char in s:
    if char.isupper():
        print(char, end= '')
