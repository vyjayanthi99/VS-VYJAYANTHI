# define a static variable and access that through a instance.

class number:
# access through a instance  
  static_variable = 10


instance = number()
instance.static_variable=15

print(instance.static_variable)