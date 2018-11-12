import random
answer = random.randint(1,5)
print(answer)
your_answer = input("please input your number:")
if int(your_answer) == answer:
    print("correct")
else:
    print("wrong")
