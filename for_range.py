
start_value = int(input("start: ?"))
end_value   = int(input("end: ?"))

print("#"*80)
print("diapazon of value")
print("_"*50)

if start_value < end_value:
    for x in range(start_value, end_value+1):
        print(x, end = " ")
else:
    for x in range(start_value, end_value-1, -1 ):
        print(x, end = " ")

print()
print()
print("#"*80)
print("divaide by 3")
print("_"*50)

if  start_value < end_value:
    for x in range(start_value, end_value+1):
        if x % 3 == 0:
            print(x, end=" ")
else:
    for x in range(start_value, end_value-1, -1):
        if x % 3 == 0:
            print(x, end=" ")
print()
print()
n = 0
print("#"*80)
print("first 5 values that divized by 3")
print("_"*50)

if start_value < end_value:
    for x in range(start_value, end_value+1):
        if x % 3 == 0 and n < 5:
            print(x, end=" ")
            n += 1
else:
    for x in range(start_value, end_value-1, -1):
        if x % 3 == 0 and n < 5:
            print(x, end=" ")
            n += 1


