import re
def email_parser(email):
      
  key_former = ["user_name", "domain"]

  pattern = re.compile(r"(^[a-z][a-z0-9]+[+]?[a-z0-9]*@[a-z][a-z]+\.com$)")

  email_checker = pattern.search(email) 
  if email_checker != None:
        
      value_former = re.split('@',email)
      dict_formed = {keys:values for keys,values in zip(key_former,value_former)}
      #dict_form = {i:i+1 for i in len(key_former)}
      return dict_formed  

  
  return None

print(email_parser('grtyolam+@gmail.com'))



  