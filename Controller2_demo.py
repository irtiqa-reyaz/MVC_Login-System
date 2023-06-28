from MyDatabase_connection import DBConnection
class Credentials:
    
    '''def isValid(self,object_from_model):
        if object_from_model.getUsername()!="":
            return True
        else:
            return False
        pass
    def isAuthentic(self,object_from_model):
        db_obj=DBConnection()
        ack_from_DB=db_obj.checkUser(object_from_model,0)
        return ack_from_DB'''
    def isAvailable(self,object_from_model2):
        db_obj=DBConnection()
        ack_from_DB=db_obj.checkUser(object_from_model2,0)
        return ack_from_DB
    
    def check_login(self,object_from_model2):
        if self.isAvailable(object_from_model2):
            will=input("\t\t\t\t\tEnter \nI:- UPDATE INFORMATION\t\t\t OR\t\t\t\tD:- DELETE USER\n")
            if will=='I':
                choose=input("\t\t\t\t\tEnter \na:-Name Change\t b:-Residence Change\t c:-Email Change\td:-Contact Change\n")
                db_obj=DBConnection()
                db_obj.updateUser(choose,object_from_model2)
            if will=='D':
                #delchoose=input("\n\t\t\t\t\tOR\n\n\n\t\t\t\t\t\t\tEnter \ndelete:-Delete User")
                db_obj=DBConnection()
                db_obj.deleteUser(will,object_from_model2)
            
        else:
            print("Information not available ")
        
            
            
       # else:object_from_model.setReply("Username not Available")

    def register_user(self,object_from_modelR):
        db_obj=DBConnection()
        ack=db_obj.addUser(object_from_modelR)
        if ack==1:
            db_obj.checkUser(object_from_modelR,ack)
            print("Your Information has been Saved Succesfully!")
        
        
                
            
        
