from Rectangle1 import Rectangle, Parallelepipede   # Import Rectangle and Parallelepipede classes from Rectangle1 module
import copy
rec0 = Rectangle()  # Create a default Rectangle object
rec1 = Rectangle(12, 5)  # Create a Rectangle object with specific dimensions (length=12, width=5)
recc = copy.copy(rec1)  # Create a shallow copy of the rec1 object using copy.copy()

# Test the Equals method to check if rec0 is equal to rec1
print(rec0.Equals(rec1))
# Print the perimeter of rec0, rec1, and recc
print("Permitre is :", rec0.Perimetre())
print("Permitre is :", rec1.Perimetre())
print("Permitre is :", recc.Perimetre())
# Print the surface area of rec0 and recc
print("Surface is :", rec0.Surface())
print("Surface is :", recc.Surface())
print("Surface is :", recc.Surface())
# Print the string representation of rec0, rec1, and recc
print(rec0.ToString())
print(rec1.ToString())
print(recc.ToString())


par0 = Parallelepipede()  # Create a default Parallelepipede object
par1 = Parallelepipede(12, 5, 12)   # Create a Parallelepipede object with specific dimensions (length=12, width=5, height=12)
parc = copy.copy(par1)  # Create a shallow copy of the par1 object using copy.copy()

# Test the Equals method to check if rec0 is equal to rec1 (should be False for different classes)
print(par0.Equals(par1))
# Print the volume of par0, par1, and parc
print("Volume is :", par0.Volume())
print("Volume is :", par1.Volume())
print("Volume is :", parc.Volume())
# Print the surface area of par0, par1, and parc
print("Surface is :", par0.Surface())
print("Surface is :", par1.Surface())
print("Surface is :", parc.Surface())
# Print the string representation of par0, par1, and parc
print(par0.ToString())
print(par1.ToString())
print(parc.ToString())

