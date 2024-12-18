from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79780725894"),
    Smartphone("Samsung", "Galaxy S21", "+79098765432"),
    Smartphone("Xiaomi", "Mi 11", "+79112233445"),
    Smartphone("Huawei", "P40 Pro", "+79556677889"),
    Smartphone("Google", "Pixel 5", "+79223344556")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")