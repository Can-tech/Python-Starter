import time
import sys
milk_amount=1000
water_amount=2000
coffee_amount=100
espresso_price=1.5
latte_price=2.5
cappuccino_price=3

def coffe_order():
    choose=input("What would you like? (espresso/latte/cappuccino): ")
    if(choose=="espresso"):
        print("espresso price is, ", espresso_price,"$")
        balance=get_money()
        use_ingredients("espresso")
        balance_left=charge_coffe_price(balance,espresso_price)
        if(balance_left!=False):
            make_coffee()
            coffe_order()
        else:
            coffe_order()
    elif(choose=="latte"):
        print("latte price is, ", latte_price,"$")
        balance=get_money()
        use_ingredients("latte")
        balance_left=charge_coffe_price(balance,latte_price)
        if(balance_left!=False):
            make_coffee()
            coffe_order()
        else:
            coffe_order()
    elif(choose=="cappuccino"):
        print("cappucino price is, ", cappuccino_price,"$")
        balance=get_money()
        use_ingredients("cappuccino")
        balance_left=charge_coffe_price(balance,cappuccino_price)
        if(balance_left!=False):
            make_coffee()
            coffe_order()
        else:
            coffe_order()
    elif(choose=="report"):
        print("Ingredients left: ")
        print("Milk: ", milk_amount,"ml")
        print("Water: ", water_amount,"ml")
        print("Coffee: ", coffee_amount,"g")
        coffe_order()


def get_money():
    """Returns Total Money put in the machine"""
    print("Put your money in the machine: ")
    total_money=0
    quarter_amount=float(input("Put your Quarters: "))
    total_money+=0.25*quarter_amount
    print("Balance: ", total_money)

    dime_amount=float(input("Put your Dimes: "))
    total_money+=0.1*dime_amount
    print("Balance: ", total_money,"$")

    nickel_amount=float(input("Put your nickels: "))
    total_money+=0.05*nickel_amount
    print("Balance: ", total_money,"$")

    penny_amount=float(input("Put your pennies: "))
    total_money+=0.01*penny_amount
    print("Total Balance: ", total_money,"$")
    return total_money
def charge_coffe_price(balance, coffee_price):
    if(balance>=coffee_price):
        print("Your order is set.")
        return balance-coffee_price
    else:
        print("Not Enough money ! Money refunding...")
        return False
def make_coffee():
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("Coffee preparing...")
    time.sleep(3)
    print("\nDone!")
def use_ingredients(product):
    global water_amount
    global coffee_amount
    global milk_amount
    if(product=="espresso"):
        water_amount-=50
        coffee_amount-=20
    elif(product=="latte"):
        water_amount-=100
        milk_amount-=100
        coffee_amount-=15
    elif(product=="cappuccino"):
        water_amount-=130
        milk_amount-=70
        coffee_amount-=20
    else:
        return False




coffe_order()