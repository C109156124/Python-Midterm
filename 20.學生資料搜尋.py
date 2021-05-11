num=["123","456","789","321","654"]
name=["Tom","Cat","Nana","Lim","Won"]
obj=["DTGD","CSIE","ASIE","DBA","FDD"]
n=input("輸入查詢學號為:")
a=num.index(n)
if n==num[a]:
    print("學生資料為:"+str(num[a]+" "+name[a]+" "+obj[a]))
else:
    print("查無此號碼")