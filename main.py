#Taken from Codecademy lesson on Python 3
#Basic snippet of a class creation involving a menu section with a start and end time (i.e. breakfast, lunch, dinner)
#
class Menu:
  #class constructor
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

#Brunch menu  (dictionary of the various items and their respective prices)
brunch_items = {
   'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

#Class Object Instantiation?
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print statement for items on the new brunch_menu object
print(brunch_menu.items)

#Early Bird Special (new dictionary of menu items and price for the early beird time block)
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu('Early Bird Special', early_bird_items, 1500, 1800)

#Dinner menu

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu('Dinner Menu', dinner_items, 1700, 2300)

#Am I going to add anything new to test the update results?
