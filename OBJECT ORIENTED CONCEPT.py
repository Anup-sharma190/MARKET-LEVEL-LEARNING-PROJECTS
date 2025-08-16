"""
Cake Demo Project - Object Oriented Programming (OOP) in Python
---------------------------------------------------------------
This project demonstrates the concept of classes, objects, attributes,
and methods using a simple "Cake" example.

Skills Shown:
- Python class creation
- Object instantiation
- Instance attributes
- Method calling with 'self'
"""


# -------------------- Step 1: Define the Class --------------------
class Cake:
    """
    The Cake class represents a cake object that can have different flavors.
    """

    def set_flavor(self, flavor):
        """
        Assign a flavor to the cake.

        Parameters:
        flavor (str): The flavor name to set for this cake.
        """
        self.flavor = flavor  # 'self' refers to the object calling this method

    def show_flavor(self):
        """
        Return the flavor of the cake.
        """
        return self.flavor


# -------------------- Step 2: Create Cake Objects --------------------
cake1 = Cake()  # First cake object
cake2 = Cake()  # Second cake object

# -------------------- Step 3: Set Flavors --------------------
cake1.set_flavor("Chocolate")  # cake1 gets Chocolate
cake2.set_flavor("Vanilla")  # cake2 gets Vanilla

# -------------------- Step 4: Show Flavors --------------------
print("Cake 1 flavor:", cake1.show_flavor())
print("Cake 2 flavor:", cake2.show_flavor())

# Output:
# Cake 1 flavor: Chocolate
# Cake 2 flavor: Vanilla