class Currency:
    # dictionary to hold currency conversion rates relative to USD
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
        string representation of the Currency object, rounded to 2 decimal places.
        
        :return: formatted string of value and unit.
        """
        return f"{round(self.value,2)} {self.unit}"

    def __repr__(self):
        """
        official string representation of the Currency object, used for debugging.
        
        :return: formatted string of value and unit.
        """
        return f"{round(self.value,2)} {self.unit}"

    def changeTo(self, new_unit):
        """
        convert the Currency object to a new unit.
        
        :param new_unit: target currency unit to convert to.
        """
        # convert the value to the new unit by using the conversion rates
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):
        """
        add two Currency objects or a Currency object and a numerical value.
        
        :param other: Currency object or numerical value to add.
        :return: a new Currency object with the result of the addition.
        """
        if isinstance(other, (int, float)):
            # if 'other' is a numerical value, treat it as USD
            x = other * Currency.currencies[self.unit]
        else:
            # convert 'other' to the current unit before addition
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(x + self.value, self.unit)

    def __iadd__(self, other):
        """
        in-place addition with another Currency object or numerical value.
        
        :param other: Currency object or numerical value to add.
        :return: self with updated value.
        """
        # call the __add__ method and update self
        result = self + other
        self.value = result.value
        self.unit = result.unit
        return self

    def __radd__(self, other):
        """
        right-hand addition for a Currency object and a numerical value.
        
        :param other: numerical value to add to the Currency object.
        :return: result of addition as a Currency object.
        """
        result = self + other
        if self.unit != "USD":
            result.changeTo("USD")
        return result

    def __sub__(self, other):
        """
        subtract a Currency object or a numerical value from this Currency object.
        
        :param other: Currency object or numerical value to subtract.
        :return: a new Currency object with the result of the subtraction.
        """
        if isinstance(other, (int, float)):
            # if 'other' is a numerical value, treat it as USD
            x = other * Currency.currencies[self.unit]
        else:
            # convert 'other' to the current unit before subtraction
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(self.value - x, self.unit)

    def __isub__(self, other):
        """
        in-place subtraction with another Currency object or numerical value.
        
        :param other: Currency object or numerical value to subtract.
        :return: Self with updated value.
        """
        # call the __sub__ method and update self
        result = self - other
        self.value = result.value
        self.unit = result.unit
        return self

    def __rsub__(self, other):
        """
        right-hand subtraction for a numerical value and this Currency object.
        
        :param other: numerical value to subtract from the Currency object.
        :return: result of subtraction as a Currency object.
        """
        # subtract this value from 'other' and convert to current unit
        result = other - self.value
        result = Currency(result, self.unit)
        if self.unit != "USD":
            result.changeTo("USD")
        return result