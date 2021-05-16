# 1) declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).

list1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# 2) afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

list2 = list1.copy()
list2.sort()
print(list2)

# 3) afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

list3 = list1.copy()
list3.sort(reverse= True)
print(list3)

# 4) afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

even = list2[1::2]
print(even)

# 5) afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

odd = list2[0::2]
print(odd)

# 6) afișarea elementelor multipli ai lui 3.

mod3 = list2[2::3]
print(mod3)
