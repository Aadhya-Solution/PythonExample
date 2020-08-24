'''
List Comprehension
List comprehension is also very useful.
It's a quick way of creating a list that
contains exactly what you want.
Consider the following two examples,
first using a for loop:
'''

squares = []
for i in range(1,11):
    if i % 2 == 0:
        squares.append(i ** 2)

squares = [x ** 2 for x in range(1,11) if x % 2 == 0]


even_list =[x for x in range(0,10,2)]

f = lambda x: x*x
l=[f(x) for x in range(10)]
print l




p=[(lambda x: x*x)(x) for x in range(10)]
print p[0](2)

