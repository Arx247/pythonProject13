# Arnas Oonsadao, 633040233-2
"""
Lab 3 Loops and Functional Programming Functions : Problem 2
"""
def fruits():
    list_of_fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
    lst2 = sorted(list_of_fruits, key=len)
    print(f"The fruits are {list_of_fruits}")
    print("After converting fruits to uppercase letters, fruits are")
    index = 0
    for value in list_of_fruits:
        print(index, value)
        index += 1
    print("After sorting fruits, fruits are")
    print(f"{lst2}")

if __name__ == "__main__":
    fruits()
