
from resource_deco import resource_deco
email = input("please input your email address: ")
password = input("please input your password: ")

@resource_deco(email, password)
def resource():
    '''This function returns business logic of our company'''
    return "This is the company most valuable resource"


print(resource())
