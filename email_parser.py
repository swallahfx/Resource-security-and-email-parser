import re


def email_parser(email):
      
  key_former = ["username", "domain"]

  pattern = re.compile(r"(^[a-z][a-z0-9]+[+]?[a-z][a-z0-9]+@[a-z]+[0-9]*\.com$)") #re pattern

  email_checker = pattern.search(email) 
  if email_checker != None:
        
      value_former = re.split('@',email)
      dict_formed = {keys:values for keys,values in zip(key_former,value_former)}
  
      return f"\n{dict_formed}\n"  

  
  return f"\n{None}\n"

print(email_parser('grtyolamgee655fgf+bvbnb@gmail12.com'))





  