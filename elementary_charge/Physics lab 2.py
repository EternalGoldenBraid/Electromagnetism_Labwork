import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.show()

# Constant as data measured
# List of all currents in the measurements
currents =      [1.0, 1.2, 1.4, 1.8, 2.0]
# List of all voltages in the measurements
Voltage =        [300, 280, 260, 240, 220, 200]

# Lists of radii
Current_1 =     [107, 102, 96, 88, 82, 75]
Current_1_2 =   [91, 86, 83, 76, 67, 61]
Current_1_4 =   [76, 75, 70, 65, 57, 55]
Current_1_8 =   [66, 63, 60, 56, 49, 43]
Current_2_0 =   [63, 60, 58, 56, 50, 45]

def specific_charge(voltage, radius, current, K_r):
    I = current
    U = voltage
    r = radius/(1000)
    B = I*(K_r)
    ratio = (2*U)/(r*r*B*B)
    return ratio

def data_processing(df, K_r):
    processed_data = {}

    currents = [1, 1.2, 1.4, 1.6, 1.8, 2.0]

    for current in currents:
        processed_data[current] = []
        for i in range(0, 6):
            U = df.iloc[i, 0].item()
            r = df.iloc[i, 1].item()
            I = (1.0)
            processed_data[current].append(specific_charge(U, r, I, K_r))

    new_data = {'Voltage': Voltage,
                1.0: processed_data[1.0],
                1.2: processed_data[1.2],
                1.4: processed_data[1.4],
                1.6: processed_data[1.6],
                1.8: processed_data[1.8],
                2.0: processed_data[2.0]}

    new_df = pd.DataFrame(new_data)
    return new_df


def main():
    measured_data = {'Voltage': Voltage,
                     1.0: Current_1,
                     1.2: Current_1_2,
                     1.4: Current_1_4,
                     1.8: Current_1_8,
                     2.0: Current_2_0}

    raw_df = pd.DataFrame(measured_data)
    print(raw_df)

    error_K_r = 3.8e-6
    K_r = (0.7444 / 1000)

    processed_df = data_processing(raw_df, K_r)
    print(processed_df)

    K_r += error_K_r
    processed_df_plus = data_processing(raw_df, K_r)
    print(processed_df_plus)

    K_r -= error_K_r
    processed_df_minus = data_processing(raw_df, K_r)
    print(processed_df_minus)

if __name__ == "__main__":
    main()