from collections import Counter
from itertools import product


if __name__ == '__main__':

    # myList = ["mayank","mayank","verma","mayank","something"]
    # print Counter(myList)
    # print Counter(myList).items()
    # print Counter(myList).keys()
    # print Counter(myList).values()
    total_shoes = int(input())
    shoes= map(int,input().split())
    total_price=0
    shoe_map=Counter(shoes)
    #print (shoe_map)
    n=int(input())
    for index in range (0,n) :
        size,price=map(int,input().split())
    # add price in total_price and remove from the shoe_map
        if(size in shoe_map):

            if(int(shoe_map[size])>0):
                shoe_map[size]= int(shoe_map[size])-1
                total_price+=price

    #print (shoe_map)
    #print ('total_price is:')
    print (total_price)
