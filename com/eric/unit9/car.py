class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def getName(self):
		return str(self.year) + " " + self.make + " " + self.model

	def update_odometer_reading(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def ubcrenebr_odometer(self, miles):
		self.odometer_reading += miles

	def fill_gas_tank(self):
		print("fill gas")


newCar = Car('audi', 'A4', 2016)
print(newCar.getName())
print(newCar.odometer_reading)
newCar.update_odometer_reading(250)
print(newCar.odometer_reading)
newCar.update_odometer_reading(50)
print(newCar.odometer_reading)


class Battery:
	def __init__(self, bettery_size=70):
		self.battery_size = bettery_size

	def describe_battery(self):
		print("this car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		print("This car doesn't need a gass tank")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.getName() + "   ")
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
