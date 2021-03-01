
import numpy as np

values = []
index = 0

# Running average function
def avg_vals(values,index):
    values = np.array(values)
    avg_values = np.sum(values)/(index+1)
    return avg_values

# Running standard deviation function
def std_vals(values,avg_vals,index):
    means = np.repeat(avg_vals,index+1)
    diffs = np.array(values) - means
    std_vals = np.sum((diffs**2)/(index+1))
    std_vals = np.sqrt(std_vals)
    return std_vals

# Running median function
def median_vals(values,index):
    values = np.array(values)
    values = np.sort(values)

    if index +1 == 1:
        median_vals = values[0]
    elif (index+1)%2 == 1:
        upper_index = int(np.ceil((index+1)/2))
        median_vals = values[upper_index-1]
    else:
        new_index = int((index+1)/2)
        median_vals = (values[new_index-1]+values[new_index])/2
    return median_vals

# Input precision of values
while True:
    precision = input("Input the precision you want for your values\n")
    try:
        precision = int(precision)
    except ValueError as e:
        print("Value Error: Enter another percision")
    if True:
        break
# Main loop for calculating running summary statistics
while True:
    data = input("Type Exit to close \n\nPlease enter a Value:\n")
    if 'Exit' == data:
        break
    try:
        # Change string input to float
         data = float(data)

         # Append float values to list
         values.append(data)

        # Call functions for running summary statistics and modify precision
         run_avg = round(avg_vals(values,index),precision)
         run_std = round(std_vals(values,run_avg,index),precision)
         run_median = round(median_vals(values,index),precision)

         # Print results
         print(run_avg,run_std,run_median)
         index +=1
    except ValueError as e:
        print ('Value Error: Enter another value')
    
print("Done")
