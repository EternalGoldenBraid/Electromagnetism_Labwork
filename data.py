from matplotlib import pyplot as plt
import numpy as np

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


def main():

    # Voltages in volts.
    small_short_voltage = [1.0, 2.0, 3.0, 4.0, 5.0]
    small_long_voltage =  [1.0, 2.0, 3.0, 4.0, 5.0]
    large_short_voltage = [16.0, 19.0, 22.0, 25.0, 28.0]
    large_long_voltage =  [16.0, 19.0, 22.0, 25.0, 28.0]

    # Currents in milliamperes
    small_short_current = [1.8, 4.0, 6.0, 8.0, 10.1]
    large_short_current = [2.61, 3.18, 3.66, 4.18, 4.73]
    small_long_current = [1.6, 3.4, 5.1, 6.8, 8.7]
    large_long_current = [2.28, 2.71, 3.18, 3.61, 4.15]

    # Plot figure for small resistance
    ax1 = plt.subplot(121)
    ax1.set_yticks(range(0,5))
    ax1.set_xticks(np.linspace(0, 10, 6))
    ax1.set_ylim(0, 5)
    ax1.set_xlim(0, 10)
    ax1.set_title("Resistor's voltage as a function of current")
    ax1.set_ylabel('Voltage (V)')
    ax1.set_xlabel('Current (mA)')
    ax1.grid(True)

    ax1.scatter(small_short_current, small_short_voltage)
    ax1.scatter(small_long_current, small_long_voltage)

    # Add best fit line using least square method
    # Reshape the array for numpy
    a1 = np.vstack([small_short_current, np.ones(len(small_short_current))]).T
    print(a1)

    # Compute the slope and constant
    r = np.linalg.lstsq(a1, small_short_voltage)[0]
    ax1.plot(small_short_current, np.multiply(r[0], small_short_current)+r[1])

    # Plot figure for large resistance
    ax2 = plt.subplot(122)
    #plt.yticks(range(-2,2))
    #plt.xticks(range(-4,4))
    ax2.set_ylim(0, 30)
    ax2.set_xlim(0, 6)
    ax1.set_title("Resistor's voltage as a function of current")
    ax2.set_ylabel('Voltage (V)')
    ax2.set_xlabel('Current (mA)')
    ax2.grid(True)

    ax2.scatter(large_short_current, large_short_voltage)
    ax2.scatter(large_long_current, large_long_voltage)

    # Add best fit line using least square method
    # Reshape the array for numpy
    a2 = np.vstack([large_short_current, np.ones(len(large_short_current))]).T
    b2 = np.vstack([large_short_current, np.ones(len(large_short_current))]).T

    # Compute the slope and constant
    r = np.linalg.lstsq(b2, large_short_voltage)[0]
    ax2.plot(large_short_current, np.multiply(r[0], large_short_current)+r[1])

    plt.show()

if __name__ == "__main__":
    main()
