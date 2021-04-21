import time
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from utils.tandapay import TandaPaySimulator

test_data = [
    {
        'ev': [81, 1000, .30, .25, .10, 1., 2, 1, .5],
        'pv': [.20, .04, .7, .2, .8, .05],
    },
    {
        'ev': [81, 1000, .30, .25, .15, 1., 2, 1, .5],
        'pv': [.20, .04, .7, .2, .8, .05],
    },
    {
        'ev': [81, 1000, .30, .25, .20, 1., 2, 1, .5],
        'pv': [.20, .04, .7, .2, .8, .05],
    },
    {
        'ev': [81, 1000, .30, .25, .25, 1., 2, 1, .5],
        'pv': [.20, .04, .7, .2, .8, .05],
    }
]

failure_count = [0, 0, 0, 0]
result_list = [[], [], [], []]

for i, d in enumerate(test_data):
    for _ in range(100):
        sim = TandaPaySimulator(ev=d['ev'], pv=d['pv'], matrix=True)
        result = sim.start_simulation()
        remaining = result[1] / result[0]
        result_list[i].append(remaining)
        if remaining < .5:
            failure_count[i] += 1

for i, r in enumerate(result_list):
    plt.figure(i + 1)
    plt.hist(r, density=True, bins=round(max(r) * 100), label=f"Value {i + 1}")
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
