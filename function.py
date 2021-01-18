# Define some constants that we will use in the calculation
# Resistance of Volt-meter
R_v_small = 5000
R_v_large = 50000

# Resistance of Amp-meter
R_a_small = 308/15
R_a_large = 52.8

def shortCouplings(I_a, U, R_v):
    """
    This function returns the correct current flowing throught the resistor
    :param I_a: (mA) current of Amp-meter
    :param U: (V) votage of Volt-meter and resistor
    :param R_v: (Ohm) resistance of volt-meter
    :return: I (mA) current of resistor
    """
    I_a_amp = I_a * 1000
    I = I_a_amp - (U / R_v)
    I = I/1000
    return I

def longCouplings(U_v, I, R_a):
    """
    This function returns the correct voltage of the resistor
    :param U_v: (V) voltage of the Volt-meter
    :param I: (mA) current of the Ampe-meter and the resistor
    :param R_a: (Ohm) resistance of the Ampe-meter
    :return: U (V) voltage of the resistor
    """
    I_amp = I*1000
    U = U_v - (R_a * I_amp)
    return U

def actualValues(type_of_coupling, type_of_resistor, current, voltage):
    """
    This function takes a list of values, and return a list of real
    values, i.e actual voltage that flows in the resistor
    :param type_of_coupling: long or short coupling
    :param type_of_resistor: small or large resistor
    :param current: (mA) the current
    :param voltage: (V) the voltage
    :return: the value after calculation
    """
    if type_of_coupling == "long":
        if type_of_resistor == "small":
            # This case is long coupling, small resistor
            U = longCouplings(voltage, current, R_a_small)
            return U

        elif type_of_resistor == "large":
            # This case is long coupling, large resistor
            U = longCouplings(voltage, current, R_a_large)
            return U

    elif type_of_coupling == "short":
        if type_of_resistor == "small":
            # This case is short coupling, small resistor
            I = shortCouplings(current, voltage, R_v_small)
            return I

        elif type_of_resistor == "large":
            # This case is short coupling, large resistor
            I = shortCouplings(current, voltage, R_v_large)
            return I

def main:
    # Small, short coupling => Need to return the actual current
    actual_small_short_current = []
    for i in range(0,4):
        actual_small_short_current.append(actualValues("short", "small", small_short_current[i], small_short_voltage[i]))

    # Small, long coupling => Need to return the actual voltage
    actual_small_long_voltage =[]
    for i in range(0,4):
        actual_small_long_voltage.append(actualValues("long","small", small_long_current[i], small_long_voltage[i]))

    # Large, short coupling => Need to return the actual current
    actual_large_short_current = []
    for i in range(0, 4):
        actual_large_short_current.append(actualValues("short", "large", large_short_current[i], large_short_voltage[i]))

    # Large, long coupling => Need to return the actual voltage
    actual_large_long_voltage = []
    for i in range(0, 4):
        actual_large_long_voltage.append(actualValues("long", "large", large_long_current[i], large_long_voltage[i]))