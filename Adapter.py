from AbstractFactory import Rugs

class PriceAdapter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        return self.rate * product._price
    

if __name__ == "__main__":
    r1 = Rugs('persian rug', 20)
    r2 = Rugs('nain rug', 18)
    r3 = Rugs('morrocco rug', 15)

    rugs = [r1, r2, r3]

    adapter = PriceAdapter(100000)

    for rug in rugs:
        print(f"{rug._name}: {adapter.exchange(rug)}")