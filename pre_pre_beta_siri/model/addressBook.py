"""
Модель зберігання/пошуку контактів.
"""
from collections import UserDict
from .record import Record
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def find(self, name:str)->Record:
        item = self.data.get(name)
        if(item is None):
            return None
        return item
    
    def delete(self, name:str):
        if name in self.data:
            del self.data[name]
        else:
            raise Exception("Can't find item: " + name)
        
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        now = datetime.today().date()

        for key, item in self.data.items():
            if(item.birthday is None):
                continue
            original_birthday = item.birthday.value
            
            birthday_this_year = original_birthday.replace(year=now.year)
            
            is_birthday_yesterday_but_sunday_today = (now.weekday() == 6) and (now == birthday_this_year + timedelta(days=1))

            if birthday_this_year < now:
                birthday_this_year = birthday_this_year.replace(year=now.year + 1)
            
            till_birthday_days = (birthday_this_year - now).days

            congratulation_date = None
            if (0 <= till_birthday_days <= 7):
                congratulation_date = birthday_this_year

                if birthday_this_year.weekday() in (5,6): #saturday, sunday
                    days_till_monday = 7 - birthday_this_year.weekday()
                    congratulation_date = birthday_this_year + timedelta(days=days_till_monday)
               
            elif is_birthday_yesterday_but_sunday_today:
                congratulation_date = now + timedelta(days=1)
            else:
                continue
           
            upcoming_birthdays.append({
                'name': key,
                'congratulation_date': congratulation_date.strftime("%d.%m.%Y")
            })
        
        return upcoming_birthdays

    def get_birthdays_till_date(self, days_till: int):
        contacts = []
        today = datetime.today()
        for key, item in self.data.items():
            if item.birthday is None:
                continue
            original_birthday = item.birthday.value
            birthday_this_year = original_birthday.replace(year=today.year)
            diff = today.date() - birthday_this_year
            if (0 >= diff.days and abs(diff.days) < days_till) or (0 < diff.days and (365 - diff.days) < days_till):
                contacts.append(item)
        if len(contacts) == 0:
            return f"No contacts found with birthday in {days_till} days."
        contact_strings = [str(record) for record in contacts]
        result = "\n".join(contact_strings)
        return result