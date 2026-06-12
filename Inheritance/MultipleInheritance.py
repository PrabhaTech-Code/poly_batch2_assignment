class Father:
    def bike(self):
        print("Father has a bike")
    
    def money(self):
        print("Father has 20 Lakhs in his bank account")


class Mother:
    def car(self):
        print("Mother has a car")

class Son(Father, Mother):
    def cycle(self):
        print("Son has a cycle")


# f = Father()
# f.bike()

# m = Mother()
# m.car()

s = Son()
s.cycle()
s.bike()
s.money()
s.car()