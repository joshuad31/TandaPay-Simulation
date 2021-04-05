import time

from utils.common import get_config
from utils.tandapay import TandaPaySimulator


ev_list = [
    [81, 1000, .70, .25, .08, 1., 2, 1, .5],
    [75, 1000, .55, .20, .10, 1., 2, 1, .5],
    [71, 1000, .70, .15, .12, 1., 2, 1, .5],
    [65, 1000, .55, .10, .14, 1., 2, 1, .5],
]

pv_list = [
    [.20, .04, .7, .2, .8, .05],
    [.15, .03, .7, .2, .8, .05],
    [.10, .02, .7, .2, .8, .05],
    [.05, .01, .7, .2, .8, .05],
]

conf = get_config()
failure_count = [0, 0, 0, 0]

for i, ev in enumerate(ev_list):
    ev.append(ev[1] * 0.025 * ev[0])
    for _ in range(100):
        sim = TandaPaySimulator(conf=conf, ev=ev, pv=pv_list[i], matrix=True)
        result = sim.start_simulate()
        if result[1] / result[0] < .5:
            failure_count[i] += 1

time.sleep(.1)
print(f"Failure count: {failure_count}")
