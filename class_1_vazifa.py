

# ------------------------- VAZIFA -------------------------------------

# class Kitob:
#     def kiritish(self):

#         self.nom=input("kitob nomini kiriting: ")
#         self.muallif=input("kitob muallifini kiriting: ")
#         self.narx=int(input("kitob narxini kiriting: "))
#         self.nashriyot=input("nashriyot: ")
#     def ochirish(self,x):
        
#             if x == "nom":
#                 del self.nom
#             elif x == "muallif":
#                 del self.muallif
#             elif x == "narx":
#                 del self.narx
#             elif x == "nashriyot":
#                 del self.nashriyot
    

# k1=Kitob()
# k2=Kitob()
# k3=Kitob()
# k4=Kitob()
# k5=Kitob()

# k1.kiritish()
# k2.kiritish()
# k3.kiritish()
# k4.kiritish()
# k5.kiritish()

# lst=[k1,k2,k3,k4,k5]

# for kitob in lst:
#      if "A"<= kitob.nashriyot[0].strip().upper() <="H":
#           print(kitob.nom,kitob.muallif,kitob.nashriyot,kitob.narx)
          

# 2-masala

# class Kompyuter:
#     def __init__(self,nom,ram,narx,protsessor):
#         self.nom=nom
#         self.ram=ram
#         self.protsessor=protsessor
#         self.narx=narx
#     def ochirish(self,x):
#         if x=="nom":
#             del self.nom
#         elif x=="ram":
#             del self.ram
#         elif x=="protsessor":
#             del self.protsessor
#         elif x=="narx":
#             del self.narx

# k1=Kompyuter()
# k2=Kompyuter()
# k3=Kompyuter()
# k4=Kompyuter()
# # k5=Kompyuter()

# # k5.ochirish("nom")
# # print(k5.nom)

# lst=[k1,k2,k3,k4]

# for kom in lst:
#     if 4<=kom.ram<=16:
#         print(f"{kom.nom} , {kom.ram} , {kom.protsessor} , {kom.narx}")

# 3-masala

class User:
    def __init__(self):
        self.nick=input("nick: ")
        self.aslIsm=input("Ism Familiya: ")
        self.email=input("email: ")
        self.yosh=int(input("yosh: "))
    def ochirish(self,x):
        if x=="nick":
            del self.nick
        elif x=="ism famiiliya":
            del self.aslIsm
        elif x=="email":
            del self.email
        elif x=="narx":
            del self.yosh
    def get_info(self):
        print(f"""Foydalanuvchi: {self.nick}
ismi: {self.aslIsm}
email: {self.email}
yosh: {self.yosh}""")

user1=User()

user1.get_info()

        
        


        








   
        



        










































