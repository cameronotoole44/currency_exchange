class Currency:
    # Dictionary to hold currency conversion rates relative to USD
    currencies =  {
        'CHF': 0.930023,  # Swiss Franc
        'CAD': 1.264553,  # Canadian Dollar
        'GBP': 0.737414,  # British Pound
        'JPY': 111.019919,  # Japanese Yen
        'EUR': 0.862361,  # Euro
        'USD': 1.0        # US Dollar
    }
      
    def __init__(self, value, unit="USD"):
        """
        Initialize a Currency object with a value and unit.
        
        :param value: Amount of currency.
        :param unit: Currency unit (default is 'USD').
        """
        self.value = value
        self.unit = unit

    def __str__(self):
        """
        String representation of the Currency object, rounded to 2 decimal places.
        
        :return: Formatted string of value and unit.
        """
        return f"{round(self.value,2)} {self.unit}"

    def __repr__(self):
        """
        Official string representation of the Currency object, used for debugging.
        
        :return: Formatted string of value and unit.
        """
        return f"{round(self.value,2)} {self.unit}"

    def changeTo(self, new_unit):
        """
        Convert the Currency object to a new unit.
        
        :param new_unit: Target currency unit to convert to.
        """
        # Convert the value to the new unit by using the conversion rates
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):
        """
        Add two Currency objects or a Currency object and a numerical value.
        
        :param other: Currency object or numerical value to add.
        :return: A new Currency object with the result of the addition.
        """
        if isinstance(other, (int, float)):
            # If 'other' is a numerical value, treat it as USD
            x = other * Currency.currencies[self.unit]
        else:
            # Convert 'other' to the current unit before addition
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(x + self.value, self.unit)

    def __iadd__(self, other):
        """
        In-place addition with another Currency object or numerical value.
        
        :param other: Currency object or numerical value to add.
        :return: Self with updated value.
        """
        # Call the __add__ method and update self
        result = self + other
        self.value = result.value
        self.unit = result.unit
        return self

    def __radd__(self, other):
        """
        Right-hand addition for a Currency object and a numerical value.
        
        :param other: Numerical value to add to the Currency object.
        :return: Result of addition as a Currency object.
        """
        result = self + other
        if self.unit != "USD":
            result.changeTo("USD")
        return result

    def __sub__(self, other):
        """
        Subtract a Currency object or a numerical value from this Currency object.
        
        :param other: Currency object or numerical value to subtract.
        :return: A new Currency object with the result of the subtraction.
        """
        if isinstance(other, (int, float)):
            # If 'other' is a numerical value, treat it as USD
            x = other * Currency.currencies[self.unit]
        else:
            # Convert 'other' to the current unit before subtraction
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(self.value - x, self.unit)

    def __isub__(self, other):
        """
        In-place subtraction with another Currency object or numerical value.
        
        :param other: Currency object or numerical value to subtract.
        :return: Self with updated value.
        """
        # Call the __sub__ method and update self
        result = self - other
        self.value = result.value
        self.unit = result.unit
        return self

    def __rsub__(self, other):
        """
        Right-hand subtraction for a numerical value and this Currency object.
        
        :param other: Numerical value to subtract from the Currency object.
        :return: Result of subtraction as a Currency object.
        """
        # Subtract this value from 'other' and convert to current unit
        result = other - self.value
        result = Currency(result, self.unit)
        if self.unit != "USD":
            result.changeTo("USD")
        return result

# Example usage
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)  # Add two Currency objects
print(v2 + v1)  # Add two Currency objects (order swapped)
print(v1 + 3)   # Add a numerical value to a Currency object
print(3 + v1)   # Add a Currency object to a numerical value
print(v1 - 3)   # Subtract a numerical value from a Currency object
print(30 - v2)  # Subtract a Currency object from a numerical value