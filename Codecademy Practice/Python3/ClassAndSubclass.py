class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item

    def __repr__(self):
        return self


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * 0.001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * 0.00005


car = VehicleInsurance(10000)
print(car)