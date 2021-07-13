from auth import authenticate
from datetime import datetime


raw_time = datetime.now()
date_now = raw_time.strftime('%D')
time_now = raw_time.strftime('%H:%M:%S')
final_time =f"{date_now} at {time_now}"

def resource_deco(email='example@email.com', password='example123'):
      
   def new_deco(func):
         user = authenticate(email, password)
         def wrapper_func():
               
              if user:
                    if user['role'] == "admin" or user['role'] =="superadmin":
                        func()
                        grant_access = f"\n{user['first_name']} {user['last_name']} \n{func()}\n"
                        with open('access_granted.txt', 'a') as write_in:
                          write_in.write(f"{user['first_name']} {user['last_name']} viewed company resources on {final_time}\n")
                          return grant_access

                    elif user['role'] != "admin" or user['role'] != "superadmin":
                          denied_access = f"\n{user['first_name']} {user['last_name']} you are not allowed to view this resource\n"
                          with open('access_denied.txt', 'a') as write_in:
                            write_in.write(f"{user['role']} {user['first_name']} {user['last_name']} tried to view most valuable resources on {final_time}\n")
                          return denied_access         
              else:
                    return "\nonly staff can access this resource\n"

         return wrapper_func 
   return new_deco        





