time_v = int(input("Введите время в секундах:"))

time_d = str(time_v // 86400).rjust(2, '0')
time_h = str((time_v % 86400) // 3600).rjust(2, '0')
time_m = str((time_v % 3600) // 60).rjust(2, '0')
time_s = str(time_v % 60).rjust(2, '0')

print(f"Время в формаде dd:hh:mm:ss: {time_d}:{time_h}:{time_m}:{time_s}.")