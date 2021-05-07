# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 61  # int(input())
extra_payment_end_month = 108  # int(input())
extra_payment = 1000  # float(input())


while principal > 0:
    if months == extra_payment_start_month:
        payment = payment + extra_payment
    if months == extra_payment_end_month + 1:
        payment = payment - extra_payment
    months = months + 1
    if payment > principal:
        payment = principal
        principal = 0
        total_paid = total_paid + payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

    print(f"{months:03} {round(total_paid, 2)} {round(principal, 2)}")
