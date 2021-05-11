a=list(input("甲方的數字:"))
b=list(input("乙方的數字:"))
f=""
for i in range(0,len(a)):   
    if int(a[i])-int(b[i])==-4:
        c="贏"
        f=f+c
    elif int(a[i])-int(b[i])==1:
        c="贏"
        f=f+c
    elif int(a[i])-int(b[i])==4:
        d="輸"
        f=f+d
    elif int(a[i])-int(b[i])==-1:
        d="輸"
        f=f+d
    else:
        e="和"
        f=f+e
print("洗刷刷結果："+f)