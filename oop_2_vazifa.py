# 1-masala


# class User:
#     def __init__(self,name, email, address):
#         self.name=name
#         self.email=email
#         self.address=address

#     def get_name(self):
#         return self.name
#     def get_email(self):
#         return self.email
#     def get_adres(self):
#         return self.address
#     def set_ad(self,new_ad):
#         self.address=new_ad
#     def __str__(self):
#         return f"""{self.name} 
# {self.address} 
# {self.email}"""

# class Customer(User):
#     def __init__(self, name, email, address, cart=None, balance=0):
#         super().__init__(name, email, address)
#         self.balance = balance
#         self.cart = [] if cart is None else cart

#     def add_to_cart(self, product, qty, price) -> None:
#         try:
#             if not qty>0 or not price>=0:
#                 raise ValueError("qty>0, price>=0 bo'lishi kerak.")
#             else:

#                 toplam=(product,qty,price)
#                 self.cart.append(toplam)
#         except ValueError as xato:
#             print(xato)

#     def clear_cart(self) -> None:
#         self.cart.clear()

#     def get_cart_total(self) -> int:
#         summa=0
#         for mahsulot in self.cart:
#             summa_i=mahsulot[1]*mahsulot[2]
#             summa+=summa_i
#         return summa
#     def checkout(self) -> bool:
#         summa=self.get_cart_total()
#         if self.balance>=summa:
#             self.balance-=summa
#             self.cart.clear()
#             return True
#         else:
#             return False
#     def __str__(self):
#         return f"""{super().__str__()} 
# balance: {self.balance}"""

# class Seller(User):
#     def __init__(self, name, email, address,products=None,rating=0.0):
#         super().__init__(name, email, address)
#         self.products= {} if products is None else products
#         self.rating=rating
#     def add_product(self, name, qty) -> None:
#         try:
#             if qty<=0:
#                 raise ValueError("qty>0 bo'lishi shart.")
#             else:
#                 if name in self.products:
#                     self.products[name][1]+=qty
#                 else:
#                     self.products[name]=qty
#         except ValueError as xato:
#             print(xato)
#     def remove_product(self, name) -> bool:
#         if name in self.products:
#             self.products.remove(name)
#             return True
#         else:
#             return False
#     def update_stock(self, name, delta_qty) -> bool:
#         if name in self.products:
#             self.products[name]+=delta_qty
#             return True
#         else:
#             return False
#     def get_stock(self) -> dict[str,int]:
#         return self.products.copy()
#     def __str__(self):
#         return f"""Seller: {self.name}
# rating: {self.rating}
# items: {sum(self.products.values())}"""

# c = Customer("Ali", "ali@mail.com", "Toshkent", balance=2_000_000)

# c.add_to_cart("Keyboard", 1, 300_000)
# c.add_to_cart("Mouse", 2, 150_000)

# print(c.get_cart_total())
# print(c.checkout())
# print(c)


# s = Seller("Gulbahor", "g@mail.com", "Samarqand", rating=4.8)

# s.add_product("Keyboard", 10)
# s.update_stock("Keyboard", -3)

# print(s.get_stock())
# print(s)

# 2-masala

# class Person:
#     def __init__(self,name, id_number):
#         self.name=name
#         self.id=id_number

#     def get_name(self):
#         return f"{self.name}"

#     def get_id(self):
#         return f"{self.id}"

#     def __str__(self):
#         return f"""Person: {self.name} 
# id: {self.id}"""


# class Patient(Person):
#     def __init__(self, name, id_number,diagnoss=None, bill=0):
#         super().__init__(name, id_number)
#         self.bill=bill
#         self.diagnos=[] if diagnoss is None else diagnoss

#     def add_diagnosis(self, text: str) -> None:
#         self.diagnos.append(text)

#     def add_charge(self, amount: int) -> None:
#         try :
#             if amount<=0:
#                 raise ValueError("qiymat musbat bo'lshi kerak")
#             else:
#                 self.bill+=amount
#         except ValueError as xato:
#             print(xato)

#     def pay(self, amount: int) -> bool:
#         if amount>=self.bill:
#             self.bill=0
#             return True
#         else:
#             self.bill-=amount
#             return False
    
#     def get_balance(self) -> int:
#         return f"qarzdorlik: {self.bill}"

#     def print_history(self) -> None:
#         print(f"""tashxislar tarixi: {self.diagnos}
# qarzdorlik: {self.bill}""")

# class Doctor(Person):
#     def __init__(self, name, id_number, specialty,schedule=None):
#         self.specialty=specialty
#         self.schedule=[] if schedule is None else schedule
#         super().__init__(name, id_number)

#     def add_slot(self, day: str, time: str) -> None:
#         slot=(day,time)

#         if not slot in self.schedule:
#             self.schedule.append(slot)

#     def  book_slot(self, day: str, time: str) -> bool:
#         slot=(day,time)
#         if slot in self.schedule:
#             self.schedule.remove(slot)
#             return True
#         else:
#             return False

#     def available_slots(self, day: str) -> list[str]:
#         natija=[]
#         toplamlar= list(filter(lambda x: x[0]==day, self.schedule))
#         for toplam in toplamlar:
#             natija.append(toplam[1])
#         return natija
    
#     def __str__(self):
#         return f"""Dr.{self.name} - {self.specialty}"""


# p = Patient("Aziz", "AB1234567")
# p.add_diagnosis("ORVI")
# p.add_charge(150_000)
# p.add_charge(80_000)
# print(p.get_balance())  # 230000
# p.pay(100_000)
# print(p.get_balance())  # 130000
# p.print_history()

# d = Doctor("Gulrux", "CD7654321", specialty="Cardiologist")
# d.add_slot("Mon", "09:00")
# d.add_slot("Mon", "09:30")
# print(d.book_slot("Mon", "09:00"))  # True
# print(d.book_slot("Mon", "09:00"))  # False
# print(d.available_slots("Mon"))     # ["09:30"]
# print(d) # Dr.Gulrux (Cardiologist)


# 3-masala


class Course:
    def __init__(self, title, teacher, students=None):
        self.title = title
        self.teacher = teacher
        self.students = students if students is not None else []

    def get_title(self) -> str:
        return self.title

    def get_teacher(self) -> str:
        return self.teacher

    def enroll(self, student_name: str) -> bool:
        if student_name in self.students:
            return False
        else:
            self.students.append(student_name)
            return True

    def drop(self, student_name: str) -> bool:
        if student_name not in self.students:
            return False
        else:
            self.students.remove(student_name)
            return True

    def __str__(self):
        return f"Course: {self.title} ({self.teacher})"


class OnlineCourse(Course):
    def __init__(self, title, teacher, students=None, url="", max_students=0):
        super().__init__(title, teacher, students)
        self.url = url
        self.maxs = max_students

    def enroll(self, student_name: str) -> bool:
        if len(self.students) < self.maxs:
            return super().enroll(student_name)
        else:
            return False

    def get_room(self) -> str:
        return f"Virtual: {self.url}"


class OfflineCourse(Course):
    def __init__(self, title, teacher, students=None, room="", capacity=0):
        super().__init__(title, teacher, students)
        self.room = room
        self.capacity = capacity

    def enroll(self, student_name: str) -> bool:
        if len(self.students) < self.capacity:
            return super().enroll(student_name)
        else:
            return False

    def get_room(self) -> str:
        return f"Room: {self.room}"


# TEST

o = OnlineCourse(
    "Python Basics",
    "Guzal",
    url="https://nt.uz/py",
    max_students=2
)

print(o.enroll("Ali"))
print(o.enroll("Vali"))
print(o.enroll("Karim"))
print(o.get_room())

f = OfflineCourse(
    "Algorithms",
    "Dilshod",
    room="B-203",
    capacity=1
)

print(f.enroll("Soliha"))
print(f.enroll("Nodir"))
print(f.get_room())
print(f)




        
    