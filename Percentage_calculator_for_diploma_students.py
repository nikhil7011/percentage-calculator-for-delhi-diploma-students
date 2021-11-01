
a = input("Enter maximun Marks of first sem:")


a = int(a)


# 20% of First semester

first_sem_mm = (20/100)*a

# This is The Final result of first semester


c = input("Enter Maximum Marks of 2nd sem:")


c = int(c)

second_sem_mm = (20/100)*c


e = input("Enter Maximum Marks of third semester:")

e = int(e)

third_sem_mm = (40/100)*e


g = input("Enter Maximum Marks of fourth semester:")

g = int(g)

fourth_sem_mm = (40/100)*g


print(third_sem_mm+fourth_sem_mm)

h = input("Enter Maximum Marks of fifth semester:")

h = int(h)

fifth_sem_mm = (40/100)*h


i = input("Enter Maximum Marks of Sixth semester:")

i = int(i)

sixth_sem_mm = (40/100)*i


f = (first_sem_mm+second_sem_mm+third_sem_mm+fourth_sem_mm+fifth_sem_mm+sixth_sem_mm)


print("Your Maximum Marks in diploma\t",f)


print("------ NOW ENTER YOUR OBTAIN MARKS-------")


m = input("Enter Obtain Marks of fist sem:")

m = int(m)
 
first_sem_ob = (20/100)*m


v = input("Enter Obtain Marks of second semester:")

v = int(v)

second_sem_ob = (20/100)*v


x = input("Enter your obtain marks of third semester:")

x = int(x)

third_sem_ob = (40/100)*x


l = input("Enter your obtain marks of fourth semester:")

l = int(l)

fourth_sem_ob = (40/100)*l

k = input("Enter your obtain marks of fifth semester:")

k = int(k)

fifth_sem_ob = (40/100)*k


j = input("Enter your obtain marks of sixth semester:")

j = int(j)

sixth_sem_ob = (40/100)*j



ff = (first_sem_ob+second_sem_ob+third_sem_ob+fourth_sem_ob+fifth_sem_ob+sixth_sem_ob)

print("you got \t",ff)  

q = ff*(100/f)

print("your percentage is-:",q)