import time
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from utils.tandapay import TandaPaySimulator

test_data = [
    {
        'ev': [81, 1000, .70, .25, .08, 1., 2, 1, .5],
        'pv': [.20, .04, .7, .2, .8, .05],
    },
    {
        'ev': [75, 1000, .55, .29, .05, 1., 2, 1, .5],
        'pv': [.15, .03, .7, .2, .8, .05],
    },
    {
        'ev': [71, 1000, .70, .23, .10, 1., 2, 1, .5],
        'pv': [.10, .02, .7, .2, .8, .05],
    },
    {
        'ev': [65, 1000, .55, .27, .07, 1., 2, 1, .5],
        'pv': [.05, .01, .7, .2, .8, .05],
    }
]

failure_count = [0, 0, 0, 0]
result_list = [[], [], [], []]

for i, d in enumerate(test_data):
    for _ in range(100):
        sim = TandaPaySimulator(ev=d['ev'], pv=d['pv'], matrix=True)
        result = sim.start_simulate()
        remaining = result[1] / result[0]
        result_list[i].append(remaining)
        if remaining < .5:
            failure_count[i] += 1

avg_percentage = [round(sum(m) / len(m) * 100, 2) for m in result_list]

for i, r in enumerate(result_list):
    plt.hist(r, density=True, bins=round(max(r) * 100), label=f"Value {i + 1}, AVG: {avg_percentage[i]}%)")
    mn, mx = plt.xlim()
    plt.xlim(mn, mx)
    kde_xs = np.linspace(mn, mx, 300)
    kde = st.gaussian_kde(r)
    plt.plot(kde_xs, kde.pdf(kde_xs), label="PDF")
    plt.legend(loc="upper left")
    plt.ylabel('Count & Probability')
    plt.xlabel(f'EV: {test_data[i]["ev"]}, PV: {test_data[i]["pv"]}')
    plt.title(f"Failure Rate: {failure_count[i]}%")
    plt.show()

time.sleep(.1)
print(f"Failure Rate: {failure_count}")
print(f"Average remaining percentages: {avg_percentage}")
