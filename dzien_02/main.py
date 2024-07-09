# czyszczenie terminala, odpowiednik Ctrl-L
print("\033c", end="")

### ===========

# lista to kolekcja elementów, może by kolekcją różnych typów
# lista = [1, "abc", "z", 123.45]
# # print(lista)

# # lista 1-elementowa
# lista_jeden_elem = [1]
# # print(lista_jeden_elem)

# zmienna = 123
# lista_ze_zmienna = [1, 2, zmienna]
# print(lista_ze_zmienna)
# zmienna = 567
# print(lista_ze_zmienna)

# lista może zawierac inne listy
# lista_list = [
#     lista,
#     lista_jeden_elem,
#     zmienna,
#     "jestem wpisana z ręki",
#     lista_ze_zmienna,
#     lista,
#     lista_jeden_elem,
#     zmienna,
#     "jestem wpisana z ręki",
#     lista_ze_zmienna,
#     lista,
#     lista_jeden_elem,
#     zmienna,
#     "jestem wpisana z ręki",
#     lista_ze_zmienna,
# ]
# print(lista_list)

# iteracja po liście
# for element in lista_list:
#     print(element)

# for licznik, element in enumerate(lista_list):
#     print(licznik, element)
#     if 2 < licznik < 4:
#         print("coś robię")


# # konkretny element z listy - indeks liczony od 0 włącznie, tu bierzemy indeks 2
# print()
# print(lista_list[2]) # zwraca element

# # zakres - indeks od 2 do 4, 4 nie należy do przedziału
# print()
# print(lista_list[2:4]) # zwraca listę

# # zakres - od 2 do 10 (10-tka nie należy) co 3
# print()
# print(lista_list[2:10:3]) # zwraca listę

# ostatni element
# print()
# print(lista_list[-1])

# przedostatni element
# print()
# print(lista_list[-2])

# lista od końca
# print()
# print(lista_list[::-1])

# # czy lista jest pusta
# pusta_lista = []
# if pusta_lista:
#     print("jestem NIEPUSTĄ listą")
# else:
#     print("jestem PUSTĄ listą")

# niepusta_lista = []
# if niepusta_lista:
#     print("jestem NIEPUSTĄ listą")
# else:
#     print("jestem PUSTĄ listą")


# jak stworzyc pusta liste i dodac do niej elementy?
# lista = []

# lista.append("abc")
# print(lista)

# lista.append(123)
# print(lista)


### ZDANIE

# Napisz kod który umieści (append) w nowej liście 10 kolejnych (range()) potęg liczby 2.
# Następnie przeiteruj po tej liście (for-em) i każdy z jej elementów wyświetl na konsoli w osobnej linii.


# rozwiązanie

# lista = []
# # dodawanie elementów do listy
# for potega in range(10):
#     lista.append(2**potega)

# # wyświetlenie listy
# for elem in lista:
#     print(elem)

# rzutowanie generatora range() na listę
lista = list(range(10))
# print(lista)

# podmiana 1 wartości w liście
# lista[4] = "123"
# print(lista)

# podmiana zakresu w liście
# lista[5:8] = [0, 0]
# print(lista)

# lista.clear()
# print(lista)

# mutowalnośc i nie mutowalnosc
# lista2 = lista # czy to jest kopia listy?
# print("lista", lista)
# print("lista2", lista2)

# lista[4] = "to zmieniłem"
# print("lista", lista)
# print("lista2", lista2) # to samo co w liście 'lista'! czyli nie zrobiła się kopia - 2 zmienne zawieraja to samo

# lista2 = lista.copy()
# print("lista", lista)
# print("lista2", lista2)

# lista[4] = "to zmieniłem"
# print("lista", lista)
# print("lista2", lista2)

# dodanie elementu przed indeksem
# print(lista)
# lista.insert(5, "abc")
# print(lista)

# dodanie elementu przed indeksem
# print(lista)
# if lista.count(6):
#     lista.remove(6)
# print(lista)

# dodawanie listy za listą
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# print(l1 + l2)

# lub - do l1 dopisane zostaną wartości z l2
# l1.extend(l2)

# lista = list(range(10)) + list(range(10)) + list(range(10))
# print(lista)

# if lista.count(6):
#     lista.remove(6)
# print(lista)

# lista = list(range(10)) + list(range(10)) + list(range(10))

# nowa_lista = []
# for e in lista:
#     if e == 6:
#         continue
#     nowa_lista.append(e)

# print(nowa_lista)


### Zadanie

# Napisz program, który pobierze od użytkownika 10 liczb, zapamięta je (zapisze na liście),
# a na koniec wyświetli całą listę pobranych wartości od końca.

# rozwiązanie

# lista = []
# for _ in range(10):
#     lista.append(input("Daj liczbę: "))

# print(lista[::-1])


# listy składane, list comprehention

# lista = []
# for i in range(10):
#     wartosc = 2**i
#     lista.append(wartosc)

# print(lista)


# # to samo z użyciem list comprehention:
# lista2 = [2**i for i in range(10)]
# print(lista2)


# lista2 = [
#     2**i
#     for i in range(10)
#     ]

# napis (string) to lista znaków:
# napis = "abcdefghijkl"
# for literka in napis:
#     print(literka)

### ZADANIE

# Utwórz listę znaków (poprzez list comprehention) z napisu
# Spróbuj do listy dodawac wielkie litery.

# wejście: "abcdefghijkl"
# wyjście: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

# rozwiązanie zadania

# lista = [literka.upper() for literka in "abcdefghijkl"]
# print(lista)


# for w forze - list comprehention

# wersja pełna
# lista = []
# for i in range(10):
#     for j in range(10):
#         lista.append(f"{i=} {j=}")
# print(lista)

# wersja skrócona/lista składana
# lista = [f"{i=} {j=}" for i in range(10) for j in range(10)]
# print(lista)


# # jak policzyc ile czasu zajmuje nasz kod?
# import time

# start_time = time.time() # zwraca ile sekund upłynęło od północy 1970-01-01
# time.sleep(5)
# end_time = time.time()
# print(f"Minęło: {end_time-start_time} sekund")


# czy list comprehention jest szybsze?
# jak policzyc ile czasu zajmuje nasz kod?
# import time

# ILE_RAZY = 100_000_000

# start_time = time.time()  # zwraca ile sekund upłynęło od północy 1970-01-01
# lista = list()
# lista = []
# for i in range(ILE_RAZY):
#     lista.append(i)
# end_time = time.time()
# print(f"Normalna pętla - minęło: {end_time-start_time} sekund")

# start_time = time.time()  # zwraca ile sekund upłynęło od północy 1970-01-01
# lista = [i for i in range(ILE_RAZY)]
# end_time = time.time()
# print(f"List comp - minęło: {end_time-start_time} sekund")


# import random

# random.choice([1,2,3])
# random.random()

### ZADANIE

# Korzystając z funkcji  randint() z pakietu random w postaci listy składanej wygeneruj
# 100 losowych liczb z zakresu 1-20 i wyświetl liste w konsoli.


# rozwiązanie:
# import random

# lista = [random.randint(1, 20) for _ in range(100)]
# print(lista)


# if w list comprehention

# lista = []
# for potega in range(10):
#     if potega % 2:
#         continue
#     lista.append(2**potega)
# print(lista)

# lista2 = [2**potega for potega in range(10) if potega % 2 == 0]
# print(lista2)


# list comp - lista list

lista = [[potega, 2**potega] for potega in range(10)]
print(lista)

# wyświetlanie n-tego elementu z listy list
for element in lista:
    print(f"Dwa podniesione do potęgi {element[0]} to jest {element[1]}")


lista_str = [
    f"Dwa podniesione do potęgi {element[0]} to jest {element[1]}" for element in lista
]
print("\n".join(lista_str))
