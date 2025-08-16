# -----------------------------------------------------------------------------
# Project: Cake Constructor Demo
# Author: Anup Sharma
# Purpose: Demonstrate how to use __init__ (constructor) in Python classes.
# Skills: Python OOP, Constructors, Objects, Attributes
# -----------------------------------------------------------------------------

class Cake:
    """
    A simple Cake class to demonstrate the __init__ constructor method.
    When we create a Cake object, it is automatically given a flavor.
    """

    def __init__(self, flavor):
        """
        Constructor method (__init__):
        Called automatically when a new Cake object is created.
        'self.flavor' stores the flavor of the cake.
        """
        self.flavor = flavor

    def show_flavor(self):
        """
        Returns the flavor of this cake.
        """
        return f"This cake's flavor is {self.flavor}."


# --------------------------- DEMO USAGE --------------------------------------
# Creating cake objects with flavors
cake1 = Cake("Chocolate")   # flavor set at creation time
cake2 = Cake("Vanilla")
cake3 = Cake("Strawberry")

# Displaying the flavors
print(cake1.show_flavor())  # Output: This cake's flavor is Chocolate.
print(cake2.show_flavor())  # Output: This cake's flavor is Vanilla.
print(cake3.show_flavor())  # Output: This cake's flavor is Strawberry.
