from bicycles import Bicycle
from bicycles import Customers
from bicycles import BicycleShop

def affordable_bikes(customer,bike_shop):
    '''
    looks at a bike shops inventory and determins which bikes the customer can affordable_bikes
    '''
    
    new_dict=bike_shop.inv_dict()
    print('With a budget of $', customer.savings)
    print(customer.name,'can afford the following bikes at', str(bike_shop.name)+':')
    for key,value in new_dict.items():
        if value > customer.savings:
            pass
        else:
            print('*',key, ': $', value)
           
    
def purchase_bike(customer,bike_shop):
    '''
    removes bike from store inventory, and places it in customer inventory.  savings will be adjusted
    '''
    #place all dictionary values in a list
    sort_price_lst=[]
    affordable_dict={}
    new_dict=bike_shop.inv_dict()
    for key,value in new_dict.items():
        if value > customer.savings:
            pass
        
        else:
            sort_price_lst.append(value)
            
    #pick the most expensive affordable bike, and deduct the cost from the customers savings        
    sort_price_lst.sort(reverse=True)   
    customer.savings=round(customer.savings-sort_price_lst[0],2)
    
    # add the bike to the customers inventory, and remove it from the bike shops inventory
    for key,value in new_dict.items():
        if value == sort_price_lst[0]:
            customer.bikes.append(key)
            del new_dict[key]
            print('')
            print('Congrats', customer.name, ' You just bought the', customer.bikes[0], 'for $', value )
            print('You have $', customer.savings, 'remaining in your savings')
            
            #remove bike from bikeshop inventory -not complete
            bike_shop.remove_bike(key)
            break
        
        else:
            pass
    
def inventory_cost(bike_shop):
    '''
    returns the total cost of a bike shops bike inventory
    '''
    bike_shop.carrying_cost()
    print(bike_shop.inv_dict())



# Define Class instances:

bike_1 = Bicycle('Mojo HD', 19, 800.01)
bike_2 = Bicycle('Stumt Jumper', 24, 120.01)
bike_3 = Bicycle('Super Fly',20, 805.01)
bike_4 = Bicycle('Enduro', 22, 400.01)
bike_5 = Bicycle('Singletrack', 27, 121.01)
bike_6 = Bicycle('Nomad',23, 350.01)
lst=[bike_1, bike_2, bike_3, bike_4, bike_5, bike_6]

customer_1 = Customers('Mike', 200, [])
customer_2 = Customers('Drew', 500, [])
customer_3 = Customers('Vince', 1000, [])


bike_shop_2 = BicycleShop('Bike World',[bike_1, bike_2, bike_3, bike_4, bike_5, bike_6], 1.20)


#Main Code
if __name__ =='__main__': 
    inventory_cost(bike_shop_2)
    print('')
    affordable_bikes(customer_1,bike_shop_2)
    print('')
    affordable_bikes(customer_2,bike_shop_2)
    print('')
    affordable_bikes(customer_3,bike_shop_2)
    purchase_bike(customer_1,bike_shop_2)
    purchase_bike(customer_2,bike_shop_2)
    purchase_bike(customer_3,bike_shop_2)