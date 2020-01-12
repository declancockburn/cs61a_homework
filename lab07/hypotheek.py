# -*- coding: utf-8 -*-
""" Created by dcockbur (Declan Cockburn) on 4/12/2019 """




principal = 200000
int_rate = 0.022
years = 30


payment = principal/(years*12)
tot = 0
for m in range(years*12):
    interest = (principal/12)*int_rate
    print("M: {}, Pr: {}, Rdmptn: {}, Int: {}, tot: {}".format(m+1, principal, payment, interest, interest + payment))
    principal = principal-payment
    tot += payment+interest

print(tot)
