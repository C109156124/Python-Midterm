a=int(input("小明身上有幾元:"))
b=int(input("販賣機有幾種飲料:"))
list1=[]
c=0
for i in range(1,b+1):
    d=int(input("輸入第%d種飲料價格：" %(i)))
    list1.append(d)
    if list1[i-1] <= a:
        c+=1
print(c)