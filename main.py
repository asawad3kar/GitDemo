# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from os import system
from coffee_resources import resources, MENU, moneylist


def get_machine_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


def refill():
    for each_r in resources:
        if each_r != "money":
            resources[each_r] += 100


def ask_user_choice():

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice.startswith("e"):
        return "espresso"
    elif user_choice.startswith("l"):
        return "latte"
    elif user_choice.startswith("c"):
        return "cappuccino"
    elif user_choice == "report":
        get_machine_report()
        return "report"
    elif user_choice == "refill":
        refill()
        return "refill"
    elif user_choice == "off":
        return "off"

    else:
        print("Kindly select your drink from the menu")


def money_calculator(_user_coins, _each_form):
    if _each_form == "quarters":
        return _user_coins * 0.25
    elif _each_form == "dimes":
        return _user_coins * 0.10
    elif _each_form == "nickels":
        return _user_coins * 0.05
    elif _each_form == "pennies":
        return _user_coins * 0.01


def update_resources(_user_selected_drink):
    for key_ in MENU[_user_selected_drink]["ingredients"]:
        if key_ in resources:
            resources[key_] -= MENU[_user_selected_drink]["ingredients"][key_]
    resources["money"] += MENU[_user_selected_drink]["cost"]


def ask_user_to_pay(_user_selected_drink, user_paid):
    for each_form in moneylist:
        user_coins = float(input(f"how many {each_form}?: "))
        user_paid += money_calculator(user_coins, each_form)
        if user_paid == MENU[_user_selected_drink]["cost"]:
            break
        elif user_paid > MENU[_user_selected_drink]["cost"]:
            user_refund = round(user_paid - MENU[_user_selected_drink]["cost"],2)
            print(f"{_user_selected_drink} costs ${MENU[_user_selected_drink]['cost']}"
                  f"Here is ${user_refund} refund.")
            print(f"Here is your {_user_selected_drink} ☕️. Enjoy!")
            update_resources(_user_selected_drink)
            break
    if user_paid < MENU[_user_selected_drink]["cost"]:
        print(f"Not enough money. Please pay {MENU[_user_selected_drink]['cost'] - user_paid} more")
        ask_user_to_pay(_user_selected_drink, user_paid)


def check_drink_resources(_user_selected_drink):
    print(f"Welcome, You have selected {_user_selected_drink}")
    refill_resource_list = []
    for drink_resource in resources:
        if drink_resource in MENU[user_selected_drink]["ingredients"]:
            if not resources[drink_resource] >= MENU[user_selected_drink]["ingredients"][drink_resource]:
                refill_resource_list.append(drink_resource)
    if len(refill_resource_list) != 0:
        print(f"Sorry cannot make you {user_selected_drink}")
        for each_item in refill_resource_list:
            print(f"I need {MENU[user_selected_drink]['ingredients'][each_item]}ml to make it and I have"
                  f" only {resources[each_item]}ml left.")
    else:
        user_paid = 0
        ask_user_to_pay(_user_selected_drink, user_paid)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm0')
    resources["money"] = 0
    coffee_machine_on = True
    while coffee_machine_on:
        user_selected_drink = ask_user_choice()
        if user_selected_drink == "report" or user_selected_drink == "refill":
            pass
        elif user_selected_drink != "off":
            check_drink_resources(user_selected_drink)
        elif user_selected_drink == "off":
            coffee_machine_on = False
