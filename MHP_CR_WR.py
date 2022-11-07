import random
import matplotlib.pyplot as plt
import numpy as np

memo_change_0 = []
memo_won_0 = []
memo_wining_rate_cr0 = []
changing_prob_list = [0]*100

round_ = 100000
for w in range(101):
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
        ch2_index = random.randint(0, 99)
        choose2 = changing_prob_list[ch2_index]
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
    memo_wining_rate_cr0.append(float(WON_SUM_0)/float(round_))
    if w!=100:
        memo_change_0.append(w)
        changing_prob_list[w] = 1
    else:
        memo_change_0.append(w)
        break

fun = np.polyfit(memo_change_0, memo_wining_rate_cr0, 1)
poly = np.poly1d(fun)
print('y = ', poly)

y_fit = poly(memo_change_0)

plt.plot(memo_change_0, y_fit, color='#647fe6', linewidth=1, label='polyfit values')
plt.scatter(memo_change_0, memo_wining_rate_cr0, s=5, c='#c2749c')

plt.xlabel("Probability of changing decision %")
plt.style.use('bmh')
plt.ylabel("Probability of winning ")