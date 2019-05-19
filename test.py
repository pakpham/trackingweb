import csv

class member:
        """docstring for member"""
        def __init__(self):
                super(member, self).__init__()
                self.id = "0"
                self.phone = "NOT FOUND"
                self.add = "NOT FOUND"
                self.name = "NOT FOUND"
                self.age = "NOT FOUND"
                self.fb = "NOT FOUND"
                self.mail = "NOT FOUND"
                self.link = "NOT FOUND"
        def showInfo(self):
                print('==========================================')
                print("================   INFO  =================")
                print("Name:            " , self.name)
                print("Phone Number:", self.phone)
                print("Year born:   ", self.age)
                print("Email:           ", self.mail)
                print("Address:     ", self.add)
                print("Facebook:    ", self.fb)
                print('==========================================')
                print('==========================================')
                pass
        def __repr__(self):
                return (self.__dict__)

member = member()


with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['id','name', 'age', 'phone','add','mail','fb','link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(member.__repr__())

# print ((member.__repr__()))