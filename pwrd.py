import numbers
import random

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols='.!:?<>'
number='1234567890'

all=lower+upper+symbols+number
length= 16
password="".join(random.sample(all,length))

print(password)