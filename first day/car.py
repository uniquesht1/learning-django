class Car:
    mileage = 17

    def __init__(self, mileage, brand):
        print("congrats you brought a car")
        self.mileage = mileage
        self.brand = brand

    def start(self):
        print(
            "Brand : ",
            self.brand,
            "vrooooom",
            "your car will run for",
            self.mileage,
            "\n",
        )


yuc = Car(mileage=17, brand="suzuki")

# print(yuc.mileage)

yuc.start()
yufc = Car(mileage=19, brand="honda")
# print(yufc.mileage)
yufc.start()


class Car4WD(Car):
    def start(self):
        # super().start()
        print("vrooooom with 4 wheels\n")


class ElectricCar(Car):
    def start(self):
        print("suiiiisuiiiii with battery power\n")


yuc = Car4WD(mileage=20, brand="kamasitu")
yuc.start()

yufc = ElectricCar(mileage=15, brand="Tesla")
yufc.start()
