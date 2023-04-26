list1 = ["Hello","World","","Python","NLP","DP"]
list1.append("OpenCV")
print(list1)
print("length of list1= \n",len(list1))
list2 = list(filter(None, list1))
print("Display the output without Empty String\n",list2)
print("length of list2= \n",len(list2))