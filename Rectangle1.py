class Rectangle():
    _count = 0   # Class variable to keep track of the number of Rectangle objects created
    def __init__(self, longueur = 0, largeur = 0):
        self.__longueur = longueur # Private instance variable for length
        self.__largeur = largeur# Private instance variable for width
        Rectangle._count += 1  # Increment the count of Rectangle objects

    def Getlongueur(self) :
        return self.__longueur  # Getter method for length
    
    def setlongueur(self, longueur) :
        self.__longueur = longueur  # Setter method for length

    def Getlargeur(self) :
        return self.__largeur  # Getter method for width
    
    def setlargeur(self, largeur) :
        self.__largeur = largeur # Setter method for width

    def Getcount(self) :
        return Rectangle._count   # Getter method for the count of Rectangle objects
    
    def Equals(self, Rec1) : # Check if the current Rectangle object is equal to another Rectangle object
        if self.__largeur == Rec1.__largeur and self.__longueur == Rec1.__longueur :
            return True
        else : 
            return False
        
    def Perimetre(self):
        P = (self.__largeur + self.__longueur) * 2 
        return P # Calculate and return the perimeter of the Rectangle
    
    def Surface(self) :
        return self.__largeur * self.__longueur # Calculate and return the surface area of the Rectangle
    
    def ToString (self) :
        return "Width :" + str(self.Getlargeur()) + ";  Length :" + str(self.Getlongueur()) +"; NbrRectangle :"+ str(self.Getcount()) +"."
    
class Parallelepipede (Rectangle) :
    _count1 = 0  # Class variable to keep track of the number of Parallelepipede objects created
    def __init__(self, longueur = 0, largeur = 0, hauter = 0 ):
        super().__init__(longueur, largeur) # Call the constructor of the base class (Rectangle)
        self.__hauter = hauter  # Private instance variable for height
        Parallelepipede._count1 += 1 # Increment the count of Parallelepipede objects

    def Gethauter(self) :
        return self.__hauter  # Getter method for height
    
    def sethauter(self, hauter) :
        self.__hauter = hauter  # Setter method for height

    def Getcount1(self) :
        return Parallelepipede._count1   # Getter method for the count of Parallelepipede objects

    def Equals(self, par) :   # Check if the current Parallelepipede object is equal to another Parallelepipede object
        if self.Getlargeur() == par.Getlargeur() and self.Getlongueur() == par.Getlongueur() and self.__hauter == par.__hauter :
            return True
        else : 
            return False
        
    def Surface(self):
        return (super().Surface() + self.__hauter * self.Getlargeur() + self.__hauter * self.Getlongueur())*2
        # Calculate and return the surface area of the Parallelepipede
    def ToString (self) :
        return "Width :" + str(self.Getlargeur()) + ";  Length :" + str(self.Getlongueur())+ "; height :"+ str(self.Getcount1()) +"; NbrParallelepipede :"+ str(self.Getcount()) +"."
    
    def Volume (self) :
        return  self.Getlargeur() * self.Getlongueur() * self.__hauter
        # Calculate and return the volume of the Parallelepipede