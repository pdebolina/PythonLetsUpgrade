# -*- coding: utf-8 -*-
"""BATCH6DAY3_ASSIGNMENT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FIAXWYE2Zzdd7efO40f_-n1ZZmrG6H89
"""

#QUESTION1:
def Add(*args):
  result=0
  for i in args:
    result+=float(i)
  return result
addition=Add(1,2,3,4,50)
print(addition)

#QUESTION
def IsPrime(num):
  num=int(num)
  dv=0
  for i in range(1,num+1):
    if(num%i==0):
      dv+=1
  

  if(dv==2):
    return "Prime"
  elif(dv>2):
    return "Non Prime"

num=input("Please enter an number : ")
status=IsPrime(num)
print("%s is : %s"%(num,status))