import datetime

class AddressBook:
    person_list = []

    def add(self,person):
        self.person_list.append(person)
    
    def show(self):
        print("------name information-------")
        for person in self.person_list:
            print(person.lastname+" "+person.firstname)
            
    
    def serch(self,key):
        print("------hit information-------")
        for person in self.person_list:
            if key in person.firstname or key in person.lastname:
                print(person.lastname+" "+person.firstname)


class Person:

    firstname = "" #名前
    lastname = "" #苗字
    phone_number = "" #電話番号
    mail_address = "" #メールアドレス
    birthday = datetime.datetime(2000,11,10) #誕生日


p1 = Person()
p1.firstname = "Tomoki"
p1.lastname = "Isoda"
p1.phone_number = "000-000"
p1.mail_address = "a@a.com"
p1.birthday = datetime.datetime(1999,11,10)

p2 = Person()
p2.firstname = "Luna"
p2.lastname = "Koyama"
p2.phone_number = "111-111"
p2.mail_address = "b@b.com"
p2.birthday = datetime.datetime(2001,4,11)

ab = AddressBook()

ab.add(p1)
ab.add(p2)

print("アドレス帳の人数: "+str(len(ab.person_list)))

ab.show()
ab.serch('Tomoki')

