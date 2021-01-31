import random

lower = 'qwertyuıopğüasdfghjklşizxcvbnmöç'
upper = lower.upper()
number = '0123456789'
mark = '!^+%&/()=?_/*-'

total = lower + upper + number + mark

password = random.choices(total, k=10)

password = ''.join(password)
print(password)