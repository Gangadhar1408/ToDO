class Mobile():
    def __init__(self, size, loc, noofhouse, builder):
        self.prop_size = size
        self.location = loc
        self.house_left = int(noofhouse)
        self.builder = builder
        print("Houses Before: ",self.house_left)

    def buy_house(self,cust_name):
        print("Congratulations", cust_name, "You have bought house", self.prop_size, "House no", self.house_left, "Built by: ", self.builder)
        self.house_left -= 1
        print("Houses Left: ",self.house_left)

build_mgr1 = Mobile("2000sqft", "Blore", "200", "Suraj")
build_mgr2 = Mobile("1000sqft", "blg", "100", "POOL")
build_mgr3 = Mobile("500sqft", "mlore", "10", "kIIRR")

build_mgr1.buy_house("tuncan")
build_mgr2.buy_house("Loolll")
build_mgr2.buy_house("Mannnn")
build_mgr3.buy_house("Aiiiis")
build_mgr3.buy_house("Muuurrrr")