def cont(s):
    count = 0
    for i in s:
        try:
            to_num = int(i)
            count += 1
            if count == 3:
                return True

        except:
            count = 0
        
    return False

s1 = "abc54abc"
s2 = "abc861xyz"   # "861" の部分が該当
s3 = "abc92def85477xyz"   # "85477" の部分が該当
s4 = "abc15def41gh7"

print(cont(s1))
print(cont(s2))
print(cont(s3))
r = cont(s4)
print(r)