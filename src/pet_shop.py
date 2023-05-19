# WRITE YOUR FUNCTIONS HERE
import pdb
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
# pdb.set_trace()
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,cash):
    # pdb.set_trace()
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sold):
    pet_shop["admin"]["pets_sold"] += sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_name):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_name:
            pets.append(pet)
    return pets
        







def find_pet_by_name(pet_shop, pet_name):
    # pdb.set_trace()
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        
    
