num=int(input("Vyvedete cqlo chislo"))

faktoriel=1

if num<0:
    print("няма факториел")
elif num==0:
    print("факориелът е 1")
else:
    for i in range(1, num+1):
        faktoriel=faktoriel*i
    print("factorielyt na", num, "e", faktoriel)