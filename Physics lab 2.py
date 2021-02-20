import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Constant as data measured
# List of all currents in the measurements
currents =      [1.0, 1.2, 1.4, 1.8, 2.0]
# List of all voltages in the measurements
Voltage =        [300, 280, 260, 240, 220, 200]

# Lists of radii
Current_1 =     [107, 102, 96, 88, 82, 75]
Current_1_2 =   [91, 86, 83, 76, 67, 61]
Current_1_4 =   [76, 75, 70, 65, 57, 55]
Current_1_6 =   [73, 69, 63, 60, 57, 51]
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
            r = df[current][i].item()
            I = current
            processed_data[current].append(specific_charge(U, r/2, I, K_r))
            #print("Voltage = ", U)
            #print("Radius = ", r)
            #print("Current = ", I)
            #print("______________________")

    new_data = {'Voltage': Voltage,
                1.0: processed_data[1.0],
                1.2: processed_data[1.2],
                1.4: processed_data[1.4],
                1.6: processed_data[1.6],
                1.8: processed_data[1.8],
                2.0: processed_data[2.0]}

    new_df = pd.DataFrame(new_data)
    return new_df
def list_of_values(df):
    processed_df_values = df.values.tolist()
    processed_list = []
    for list in processed_df_values:
        for value in list:
            processed_list.append(value)
    return processed_list


def main():
    measured_data = {'Voltage': Voltage,
                     1.0: Current_1,
                     1.2: Current_1_2,
                     1.4: Current_1_4,
                     1.6: Current_1_6,
                     1.8: Current_1_8,
                     2.0: Current_2_0}

    raw_df = pd.DataFrame(measured_data)
    print(raw_df)

    error_K_r = 3.8e-6
    K_r = (0.7444 / 1000)

    processed_df = data_processing(raw_df, K_r)

    K_r += error_K_r
    processed_df_plus = data_processing(raw_df, K_r)

    K_r -= error_K_r
    processed_df_minus = data_processing(raw_df, K_r)

    print(processed_df)

    #for i in range(0,7):
        #print(processed_df.iloc[:, i])

    processed_df_values = processed_df.drop(['Voltage'], axis = 1)
    processed_df_minus_values = processed_df_minus.drop(['Voltage'], axis = 1)
    processed_df_plus_values = processed_df_plus.drop(['Voltage'], axis = 1)

    processed_list = list_of_values(processed_df_values)
    #processed_list = list_of_values(processed_df_minus_values)
    #processed_list = list_of_values(processed_df_plus_values)

    plt.hist(processed_list, bins = 6, edgecolor = 'black')
    plt.xlabel('Ratio (C/kg)')
    plt.ylabel('Frequency (pcs)')

    min_val = min(processed_list)
    max_val = max(processed_list)
    interval = abs((max_val - min_val) / 6)
    print('Interval = ', interval)
    print("The min value is: ", min_val)
    print("The max value is: ", max_val)
    print("The intervals are: ")
    for i in range(0,6):
        print(i+1, min_val + i*interval,"-", min_val + (i+1)*interval)
    print("Based on the histogram, the value of the ratio is:",
          (405839774165.4295 + 361495916626.323)/2, "+-", 405839774165.4295-(405839774165.4295 + 361495916626.323)/2)

    plt.show()

if __name__ == "__main__":
    main()