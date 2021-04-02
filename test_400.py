from utils.common import get_config
from utils.tandapay import TandaPaySimulator


ev_list = [
    [81, 1000, 1, .25, .10, 0, 2, 0, .99],
    [75, 1000, 1, .20, .15, 0, 2, 0, .99],
    [71, 1000, 1, .15, .20, 0, 2, 0, .99],
    [65, 1000, 1, .10, .25, 0, 2, 0, .99],
]

pv_list = [
    [.20, .04, .7, .2, .8, .05],
    [.15, .03, .7, .2, .8, .05],
    [.10, .02, .7, .2, .8, .05],
    [.05, .01, .7, .2, .8, .05],
]

conf = get_config()
failure_count = [0, 0, 0, 0]

for i in range(4):
    ev_list[i].append(ev_list[i][1] * 0.025 * ev_list[i][0])
    for _ in range(100):
        sim = TandaPaySimulator(conf=conf, ev=ev_list[i], pv=pv_list[i], matrix=True)
        result = sim.start_simulate()
        if result[1] / result[0] < .5:
            failure_count[i] += 1

print(f"Failure count: {failure_count}")
