
with open('efficiency.txt', 'r') as file:
    efficiency = [float(line.strip()) for line in file]

with open('shifts.txt', 'r') as file:
    shifts = [line.strip() for line in file]

print("Efficiency:", efficiency)
print("Shifts:", shifts)

import numpy as np
np_shifts = np.array(shifts)
print("Numpy Shifts Array:", np_shifts)
print("Dtype of np_shifts:", np_shifts.dtype)

np_efficiency = np.array(efficiency)
print("Numpy Efficiency Array:", np_efficiency)
print("Dtype of np_efficiency:", np_efficiency.dtype)

morning_efficiency = np_efficiency[np_shifts == 'Morning']
morning_avg = morning_efficiency.mean()
print("Average Efficiency (Morning):", morning_avg)

other_efficiency = np_efficiency[np_shifts != 'Morning']
other_avg = other_efficiency.mean()
print("Average Efficiency (Other Shifts):", other_avg)
