
from resource_deco import resource_deco
 

@resource_deco(email="folorunso@decadev.com", password="decagon123")
def resource():
    '''This function returns business logic of our company'''
    return "This is the company most valuable resource"


print(resource())
