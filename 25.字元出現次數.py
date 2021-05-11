a=input("檢測的字串(end結束)：")
b=input("檢測的單一字元：")
while (a != "end"):
    print("字元%s出現的次數為：%d" %(b,a.count(b)))
    a=input("檢測的字串(end結束)：")
    if a=="end":
        break
    data2=input("檢測的單一字元：")    
print("檢測結束")