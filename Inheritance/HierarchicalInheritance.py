#     A
#    / \
#   B   C

#    Father
#   /   \
#  Son   Daughter

class Father:
    def money(self):
        print("Father has 20 Lakhs in his bank account")

    def bike(self):
        print("Father has a bike")

class Son(Father):
    def cycle(self):
        print("Son has a cycle")

class Daughter(Father):
    def dress(self):
        print("Daughter has a dress")


# f = Father()
# f.money()

# s = Son()
# s.cycle()
# s.money()
#s.bike()

d = Daughter()
d.dress()
d.money()
d.bike()