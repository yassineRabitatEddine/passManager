from getpass import getpass
import datasource



while True:
    choice=int(input("""Choose one option from the menu below : \n
                     1.Sign up\n
                     2.Sign in\n
                     3.Quit\n
                     >>>"""))
    
    
    if choice==1:
        print("**** Sign Up ****\n")
        username=input("Username : ")
        password=getpass("Password : ")
        u=datasource.User(username,password)
        if u.addUser()==True:
            print("User registred")
        else:
            print("This username is already taken !")
            
    elif choice==2:
        print("*** Sign In ***\n")
        username=input("Username : ")
        password=getpass("Password : ")
        u=datasource.User(username,password)
        if u.authenticate()==1:
            print(f"\tHi {username} !")
            while True:
                choice2=int(input("""Choose one option from the menu below : \n
                        1.Add password\n
                        2.Update password\n
                        3.Delete password\n
                        4.Get password\n
                        5.List all passwords\n
                        6.Return to the main pannel\n
                        >>>"""))
                
                if choice2==1:
                   print("Add password :\n")
                   website=input("Website : ")
                   password2=getpass("Password : ")
                   p=datasource.Password(website)
                   if p.addPassword(password2)==True:
                      print("Password registred.")
                   else:
                       print("Website password already exists !")
                       
                elif choice2==2:
                    print("Update password")
                    website=input("Website : ")
                    password2=getpass("New password : ")
                    p=datasource.Password(website)
                    p.updatePassword(password2)
                   
                elif choice2==3:
                    print("Delete password : ")
                    website=input("Website : ")
                    p=datasource.Password(website)
                    p.deletePassword()
                    print("Password deleted")
                    
                elif choice2==4:
                    print("Get password : ")
                    website=input("Website : ")
                    p=datasource.Password(website)
                    if(p.getPassword())==False:
                        print("No such password !")
                    else:
                        print("Password copied to clipboard !")
                        
                elif choice2==5:
                    print("List all passwords")
                    s=u.listPasswords()

                else:
                    break  
                
        else:
            print("No such user exists !")
            
    else:
        break
datasource.conn.close()
