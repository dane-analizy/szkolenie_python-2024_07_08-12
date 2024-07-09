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
