import datetime

class Addressbook:
    person_list = []

    def register(self,person):
        self.person_list.append(person)

    def show(self):
        for p in self.person_list:
            print(p.lastname)

    def search(self,key):
        for p in self.person_list:
            if key in p.lastname or key in p.firstname:
                print(p.firstname+"さんがヒットしました")
                
        

class User:
    lastname = ''
    firstname = ''
    phone_number =''
    mail_address = ''
    birthday = datetime.datetime(2000,1,1)

ab = Addressbook()

p1 = User()
p1.lastname='Isoda'
p1.firstname = 'Tomoki'
p1.phone_number = '000-000-0000'
p1.mail_address = 'a@a.com'
p1.birthday = datetime.datetime(1999,11,10)

p2 = User()
p2.lastname='Koyama'
p2.firstname = 'Luna'
p2.phone_number = '000-000-0001'
p2.mail_address = 'b@b.com'
p2.birthday = datetime.datetime(2001,4,11)

#リストに登録
ab.register(p1)
ab.register(p2)
#苗字を表示 
ab.show()

ab.search('Tomoki')