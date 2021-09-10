#!/usr/bin/python3

# Calculate when you get to a target ARR

from typing import Counter


mrr_current = int(input("Insert MMR 0: "))
mrr_previous = int(input("Insert MRR -1: "))
incr_percentuale = int(((mrr_current - mrr_previous) / mrr_previous) * 100)
print("Percentage increase: ", incr_percentuale)
counter = 0
objective_raw = int(input("Inserisci il valore obiettivo in migliaia (k): "))
objective = objective_raw * 1000
tmp = mrr_current

while (tmp*12 <= objective):
    tmp = tmp + (tmp * (incr_percentuale / 100))
    counter = counter + 1

print("Con una crescita mensile percentuale di ", incr_percentuale,
      " raggiungerai l'obbiettivo di ", objective, " in ", counter, " mesi.\n")
