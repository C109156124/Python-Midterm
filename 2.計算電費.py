a=int(input("輸入度數:"))
s=ns= 0
if a<=120:
    s=a*2.10
    ns=a*2.10
elif a>120 and a<=330:
    s=120*2.10+(a-120)*3.02
    ns=120*2.10+(a-120)*2.68
elif a>330 and a<=500:
    s=120*2.10+210*3.02+(a-330)*4.39
    ns=120*2.10+210*2.68+(a-330)*3.61
elif a>500 and a<=700:
    s=120*2.10+210*3.02+170*4.39+(a-500)*4.97
    ns=120*2.10+210*2.68+170*3.61+(a-500)*4.01
elif a>700:
    s=120*2.10+210*3.02+170*4.39+200*4.97+(a-700)*5.63
    ns=120*2.10+210*2.68+170*3.61+200*4.01+(a-700)*4.50
print("Summer months:"+str(s)+"\n"+"Non-Summer months:"+str(ns))
