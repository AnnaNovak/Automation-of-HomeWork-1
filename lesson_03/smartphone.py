class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number


my_phone = Smartphone("Apple", "iPhone 13", "+79780725894")
print(my_phone.brand)  
print(my_phone.model)  
print(my_phone.phone_number)  