from datetime import datetime, timedelta

now = datetime.now()

ev1 = datetime(1998, 6, 12)

print(f'I was born on {ev1.strftime("%A")}')

delta = now - ev1

print(f"Au trecut {delta.days} zile de la nasterea mea.")
print(f"Au trecut {delta.total_seconds()} secunde de la nasterea mea.")