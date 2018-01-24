class Bicycle():
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
        
class BicycleShop(Bicycle):
    def __init__(self, name, inventory, mark_up):
        self.name = name
        self.inventory = inventory
        self.mark_up = mark_up
        
        
    def inv_dict (self):
        model_dict={}
        for index in range (len(self.inventory)):
            model_dict[self.inventory[index].model]=round(self.inventory[index].cost*self.mark_up,2)
        return (model_dict)
        
    def carrying_cost (self):
        inventory_value=0
        cost_dict={}
        for index in range (len(self.inventory)):
            cost_dict[self.inventory[index].model]=self.inventory[index].cost
        
        for values in cost_dict:
            inventory_value += cost_dict[values]
        
        print(self.name, '-Total Inventory Value- $',round(inventory_value,2))
    
    def remove_bike (self,bike_model):
        for index in range (len(self.inventory)):
            if bike_model == self.inventory[index].model:
                pass
                

class Customers():
    def __init__(self, name, savings, bikes):
        self.name = name
        self.savings = savings
        self.bikes = bikes  
