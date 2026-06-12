class GrandParent:
    def display_grandparent(self):
        print(f"(Grandparent) I have 15 Lakhs in my bank account.")

class Parent(GrandParent):
    def display_parent(self):
        print(f"(Parent) I have 20 Lakhs in my bank account.")

class Child(Parent):
    def display_child(self):
        print(f"(Child) I have 25 Lakhs in my bank account.")


# gp = GrandParent()
# gp.display_grandparent()

# p = Parent()
# p.display_grandparent()
# p.display_parent()

c = Child()
c.display_grandparent()
c.display_parent()
c.display_child()