class car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  
  def move(self):
    print("Start") 

class Honda(car):
  pass

class Toyota(car):
  pass

car1 = car("Ford", "Mustang" , "2009")       
car2=  Honda ("Civic", "Touring 20", "2023") 
car3= Toyota("Fortuner", "747", "2024")  

print(car1.make,",", car1.model,"," , car1.year)
car1.move()
print(car2.make,",", car2.model, ",",car2.year)
car2.move()
print(car3.make,",", car3.model,",", car3.year)
car3.move()

