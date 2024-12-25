import numpy as np

np.random.seed(42) 

temperatures = np.round(np.random.uniform(15, 35, size=30), 2)
print("Dữ liệu nhiệt độ trong tháng:", temperatures)

mean_temperature = np.mean(temperatures)
print("Nhiệt độ trung bình trong tháng:", round(mean_temperature, 2), "độ C")

max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
max_day = np.argmax(temperatures) + 1 
min_day = np.argmin(temperatures) + 1

print(f"Ngày có nhiệt độ cao nhất là ngày {max_day} với {max_temp} độ C.")
print(f"Ngày có nhiệt độ thấp nhất là ngày {min_day} với {min_temp} độ C.")

temperature_diff = np.abs(np.diff(temperatures))
max_diff = np.max(temperature_diff)
max_diff_day = np.argmax(temperature_diff) + 1 

print(f"Ngày có sự biến đổi nhiệt độ cao nhất là ngày {max_diff_day} với mức chênh lệch {max_diff:.2f} độ C.")

above_20 = np.where(temperatures > 20)[0] + 1
print("Các ngày có nhiệt độ trên 20 độ C:", above_20)

specific_days = [5, 10, 15, 20, 25]
specific_temps = temperatures[np.array(specific_days) - 1]
print("Nhiệt độ các ngày 5, 10, 15, 20, 25:", specific_temps)

above_avg_days = np.where(temperatures > mean_temperature)[0] + 1
above_avg_temps = temperatures[temperatures > mean_temperature]
print("Các ngày có nhiệt độ trên trung bình:", above_avg_days)
print("Nhiệt độ tương ứng:", above_avg_temps)

even_days = temperatures[1::2]
odd_days = temperatures[0::2] 

print("Nhiệt độ các ngày chẵn:", even_days)
print("Nhiệt độ các ngày lẻ:", odd_days)

