from machine_data import resources
from machine_data import MENU
from machine_data import COIN

def resource_check(resources, menu, choice):
    
    if resources["coffee"]>=MENU[choice]["ingredients"]["coffee"]:
        switch=1
    else: 
        switch=0
        print("Sorry we are running low on resources!")
        return switch
    
    if resources["water"]>=MENU[choice]["ingredients"]["water"]:
        switch=1
    else: 
        switch=0
        print("Sorry we are running low on resources!")
        return switch
    
    if resources["milk"]>=MENU[choice]["ingredients"]["milk"]:
        switch=1
    else:
        switch=0
        print("Sorry we are running low on resources!")
        return switch
    return switch

def machine_processing(resources, MENU, choice):
    final_coffee=resources["coffee"]-MENU[choice]["ingredients"]["coffee"]
    resources["coffee"]=final_coffee
    final_water=resources["water"]-MENU[choice]["ingredients"]["water"]
    resources["water"]=final_water
    final_milk=resources["milk"]-MENU[choice]["ingredients"]["milk"]
    resources["milk"]=final_milk


def coin_processing(COIN, MENU, choice):
    profit=0
    print("\nPlease insert coins.")
    quarters=int(input("How many Quarters: "))
    dimes=int(input("How many Dimes: "))
    nickels=int(input("How many Nickels: "))
    pennies=int(input("How many Pennies: "))
    total=(COIN["penny"]*pennies) + (COIN["nickel"]*nickels) + (COIN["dime"]*dimes) + (COIN["quarter"]*quarters)
    total=round(total,2)
    if MENU[choice]["cost"]<=total:
        profit+=MENU[choice]["cost"]
        change=round(total-MENU[choice]["cost"],2)
        print("Here is your coffee! ☕")
        print(f"Here is ${change} in change")
        return profit
    else: 
        print("Sorry that's not enough money, Money Refunded!")
        profit=False
        return profit