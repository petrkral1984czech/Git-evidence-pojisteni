Class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class CarFactory:
    def create_felicia(self):
        return Car("Škoda", "Felicia")
factory = CarFactory()
felicia = factory.create_felicia()