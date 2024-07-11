from pathlib import Path

# to się uruchomi nawet przy imporcie
print("Początek modul.py")


def funkcja_a():
    print("Jestem funkcją A")


def funkcja_b():
    print("Jestem funkcją B")


def gdzie_jestem():
    print(Path("."))


def kim_jestem():
    print("Name:", __name__)
    print("File:", __file__)


# to się uruchomi nawet przy imporcie
funkcja_a()

# to się uruchomi nawet przy imporcie
zmienna_z_modulu = "jestem sobie zmienną z modułu modul.py"


kim_jestem()
print("Koniec modul.py")

if __name__ == "__main__":
    print("Uruchomiłeś mnie (modul.py) jako punkt startowy")
