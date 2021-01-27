from matplotlib import pyplot as plt
import numpy as np
from helpers import actualValues
import pandas as pd


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


    xlim_l, xlim_r = 0,12 
    ylim_u, ylim_l = 6, 0
    #plt.yticks(range(-2,2))
    #plt.xticks(range(-4,4))
    # Plot figure for small resistance
    ax1 = plt.subplot(221)
    ax1.set_yticks(range(0,8))
    ax1.set_xticks(np.linspace(0, 10, 6))
    ax1.set_ylim(ylim_l, ylim_u)
    ax1.set_xlim(xlim_l, xlim_r)
    ax1.set_title("Small Resistor's voltage as a function of current")
    ax1.set_ylabel('Voltage (V)')
    ax1.set_xlabel('Current (mA)')
    ax1.grid(True)

    ax1.scatter(small_short_current, small_short_voltage)
    ax1.scatter(small_long_current, small_long_voltage)

    # Add best fit line using least square method
    # Reshape the array for numpy
    a1 = np.vstack([small_short_current, np.ones(len(small_short_current))]).T

    # Compute the slope and constant
    r = np.linalg.lstsq(a1, small_short_voltage, rcond=None)[0]
    ax1.plot(small_short_current, np.multiply(r[0], small_short_current)+r[1])

    # Reshape the array for numpy
    a1 = np.vstack([small_long_current, np.ones(len(small_long_current))]).T

    # Compute the slope and constant
    r = np.linalg.lstsq(a1, small_long_voltage, rcond=None)[0]
    ax1.plot(small_long_current, np.multiply(r[0], small_long_current)+r[1])

    # Plot figure for large resistance
    xlim_l, xlim_r = 0, 6
    ylim_u, ylim_l = 30, 15
    ax2 = plt.subplot(222)
    #plt.yticks(range(-2,2))
    #plt.xticks(range(-4,4))
    ax2.set_ylim(ylim_l, ylim_u)
    ax2.set_xlim(xlim_l, xlim_r)
    ax2.set_title("Large resistor's voltage as a function of current")
    ax2.set_ylabel('Voltage (V)')
    ax2.set_xlabel('Current (mA)')
    ax2.grid(True)

    ax2.scatter(large_short_current, large_short_voltage)
    ax2.scatter(large_long_current, large_long_voltage)

    # Add best fit line using least square method
    # Reshape the array for numpy
    b2 = np.vstack([large_short_current, np.ones(len(large_short_current))]).T

    # Compute the slope and constant
    r = np.linalg.lstsq(b2, large_short_voltage, rcond=None)[0]
    ax2.plot(large_short_current, np.multiply(r[0], large_short_current)+r[1],
            label = "Short coupling")

    b2 = np.vstack([large_long_current, np.ones(len(large_long_current))]).T
    # Compute the slope and constant
    r = np.linalg.lstsq(b2, large_long_voltage, rcond=None)[0]
    ax2.plot(large_long_current, np.multiply(r[0], large_long_current)+r[1],
            label = "Long coupling")

    # Plotting measured values ends here.
    # Start calculating the actual values.
    actual_small_short_current = []
    for i in range(0,5):
        actual_small_short_current.append(actualValues("short", "small", 
            small_short_current[i], small_short_voltage[i]))

    # Small, long coupling => Need to return the actual voltage
    actual_small_long_voltage =[]
    for i in range(0,5):
        actual_small_long_voltage.append(actualValues("long","small",
            small_long_current[i], small_long_voltage[i]))

    # Large, short coupling => Need to return the actual current
    actual_large_short_current = []
    for i in range(0,5):
        actual_large_short_current.append(actualValues("short", "large",
            large_short_current[i], large_short_voltage[i]))

    # Large, long coupling => Need to return the actual voltage
    actual_large_long_voltage = []
    for i in range(0,5):
        actual_large_long_voltage.append(actualValues("long", "large",
            large_long_current[i], large_long_voltage[i]))

    # For short couplings we use the measured voltage to derive the actual current.
    # For long couplings we use the measured current to derive the actual voltage.
    # Plot figure for actual values of the small resistor
    xlim_l, xlim_r = 0, 11
    ylim_u, ylim_l = 6, 0
    ax3 = plt.subplot(223)
    #plt.yticks(range(-2,2))
    #plt.xticks(range(-4,4))
    ax3.set_ylim(ylim_l, ylim_u)
    ax3.set_xlim(xlim_l, xlim_r)
    ax3.set_title("Actual small")
    ax3.set_ylabel('Voltage (V)')
    ax3.set_xlabel('Current (mA)')
    ax3.grid(True)

    ax3.scatter(actual_small_short_current, small_short_voltage)
    ax3.scatter(small_long_current, actual_small_long_voltage)

    # Plot figure for actual values of large resistor
    xlim_l, xlim_r = 0, 6
    ylim_u, ylim_l = 30, 15
    ax4 = plt.subplot(224)
    #plt.yticks(range(-2,2))
    #plt.xticks(range(-4,4))
    ax4.set_ylim(ylim_l, ylim_u)
    ax4.set_xlim(xlim_l, xlim_r)
    ax4.set_title("Actual large")
    ax4.set_ylabel('Voltage (V)')
    ax4.set_xlabel('Current (mA)')
    ax4.grid(True)

    ax4.scatter(actual_large_short_current, large_short_voltage,
            label = "Short coupling")
    ax4.scatter(large_long_current, actual_large_long_voltage,
            label = "Short coupling")

    ax2.legend(loc=0)
    ax4.legend(loc=0)
    plt.legend()

    small_short = np.vstack((actual_small_short_current, small_short_voltage))
    small_long = np.vstack((small_long_current, actual_small_long_voltage))
    large_short = np.vstack((actual_large_short_current, large_short_voltage))
    large_long= np.vstack((large_long_current, actual_large_long_voltage))

    print(small_short)
    print("")
    print(small_long)
    print("")
    print(large_short)
    print("")
    print(large_long)
    print("")

    #plt.show()
    
    ## Export data to csv
    df = pd.DataFrame(small_short)
    df.to_csv('file.csv',index=True)

if __name__ == "__main__":
    main()
