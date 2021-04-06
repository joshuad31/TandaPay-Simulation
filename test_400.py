import time

from utils.tandapay import TandaPaySimulator


ev_list = [
    [81, 1000, .70, .25, .08, 1., 2, 1, .5],
    [75, 1000, .55, .29, .05, 1., 2, 1, .5],
    [71, 1000, .70, .23, .10, 1., 2, 1, .5],
    [65, 1000, .55, .27, .07, 1., 2, 1, .5],
]

pv_list = [
    [.20, .04, .7, .2, .8, .05],
    [.15, .03, .7, .2, .8, .05],
    [.10, .02, .7, .2, .8, .05],
    [.05, .01, .7, .2, .8, .05],
]

failure_count = [0, 0, 0, 0]
result_list = [[], [], [], []]

for i, ev in enumerate(ev_list):
    ev.append(ev[1] * 0.025 * ev[0])
    for _ in range(100):
        sim = TandaPaySimulator(ev=ev, pv=pv_list[i], matrix=True)
        result = sim.start_simulate()
        remaining = result[1] / result[0]
        result_list[i].append(remaining)
        if remaining < .5:
            failure_count[i] += 1

avg_percentage = [round(sum(m) / len(m) * 100, 2) for m in result_list]

time.sleep(.1)
print(f"Failure counts: {failure_count}")
print(f"Average remaining percentages: {avg_percentage}")
