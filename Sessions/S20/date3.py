import time

ev1 = "20-02-2023 10:11"
ev2 = "22-02-2023 12:45"

ev_tm1 = time.strptime(ev1, "%d-%m-%Y %H:%M")
ev_tm2 = time.strptime(ev2, "%d-%m-%Y %H:%M")

delta_min = ev_tm2.tm_min - ev_tm1.tm_min
delta_h = (ev_tm2.tm_hour - ev_tm1.tm_hour) * 60
delta_d = (ev_tm2.tm_mday - ev_tm1.tm_mday) * 60 * 24

print(delta_h + delta_d + delta_min)