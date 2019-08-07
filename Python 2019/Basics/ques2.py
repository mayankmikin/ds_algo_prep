prices = [1,3,3,2,5]
#prices = [5,1,3,4,6,2]

def get_min(arr):
    print('remaining list is:')
    print(arr)
    return min(arr)


if __name__ == '__main__':
    final_price = 0
    items_purchased_at_Full_price = []
    for i in range(0, len(prices)):
        # for first element
        if(i==len(prices)-1):
            start=i
        else:
            start=i+1

        sub_lst = prices[start:len(prices)]
        min_val = get_min(sub_lst)
        #print('i is : ', i, ' current item value is ', prices[i])
        print('min of rest of array is: ', min_val)
        if(prices[i]) > min_val:
            if(i+1<len(prices) and prices[i]!=prices[i+1]):
                val_to_add = prices[i] - min_val
                print('for item',prices[i],' value to add ', val_to_add)
                final_price += val_to_add
        elif (prices[i])==min_val:
            if (i==len(prices)-1):
                print('for item',prices[i],' value to add WITH FULL PRICE', prices[i])
                items_purchased_at_Full_price.append(i)
                final_price += prices[i]
            else:
                val_to_add = prices[i] - min_val
                print('for item',prices[i],' value to add ', val_to_add)
                final_price += val_to_add
        else:
            if(i+1<len(prices) and prices[i]==prices[i+1]):
                print('CURRENT ITEM EQUALS TO RIGHT ONE ')
            print('for item',prices[i],' value to add WITH FULL PRICE', prices[i])
            items_purchased_at_Full_price.append(i)
            final_price += prices[i]

    print('final price is: ', final_price)
    print(final_price)
    print('indices of full price items: ')
    for i in items_purchased_at_Full_price:
        print(i),
    # print(items_purchased_at_Full_price)
