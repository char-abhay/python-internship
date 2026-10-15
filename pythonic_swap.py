a=10
b=20
print("before swap a=",a,"b=",b)
temp=a
a=b
b=temp
print(f"after swap a={a} b={b}")

#without temp variable pythonic way
print("without temp in pythonic way")
print("------------------------------")
c=30
d=40
print("before swap c=",c,"d=",d)
c,d=d,c
print(f"after swap c={c} d={d}")