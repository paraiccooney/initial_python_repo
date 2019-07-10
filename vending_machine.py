from byotest import *

usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

def getChange(amount, coins=eur_coins):
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
    return change
    

#here we expect that when there is 0 change to be given we will have an empty list
test_are_equal(getChange(0),[])
test_are_equal(getChange(1),[1])
test_are_equal(getChange(2),[2])
test_are_equal(getChange(50),[50])
test_are_equal(getChange(3),[2,1])
test_are_equal(getChange(7),[5,2])
test_are_equal(getChange(9),[5,2,2])
test_are_equal(getChange(35, usd_coins),[25,10])

print("All tests passed!")