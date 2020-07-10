# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# BASE CLASS
class Vehicle:
    pass

# Ground Vehicle Subclass
class GroundVehicle(Vehicle):
    pass

# Subclasses of Ground Vehicle
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# Flight Vehicle Subclass
class FlightVehicle(Vehicle):
    pass

# Subclasses of Flight Vehicle
class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass