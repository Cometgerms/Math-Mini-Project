import random
import matplotlib.pyplot as plt

memo_change_0 = []
memo_won_0 = []
memo_wining_rate_cr0 = []

memo_change_1 = []
memo_won_1 = []
memo_wining_rate_cr1 = []
round_ = 10000000
WON_SUM_0 = 0
for i in range(round_):
    random_car = random.randint(1, 3)
    goat = []
    for j in range(1, 4):
        if j!=random_car:
            goat.append(int(j))
    choose1 = random.randint(1, 3)
    if(choose1 == random_car):
        AGoat = goat[random.randint(0, 1)]
    else:
        for j in goat:
            if (j != choose1) & (j != random_car):
                AGoat = j
    choose2 = 0
    memo_change_0.append(int(choose2))
    if choose2 == 1:
        for j in range(1, 4):
            if (j!=AGoat) & (j!=choose1):
                final_choice = j
    else: final_choice = choose1
    if final_choice == random_car:
        memo_won_0.append(1)
        WON_SUM_0+=1
    else:
        memo_won_0.append(0)

    FLOAT_WON_SUM = float(WON_SUM_0)
    FLOAT_TOTAL = float(i+1)
    memo_wining_rate_cr0.append(FLOAT_WON_SUM / FLOAT_TOTAL * 100.0)

WON_SUM_1=0
for i in range(round_):
    random_car = random.randint(1, 3)
    goat = []
    for j in range(1, 4):
        if j!=random_car:
            goat.append(int(j))
    choose1 = random.randint(1, 3)
    if(choose1 == random_car):
        AGoat = goat[random.randint(0, 1)]
    else:
        for j in goat:
            if (j != choose1) & (j != random_car):
                AGoat = j
    choose2 = 1
    memo_change_1.append(int(choose2))
    if choose2 == 1:
        for j in range(1, 4):
            if (j!=AGoat) & (j!=choose1):
                final_choice = j
    else: final_choice = choose1
    if final_choice == random_car:
        memo_won_1.append(1)
        WON_SUM_1+=1
    else:
        memo_won_1.append(0)

    FLOAT_WON_SUM = float(WON_SUM_1)
    FLOAT_TOTAL = float(i+1)
    memo_wining_rate_cr1.append(FLOAT_WON_SUM / FLOAT_TOTAL * 100.0)

plt.plot(memo_wining_rate_cr0, color='#647fe6', label='Choosing rate = 0')
plt.text(round_, memo_wining_rate_cr0[round_-1], memo_wining_rate_cr0[round_-1])
plt.plot(memo_wining_rate_cr1, color='#c2749c', label='Choosing rate = 1')
plt.text(round_, memo_wining_rate_cr1[round_-1], memo_wining_rate_cr1[round_-1])
plt.legend(loc='upper right', edgecolor='none', facecolor='none')
plt.xlabel("Times")
plt.style.use('bmh')
plt.ylabel("Probability %")


