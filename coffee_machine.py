from machine_data import resources
from machine_data import MENU
from machine_data import COIN
import machine_functions as mf

profit=0
flag=True
while flag:
    choice=input("​What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="espresso":
        switch=mf.resource_check(resources, MENU, choice)
        if switch==1:
            profit_per_transaction=mf.coin_processing(COIN, MENU, choice)
            if profit_per_transaction!=False:
                mf.machine_processing(resources, MENU, choice)
                profit+=profit_per_transaction
       

    elif choice=="latte":
        switch=mf.resource_check(resources, MENU, choice)
        if switch==1:
            profit_per_transaction=mf.coin_processing(COIN, MENU, choice)
            if profit_per_transaction!=False:
                mf.machine_processing(resources, MENU, choice)
                profit+=profit_per_transaction

    elif choice=="cappuccino":
        switch=mf.resource_check(resources, MENU, choice)
        if switch==1:
            profit_per_transaction=mf.coin_processing(COIN, MENU, choice)
            if profit_per_transaction!=False:
                mf.machine_processing(resources, MENU, choice)
                profit+=profit_per_transaction

    elif choice=="off":
        print("Turning off the machine!")
        flag=False

    elif choice=="report":
        print(f'''
        \n Water: {resources["water"]} 
        \n Milk: {resources["milk"]} 
        \n Coffee: {resources["coffee"]} 
        \n Money: ${profit} 
        \n''')

    else:
        print("Wrong Choice please enter again!")
