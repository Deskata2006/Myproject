import random
def input_int(prompt):
    s=input(prompt)
    return int(s)
def desetici(x):
    return (abs(x)//10)%10
def dvycif(x):
    ax=abs(x)           #ax e prosto promenliva
    return 10<= ax<=99
def tricif(x):
    ax=abs(x)
    return 100<= ax<=999
while True:
    try:
        n=input_int("Въведи цяло число от 10-50: ")
    except ValueError:
        print("Грешка трябва да въведеш цяло число ")
        continue
    if n>=10 and n<=50:
        break
    else:
        print("Трябва да сте в интервала от 10 до 50, опитай пак! ")
a=random.randint(-2500, -1300 )
b=random.randint(1111, 4444)
print(f"\nГенерирани граници са a={a} and b={b} ")
print(f"Сега въведи {n} числа в интервала {a} - {b} ")

mylist1=[]
while len(mylist1)<n:
    try:
        chislo=input_int(f"Елемент{len(mylist1)+1} / {n} :")
    except ValueError:
        print("Въведи валидно цяло цисло: ")
        continue
    if chislo>=a and chislo<=b:
        mylist1.append(chislo)
    else:
        print(f"Числото трябва да е между {a} and {b}, опитай пак! ")
    print("Списъкът mylist1 е ", mylist1)

coutOtrDes=0
for x in mylist1:
    if x<0:
        tens=desetici(x)
        if tens%4==0 and tens%5==0:
            coutOtrDes+=1
print(" Броя на отрицателните елементи в моя списък1, които десетици се делят на 4 и 5 са: ", coutOtrDes)

dvuChetni=[x for x in mylist1 if dvycif(x) and x%2==0 ]
if dvuChetni:
    avrDvuChetni=sum(dvuChetni)/len(dvuChetni)
    print("Двуцифрените , четни числа са ", dvuChetni)
    print(f"Средната стойностна двуцифрените, четни чиса е: {avrDvuChetni:.2f}")
else: 
    print("Няма двуцифрени, четни числа")

mylist2=[x for x in mylist1 if tricif(x) and x%3==0]
print("\nТрицифрени и кратни на 3 са въввтроя ми списък: ", mylist2)

coutNecetIndex=0
for inx, chiso in enumerate(mylist2): # enumerate means първата променлива ще е индекс, а втората число, независимо как се касват 
    if inx%2==1:
        if chiso%2!=0:                   
            coutNecetIndex+=1
print("Броя на нечетните числа с нечетен индех е:", coutNecetIndex)

for inx in range(len(mylist2)):
    if inx%2!=0:
        mylist2[inx]=13
print("Моят списък2 след замяната на елементите с нечетен индекс с 13 е:  ", mylist2)

len1=len(mylist1)
len2=len(mylist2)

print(f"Дължината на mylist1: {len1}, na mylist2: {len2} ")

if len1!=len2:
    if len1>len2:
        print("mylist1 е по дълъг от mylist2")
        if len(mylist1)>=2:
            removedFirst=mylist1.pop(0)
            removedLast=mylist1.pop(-1)
            print(f"Премахваме първия елемент{removedFirst} и премахване последния {removedLast}")

    else:
        print("mylist2 е подълъг от mylist1 ")
        if len(mylist2)>=2:
            removedFirst=mylist2.pop(0)
            removedLast=mylist2.pop(-1)
            print(f"Премахваме първия елемент{removedFirst} и последния{removedLast}")

else:
    print("Двата списика са еднакви")

print("\nКРАЕН РЕЗУЛТАТ:")
print("mylist1:", mylist1)
print("mylist2:", mylist2)


     







