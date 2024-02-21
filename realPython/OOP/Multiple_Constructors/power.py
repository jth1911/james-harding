# power.py

class CumulativePowerFactory:
    def __init__(self, exponent=2, *, start=0):
        """
         Initialize the object with exponent and start value. This is useful for debugging and to ensure that the object is not re - initialized after a test is run
         
         @param exponent - exponent of the test default is 2
         @param start - value to start the test with default is 0
        """
        self._exponent = exponent
        self.total = start

    def __call__(self, base):
        """
         Calculates the power of the given base and adds it to the total. This is useful for testing purposes
         
         @param base - The base to calculate the power of
         
         @return The power of the given base after the exponent has
        """
        power = base ** self._exponent
        self.total += power
        return power
