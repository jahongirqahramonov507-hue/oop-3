class MyDate:

    MONTHS = [
        "Yanvar", "Fevral", "Mart", "Aprel",
        "May", "Iyun", "Iyul", "Avgust",
        "Sentabr", "Oktabr", "Noyabr", "Dekabr"
    ]

    DAY_IN_MONTHS = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]
 
    def __init__(self, day, month, year):
        

        if not 1 <= year <= 9999:
            raise ValueError("Noto'g'ri sana kiritildi!")

        if not 1 <= month <= 12:
            raise ValueError("Noto'g'ri sana kiritildi!")

        days = self.isLeapYear(year)

        if not 1 <= day <= days[month - 1]:
            raise ValueError("Noto'g'ri sana kiritildi!")

        self.__day = day
        self.__month = month
        self.__year = year
    def isLeapYear(self, year):
        days=self.DAY_IN_MONTHS.copy()

        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days[1] = 29

        return days
    def setDate(self,day,month,year):
        days=self.DAY_IN_MONTHS[month - 1]
        if month < 1 or month > 12:
            raise ValueError("Oy noto'g'ri")

        if day < 1 or day> days:
            raise ValueError("Kun noto'g'ri")

        self.__day = day
        self.__month = month
        self.__year = year
        
        
    def nextDay(self):
        days=self.isLeapYear(self.__year)
        if self.__day == days[self.__month - 1]:
             self.__month+=1
             self.__day=1
             
        elif self.__month==12 and self.__day==31:
             self.__year+=1
             self.__day=1
             self.__month=1
        else:
             self.__day+=1
    def previousDay(self):
        if self.__day==1 and not self.__month==1 :
            self.__month-=1

            self.__day=self.DAY_IN_MONTHS[self.__month-1]

        elif self.__day==1 and self.__month==1:
             self.__year-=1
             self.__day=31
             self.__month=12

        else:
             self.__day-=1

        return f"{self.__day}.{self.__month}.{self.__year}"
    def nextMonth(self):
        if self.__month==12:
              self.__year+=1
              self.__month=1
        self.__month+=1
        return f"{self.__day}.{self.__month}.{self.__year}"
    def previousMonth(self):
        if self.__month==1:
              self.__month=1
              self.__year-=1
        else:
             self.__month-=1
        return f"{self.__day}.{self.__month}.{self.__year}"

    def nextYear(self):
        self.__year+=1
        return f"{self.__day}.{self.__month}.{self.__year}"

    def previousYear(self):
        self.__year-=1
        return f"{self.__day}.{self.__month}.{self.__year}"
    def __str__(self):
        name_month=self.MONTHS[self.__month-1]
        return f"{self.__day}-{name_month} {self.__year}-yil"

        
         
# sana = MyDate(15, 6, 2023)
# sana.nextDay()
# print(sana)  # 16-Iyun 2023 yil

# sana = MyDate(30, 4, 2023)
# sana.nextDay()
# print(sana)  # 01-May 2023 yil

# sana = MyDate(31, 12, 2023)
# sana.nextDay()
# print(sana)  # 01-Yanvar 2024 yil

# sana = MyDate(1, 5, 2023)
# sana.previousDay()
# print(sana)  # 30-Aprel 2023 yil

# sana = MyDate(28, 2, 2024)
# sana.nextDay()
# # print(sana)  # 29-Fevral 2024 yil


# sana = MyDate(29, 2, 2024)
# sana.nextDay()
# print(sana)  # 01-Mart 2024 yil

# sana = MyDate(28, 2, 2023)
# sana.nextDay()
# print(sana)  # 01-Mart 2023 yil

# sana = MyDate(1, 1, 2023)
# sana.previousDay()
# print(sana)  # 31-Dekabr 2022 yil

# try:
#     sana = MyDate(15, 6, 10000)
# except ValueError as e:
#     print(e)  # Noto'g'ri sana kiritildi!

# try:
#     sana = MyDate(15, 13, 2023)
# except ValueError as e:
#     print(e)  # Noto'g'ri sana kiritildi

# try:
#     sana = MyDate(32, 5, 2023)
# except ValueError as e:
#     print(e)  # Noto'g'ri sana kiritildi!

# sana = MyDate(15, 6, 2023)
# sana.setDate(5, 7, 2023)
# print(sana)  # 05-Iyul 2023 yil

try:
    sana = MyDate(15, 6, 2023)
    sana.setDate(31, 4, 2023)
except ValueError as e:
    print(e)  # Noto'g'ri sana kiritildi!