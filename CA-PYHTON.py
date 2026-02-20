a = int(input("price1: "))
b = int(input("price2: "))
c = int(input("price3: "))
d = a + b + c
discount = 0
if(d>50):
    discount = d*10/100
final = d - discount
print(f"total: ${d}")
if discount > 0:
    print(f"Discount applied: ${discount}")
else:
    print(f"No discount")
print(f"Final amount: ${final}")