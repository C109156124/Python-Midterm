dict1={}
n=int(input("輸入筆數n:"))
for i in range (1,n+1):
    en=input("請輸入英文:")
    ch=input("請輸入中文:")
    dict1[en] = ch
a=input("請輸入查詢單字:")
if a in dict1:
    print(a+"中文意思為"+dict1[a])
else:
    print("字典未有此單字")