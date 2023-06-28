import mysql.connector
class DBConnection:
    def __init__(self):
        self.DB_Conn=mysql.connector.connect(host="localhost",user="root",password="",database="datadb")
        self.permission=self.DB_Conn.cursor()
       #print("DB CONNECTED")
    def checkUser(self,object_from_model2,ack):
        usr=object_from_model2.getUsername()
        RSD=object_from_model2.getResidence()
        PH=object_from_model2.getContact()
        EM=object_from_model2.getEmail()
        if ack==0:
            query="select * from login where username='"+usr+"'"
            self.permission.execute(query)
            #abc=self.permission.fetchall()
            abc=self.permission.fetchone()
            if abc!=None:
                print("Name:-"+abc[0]+"")
                print("Residence:-"+abc[1]+"")
                print("Email:-"+abc[2]+"")
                print("Contact:-"+abc[3]+"")
                return True
            else:
                return False
                
            
            #for row in abc:
            #if abc!=None:
               # return True
            #else:
                #return False
            #for row in abc:
               # print(row)
                #print("\n")
        else:
            query="insert into login values('"+usr+"','"+RSD+"','"+EM+"','"+PH+"');"
            self.permission.execute(query)
            self.DB_Conn.commit()
            abc=self.permission.fetchone()
            if abc != None:
                return True
            else:
                return False
        
    def addUser(self,object_from_model2):
        USR=object_from_model2.getUsername()
        RSD=object_from_model2.getResidence()
        PH=object_from_model2.getContact()
        EM=object_from_model2.getEmail()
        query="insert into register values('"+USR+"','"+RSD+"','"+EM+"','"+PH+"');"
        self.permission.execute(query)
        self.DB_Conn.commit()
        return 1
        
            
            
        
    def updateUser(self,choose,object_from_model2):
        #? object dena haina jisme naya email etc likha hoga
        #object two types ke h >?
        #condition hogi object.username
        
        if choose=='a':
            new=input("Enter new Name:-")
            #query="UPDATE login SET username = 'aaaaaaaaaaaa' WHERE username = 'C'"
            query="UPDATE login SET username='"+new+"' WHERE username='"+object_from_model2.getUsername()+"'"
            self.permission.execute(query)
            self.DB_Conn.commit()
            print("Your Name has been changed")

        if choose=='b':
            new=input("Enter new Residence:-")
            query="UPDATE login SET residence='"+new+"' WHERE username='"+object_from_model2.getUsername()+"'"
            self.permission.execute(query)
            self.DB_Conn.commit()
            print("Your Residence has been changed")

        if choose=='c':
            new=input("Enter new Email:-")
            query="UPDATE login SET email='"+new+"' WHERE username='"+object_from_model2.getUsername()+"'"
            self.permission.execute(query)
            self.DB_Conn.commit()
            print("Your Email has been changed")

        if choose=='d':
            
            new=input("Enter new Contact:-")
            query="UPDATE login SET contact='"+new+"' WHERE username='"+object_from_model2.getUsername()+"'"
            self.permission.execute(query)
            self.DB_Conn.commit()
            print("Your Contact has been changed")
        
    
            
        
    def deleteUser(self,will,object_from_model2):
        if will=='D':
            query= "DELETE FROM login WHERE username='"+object_from_model2.getUsername()+"'"
            self.permission.execute(query)
            self.DB_Conn.commit()
            print("User has been Deleted succesfully!")
       
        
    
