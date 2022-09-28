import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	if type(sentence) == str:
		for i in range(len(sentence)):
			if sentence[i] == "a":
				total += 1
		return total
	else:
		return 0


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		if item.name and item.price and item.stock and type(item.name) == str and type(item.price) == int and type(item.stock) == int:
			self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		if len(self.items) == 0:
			return None
		else:
			maxstock = self.items[0].stock
			maxstock_item = self.items[0]
			for x in range(1, len(self.items)):
				if maxstock < self.items[x].stock:
					maxstock = self.items[x].stock
					maxstock_item = self.items[x]
			return maxstock_item
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		if len(self.items) == 0:
			return None
		else:
			maxprice = self.items[0].price
			maxprice_item = self.items[0]
			for x in range(1, len(self.items)):
				if maxprice < self.items[x].price:
					maxprice = self.items[x].price
					maxprice_item = self.items[x]
			return maxprice_item	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)
		self.item6 = Item("", 0, 0)
		self.item7 = Item("Grape Faygo", 3, 60)
		self.item8 = Item("Lemonade", "5", 1.23)

		self.warehouse1 = Warehouse(items=[])
		self.warehouse2 = Warehouse(items=[])
		self.warehouse3 = Warehouse(items=[])

	## Check to see whether count_a works
	def test_count_a(self):
		#no a's, empty strings, single character, weird characters, case sensitivity, not string, etc
		self.assertEqual(count_a("hello this is my string"), 0, "string with no a's")
		self.assertEqual(count_a(""), 0, "empty string")
		self.assertEqual(count_a("a"), 1, "string with 1 a")
		self.assertEqual(count_a("𝒶𝒶𝓎𝒶𝓃𝒶"), 0, "string with weird characters")
		self.assertEqual(count_a("AAYANA"), 0, "string with uppercase 'A'")
		self.assertEqual(count_a(12345), 0, "not a string")


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		#empty items, check indexes, improper types
		self.warehouse1.add_item(self.item6)
		self.assertEqual(len(self.warehouse1.items),0 , "testing empty item")

		self.warehouse1.add_item(self.item1)
		self.warehouse1.add_item(self.item2)
		self.warehouse1.add_item(self.item3)
		self.assertEqual(len(self.warehouse1.items), 3, "testing adding 3 items")
		self.assertEqual(self.warehouse1.items[0], self.item1, "testing indexes")
		self.assertEqual(self.warehouse1.items[1], self.item2, "testing indexes")
		self.assertEqual(self.warehouse1.items[-1], self.item3, "testing indexes")

		self.warehouse2.add_item(self.item8)
		self.assertEqual(self.warehouse1.items[-1], self.item3, "testing improper type values")


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		#normal, tie, one item only, empty list
		self.assertEqual(self.warehouse2.get_max_stock(), None, "testing empty items list")
		self.warehouse2.add_item(self.item4)
		self.assertEqual(self.warehouse2.get_max_stock(), self.item4, "only 1 item in list")
		self.warehouse2.add_item(self.item5)
		self.assertEqual(self.warehouse2.get_max_stock(), self.item4, "testing normal max stocks")
		self.warehouse2.add_item(self.item7)
		self.assertEqual(self.warehouse2.get_max_stock(), self.item4, "testing tie values")

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		#tie, one item only, empty list
		self.assertEqual(self.warehouse3.get_max_price(), None, "testing empty items list")
		self.warehouse3.add_item(self.item4) #2
		self.assertEqual(self.warehouse3.get_max_price(), self.item4, "only 1 item in list")
		self.warehouse3.add_item(self.item5) #3
		self.assertEqual(self.warehouse3.get_max_price(), self.item5, "testing normal max price")
		self.warehouse3.add_item(self.item7) #3
		self.assertEqual(self.warehouse3.get_max_price(), self.item5, "testing tie values")
		

def main():
	unittest.main(verbosity=2)

if __name__ == "__main__":
	main()