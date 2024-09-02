A = int(input())
B = int(input())
C = int(input())
X = int(input())
A_List = []
B_List = []
C_List = []
for a in range(A):
    a_value = 500 * (a + 1)
    A_List.append(a_value)
for b in range(B):
    b_value = 100 * (b + 1)
    B_List.append(b_value)    
for c in range(C):
    c_value = 50 * (c + 1)
    C_List.append(c_value)

All_Lists = [A_List, B_List, C_List]
Value_Exist_Lists = [List for List in All_Lists if len(List) > 0]
count = 0
for value1 in Value_Exist_Lists[0]:
    if value1 == X:
        count += 1
    if len(Value_Exist_Lists) >= 2:
        for value2 in Value_Exist_Lists[1]:
            if value2 == X:
                count += 1
            if value1 + value2 == X:
                count += 1
            if len(Value_Exist_Lists) >= 3:
                for value3 in Value_Exist_Lists[2]:
                    if value3 == X:
                        count += 1
                    if value2 + value3 == X:
                        count += 1
                    if value1 + value2 + value3 == X:
                        count += 1
print(count)
                
        
