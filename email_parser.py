import re


def email_parser(email):
      
  key_former = ["username", "domain"]

  pattern = re.compile(r"(^[a-zA-Z][a-zA-Z0-9]+[+]?[a-zA-Z][a-zA-Z0-9]+@[a-zA-Z]+[0-9]*\.com$)") #re pattern

  email_checker = pattern.search(email) 
  if email_checker != None:
        
      value_former = re.split('@',email)
      dict_formed = {keys:values for keys,values in zip(key_former,value_former)}
  
      return f"\n{dict_formed}\n"  

  
  return f"\n{None}\n"

print(email_parser('grtyobvbnb@gmail12.com'))





  