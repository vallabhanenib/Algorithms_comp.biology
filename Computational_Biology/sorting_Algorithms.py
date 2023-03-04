# -*- coding: utf-8 -*-
"""Homework06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XAOF2YpfMqXSU4jF2k623gvLOO6qUCeA

Group Members: Bharathi Vallabhaneni, Ethan Kao

Discussed our ideas on how to implement and worked accordingly

Part I 

1) perform_reversal(data, a, b) function implementation
"""

def perform_reversal(data, a, b):
  list1 = data[0:a]
  list2 = data[a:b+1][::-1]
  list3 = data[b+1:]
  return list1+list2+list3

a = 2
b = 5
data = [0, 5, 4, 1, 3, 2, 6]
print(perform_reversal(data,a,b))

a1=3
b1=6
Test1 = [0, 1, 2, 6, 5, 4, 3, 7]
print(perform_reversal(Test1,a1,b1))

a2=2
b2=4
Test2 = [0, 5, 6, 2, 4, 3, 1, 7]
print(perform_reversal(Test2,a2,b2))

a3= 3
b3= 8
Test3 = [0, 6, 5, 4, 8, 7, 1, 2, 3, 9]
print(perform_reversal(Test3,a3,b3))

"""2) Implement your function to calculate the number of breakpoints

count_breakpoints(data) function implementation
"""

def count_breakpoints(data):
  breakP= 0
  for i in range(0, len(data)-1):
    if(abs(data[i+1]-data[i]) !=1):
      breakP +=1
  return breakP
#print(breakP)

data = [0, 5, 4, 1, 3, 2, 6]
print(count_breakpoints(data))

Test1 = [0, 1, 2, 6, 5, 4, 3, 7]
print(count_breakpoints(Test1))

Test2 = [0, 5, 6, 2, 4, 3, 1, 7]
print(count_breakpoints(Test2))

Test3 = [0, 6, 5, 4, 8, 7, 1, 2, 3, 9]
print(count_breakpoints(Test3))

"""3) Use the functions defined in questions 1 & 2, we can start implementing your function to locate a potential segment [a,b] whose reversal would remove the maximum number of breakpoints. """

def find_best_reversal(data):
  index = []
  bp_count = count_breakpoints(data)
  for a in range(1, len(data)-2):
    for b in range(a+1,len(data)-1):
      Temp = perform_reversal(data,a,b)
      if count_breakpoints(Temp) < bp_count:
        index.clear()
        index.append(a)
        index.append(b)
        bp_count = count_breakpoints(Temp)
  if index == []:
    index = [-1,-1]
  return index

data = [0, 5, 4, 2, 3, 1, 6, 7]
print(find_best_reversal(data))

def find_best_reversal1(data):
  index = []
  bp_count = count_breakpoints(data)
  for a in range(0, len(data)-1):
    for b in range(a,len(data)-1):
      if a==b:
        continue
      if a<b:
        Temp = perform_reversal(data,a,b)
      else:
        Temp = perform_reversal(data,b,a)
      if count_breakpoints(Temp) <= bp_count:
        index.clear()
        if a<b:
          index = [a,b]
        else:
          index = [b,a]
        bp_count = count_breakpoints(Temp)
  if index == []:
    print('Error')
    exit(-1)
    
    for i in range(len(List)-1):
      if abs(List[i] - List[i+1]) != 1:
        pos1 = i
        pos2 = List.index(List[i]+1)
        if pos1 < pos2:
          indice = [pos1+1, pos2]
        else:
          indice = [pos2,pos1-1]
        break
    
  return index
    
data = [0, 5, 4, 2, 3, 1, 6, 7]
print(find_best_reversal1(data))

Test1=[0, 1, 2, 6, 5, 4, 3, 7]
print(find_best_reversal(Test1))

Test2=[0, 5, 6, 2, 4, 3, 1, 7]
print(find_best_reversal(Test2))

Test3=[0, 6, 5, 4, 8, 7, 1, 2, 3, 9]
print(find_best_reversal(Test3))

"""4) In order to handle the case that no existing indices a & b can reduce the number of breakpoints, we need to reverse an increasing strip. We need implement the following function:

find_increasing_strip(data) function implementation
"""

import more_itertools as mit
def find_increasing_strip(data):
  Temp_List = [list(i) for i in mit.consecutive_groups(data)]
  #print(Temp_List)
  inc_strip =[]
  for j in range(len(Temp_List)):
    if len(Temp_List[j])>1:
      inc_strip.append(Temp_List[j])
  a= inc_strip[1][0]
  b= inc_strip[1][len(inc_strip[1])-1]

  return [data.index(a), data.index(b)]

data = [0, 1, 2, 5, 6, 7, 3, 4, 8]
print(find_increasing_strip(data))

Test1=[0, 1, 2, 6, 5, 3, 4, 7]
print(find_increasing_strip(Test1))

Test2=[0, 1, 5, 6, 2, 3, 4, 7]
print(find_increasing_strip(Test2))

Test3=[0, 1, 6, 5, 8, 7, 2, 3, 4, 9]
print(find_increasing_strip(Test3))

"""5) Then we should integrate all the above functions to derive the following algorithm:

sort_by_reversal(data) implementation
"""

def sort_by_reversal(data):
  brk_point= count_breakpoints(data)
  step = 0
  print('There are ',brk_point, 'BreakPoints in this pattern','\n')
  while brk_point >=1:
    if find_best_reversal1(data) != [-1,-1]:
      print('Performing inversion for a=',find_best_reversal(data)[0], 'b=',find_best_reversal(data)[1], 'results in')
      new_reversal = find_best_reversal1(data)
    else:
      new_reversal = find_increasing_strip(data)
      print('No BreakPoint removed in this step')

    data = perform_reversal(data,new_reversal[0],new_reversal[1])
    brk_point = count_breakpoints(data)
    step +=1

    print('Step',step,':','\n')
    print('Data after reversal:', data)
    print('There are ',brk_point, 'BreakPoints in this pattern')
    
    print('--------------------------------------')
  print('Used',step,'reversals')
  return
    
data = [0,15,10,2,16,4,3,9,20,19,18,6,22,8,13,14,11,5,7,21,12,17,1,23,24]
print('Data = ',data,'\n')
print('Start reversal steps: ','\n')
sort_by_reversal(data)

Test1= [0, 10, 13, 16, 14, 2, 15, 1, 17, 18, 8, 7, 6, 5, 4, 3, 12, 9, 11, 19]
print('Data = ',Test1,'\n')
print('Start reversal steps: ','\n')
sort_by_reversal(Test1)

Test2= [0, 20, 1, 21, 22, 11, 10, 15, 5, 4, 6, 7, 8, 2, 17, 16, 9, 3, 19, 13, 14, 18, 23, 12, 24]
print('Data = ',Test2,'\n')
print('Start reversal steps: ','\n')
sort_by_reversal(Test2)

Test3= [0, 16, 17, 12, 14, 3, 15, 31, 20, 7, 6, 43, 39, 36, 11, 32, 38, 33, 34, 47, 13, 18, 4, 24, 29, 48, 46, 45, 5, 37, 35, 19, 44, 30, 21, 10, 9, 8, 25, 26, 2, 23, 28, 27, 1, 40, 41, 22, 42, 49]
print('Data = ',Test3,'\n')
print('Start reversal steps: ','\n')
sort_by_reversal(Test3)

Test4= [0, 2, 89, 54, 95, 16, 12, 53, 75, 70, 65, 36, 18, 17, 85, 46, 94, 15, 49, 50, 43, 44, 45, 83, 67, 68, 87, 88, 51, 69, 61, 60, 20, 76, 64, 42, 72, 6, 26, 74, 35, 34, 21, 22, 23, 24, 25, 38, 37, 30, 93, 90, 52, 62, 57, 82, 59, 9, 19, 41, 40, 39, 1, 3, 4, 5, 71, 31, 86, 48, 84, 58, 55, 56, 66, 91, 92, 8, 81, 63, 96, 97, 29, 28, 27, 80, 79, 78, 77, 32, 33, 14, 13, 7, 11, 10, 73, 47, 98]
print('Data = ',Test4,'\n')
print('Start reversal steps: ','\n')
sort_by_reversal(Test4)

"""Part II

Algorithm 1:

SimpleReversalSort Implementation:

"""

def SimpleReversalSort(data):
  reversal = 0
  for i in range(len(data)-1):
    j = data.index(min(data[i:]))
    if j !=i:
      data = perform_reversal(data,i,j)
      reversal +=1
      print('Reversion',reversal,':','\n')
      print('Performing inversion for a=',i,'b=',j,'\n')      # will return a, b
      print('After inversion:',data,'\n')                     # will return data after reversal
  print('Used', reversal,'Reversals','\n')
  return

data = [0, 5, 4, 1, 3, 2, 6]
SimpleReversalSort(data)

print('Test data 1:')
Test1= [0, 10, 13, 16, 14, 2, 15, 1, 17, 18, 8, 7, 6, 5, 4, 3, 12, 9, 11, 19]
SimpleReversalSort(Test1)

print('Test data 2:')
Test2= [0, 20, 1, 21, 22, 11, 10, 15, 5, 4, 6, 7, 8, 2, 17, 16, 9, 3, 19, 13, 14, 18, 23, 12, 24]
SimpleReversalSort(Test2)

print('Test data 3:')
Test3= [0, 16, 17, 12, 14, 3, 15, 31, 20, 7, 6, 43, 39, 36, 11, 32, 38, 33, 34, 47, 13, 18, 4, 24, 29, 48, 46, 45, 5, 37, 35, 19, 44, 30, 21, 10, 9, 8, 25, 26, 2, 23, 28, 27, 1, 40, 41, 22, 42, 49]
SimpleReversalSort(Test3)

print('Test data 4:')
Test4= [0, 2, 89, 54, 95, 16, 12, 53, 75, 70, 65, 36, 18, 17, 85, 46, 94, 15, 49, 50, 43, 44, 45, 83, 67, 68, 87, 88, 51, 69, 61, 60, 20, 76, 64, 42, 72, 6, 26, 74, 35, 34, 21, 22, 23, 24, 25, 38, 37, 30, 93, 90, 52, 62, 57, 82, 59, 9, 19, 41, 40, 39, 1, 3, 4, 5, 71, 31, 86, 48, 84, 58, 55, 56, 66, 91, 92, 8, 81, 63, 96, 97, 29, 28, 27, 80, 79, 78, 77, 32, 33, 14, 13, 7, 11, 10, 73, 47, 98]
SimpleReversalSort(Test4)

"""Algorithm 2:

BreakPointReversalSort Implementation:
"""

def BreakPointReversalSort(data):
  brk_point= count_breakpoints(data)
  step = 0
  print('There are ',brk_point, 'BreakPoints in this pattern','\n')
  while brk_point > 0:
    new_reversal = find_best_reversal1(data)
    print('Performing inversion for a=',find_best_reversal1(data)[0], 'b=',find_best_reversal1(data)[1], 'results in')
    data = perform_reversal(data,new_reversal[0],new_reversal[1])
    brk_point = count_breakpoints(data)
    step +=1

    print('Step',step,':','\n')
    print('Data after reversal:', data)
    print('There are ',brk_point, 'BreakPoints in this pattern')
    
    print('--------------------------------------')
  print('Used',step,'reversals')
  return

data = [0,15,10,2,16,4,3,9,20,19,18,6,22,8,13,14,11,5,7,21,12,17,1,23,24]
print('Data = ',data,'\n')
print('Start reversal steps: ','\n')
BreakPointReversalSort(data)

print('Test data 1:')
Test1= [0, 10, 13, 16, 14, 2, 15, 1, 17, 18, 8, 7, 6, 5, 4, 3, 12, 9, 11, 19]
BreakPointReversalSort(Test1)

print('Test data 2:')
Test2= [0, 20, 1, 21, 22, 11, 10, 15, 5, 4, 6, 7, 8, 2, 17, 16, 9, 3, 19, 13, 14, 18, 23, 12, 24]
BreakPointReversalSort(Test2)

print('Test data 3:')
Test3= [0, 16, 17, 12, 14, 3, 15, 31, 20, 7, 6, 43, 39, 36, 11, 32, 38, 33, 34, 47, 13, 18, 4, 24, 29, 48, 46, 45, 5, 37, 35, 19, 44, 30, 21, 10, 9, 8, 25, 26, 2, 23, 28, 27, 1, 40, 41, 22, 42, 49]
BreakPointReversalSort(Test3)

print('Test data 4:')
Test4= [0, 2, 89, 54, 95, 16, 12, 53, 75, 70, 65, 36, 18, 17, 85, 46, 94, 15, 49, 50, 43, 44, 45, 83, 67, 68, 87, 88, 51, 69, 61, 60, 20, 76, 64, 42, 72, 6, 26, 74, 35, 34, 21, 22, 23, 24, 25, 38, 37, 30, 93, 90, 52, 62, 57, 82, 59, 9, 19, 41, 40, 39, 1, 3, 4, 5, 71, 31, 86, 48, 84, 58, 55, 56, 66, 91, 92, 8, 81, 63, 96, 97, 29, 28, 27, 80, 79, 78, 77, 32, 33, 14, 13, 7, 11, 10, 73, 47, 98]
BreakPointReversalSort(Test4)

"""Algorithm 3:

ImprovedBreakPointReversalSort implentation
"""

def find_decreasing_strip(data):
    Temp_List = [data[i+1] - data[i] for i in range(len(data)-1)]
    dec_Strip = []
    start = 0
    for i, j in enumerate(Temp_List):
        if (abs(j) == 1) and (j == Temp_List[start]):
            continue   
        if (start > 0):
            if Temp_List[start] != 1:
                dec_Strip.append([start, i])
        start = i+1
    dec_strip = []
    for i in dec_Strip:
      if i[0] != i[1]:
        dec_strip.append(i)
    return (dec_strip)

data = [0, 10, 13, 16, 14, 2, 15, 1, 17, 18, 8, 7, 6, 5, 4, 3, 12, 9, 11, 19]
print(find_decreasing_strip(data))
print('Test data 2:')
Test2= [0, 20, 1, 21, 22, 11, 10, 15, 5, 4, 6, 7, 8, 2, 17, 16, 9, 3, 19, 13, 14, 18, 23, 12, 24]
find_decreasing_strip(Test2)

def ImprovedBreakPointReversalSort(data):
  brk_point= count_breakpoints(data)
  step = 0
  print('There are ',brk_point, 'BreakPoints in this pattern','\n')
  while brk_point > 0:
    decreasing_strip = find_decreasing_strip(data)
    if len(decreasing_strip) > 0:
      print('Performing inversion for a=',find_best_reversal1(data)[0], 'b=',find_best_reversal1(data)[1], 'results in')
      new_reversal = find_best_reversal1(data)
    else:
      new_reversal = find_increasing_strip(data)
      print('No BreakPoint removed in this step')

    data = perform_reversal(data,new_reversal[0],new_reversal[1])
    brk_point = count_breakpoints(data)
    step +=1

    print('Step',step,':','\n')
    print('Data after reversal:', data)
    print('There are ',brk_point, 'BreakPoints in this pattern')
    
    print('--------------------------------------')
  print('Used',step,'reversals')
  return


print('Test data 1:')
Test1= [0, 10, 13, 16, 14, 2, 15, 1, 17, 18, 8, 7, 6, 5, 4, 3, 12, 9, 11, 19]
ImprovedBreakPointReversalSort(Test1)

print('Test data 2:')
Test2= [0, 20, 1, 21, 22, 11, 10, 15, 5, 4, 6, 7, 8, 2, 17, 16, 9, 3, 19, 13, 14, 18, 23, 12, 24]
ImprovedBreakPointReversalSort(Test2)

print('Test data 3:')
Test3= [0, 16, 17, 12, 14, 3, 15, 31, 20, 7, 6, 43, 39, 36, 11, 32, 38, 33, 34, 47, 13, 18, 4, 24, 29, 48, 46, 45, 5, 37, 35, 19, 44, 30, 21, 10, 9, 8, 25, 26, 2, 23, 28, 27, 1, 40, 41, 22, 42, 49]
ImprovedBreakPointReversalSort(Test3)

print('Test data 4:')
Test4= [0, 2, 89, 54, 95, 16, 12, 53, 75, 70, 65, 36, 18, 17, 85, 46, 94, 15, 49, 50, 43, 44, 45, 83, 67, 68, 87, 88, 51, 69, 61, 60, 20, 76, 64, 42, 72, 6, 26, 74, 35, 34, 21, 22, 23, 24, 25, 38, 37, 30, 93, 90, 52, 62, 57, 82, 59, 9, 19, 41, 40, 39, 1, 3, 4, 5, 71, 31, 86, 48, 84, 58, 55, 56, 66, 91, 92, 8, 81, 63, 96, 97, 29, 28, 27, 80, 79, 78, 77, 32, 33, 14, 13, 7, 11, 10, 73, 47, 98]
ImprovedBreakPointReversalSort(Test4)