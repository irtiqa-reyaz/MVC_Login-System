from Model2 import data_store
from Controller2_demo import Credentials
class Users:
    username=""
    email=""
    ph=""
    residence=""
    acc=Credentials()
    def __init__(self):
        choice=float(input("Press\n1:-Search User\n2:-Register New User\n"))
        if choice==1:
            self.username=input("Enter your Name\t")
            login_store=data_store()
            login_store.setUsername(self.username)
            self.acc.check_login(login_store)
            #print(login_store.getReply())
        else:
            self.username=input("Enter your Username\t")
            self.residence=input("Enter your Residence\t")
            self.email=input("Enter your Email\t")
            self.ph=input("Enter your Contact\t")
            register=data_store()
            register.setUsername(self.username)
            register.setResidence(self.residence)
            register.setEmail(self.email)
            register.setContact(self.ph)
            self.acc.register_user(register)
    '''def display(self):
        print(self.username)
        print(self.password)'''
usr=Users()

