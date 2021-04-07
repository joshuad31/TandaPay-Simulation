import os
import time
from datetime import datetime
from openpyxl import load_workbook
from utils.tandapay import TandaPaySimulator

# =============================  Test Data  =========================================
ev4_list = [.24, .26, .27, .28, .29]
pv4_list = [.08, .12, .16, .20]
pv5_list = [.77, .83, .89, .95]
ev3_list = [.40, .55, .70]
ev1_list = [60, 68, 70, 85]
ev5_list = [.10, .20]
ev6_list = [.70, 1.00]
ev7_list = [2, 3]
ev2 = 1000
ev8 = 1
ev9 = .33333
pv1 = .10
pv2 = .02
pv3 = .7
pv6 = .03
# ===================================================================================

_cur_dir = os.path.dirname(os.path.realpath(__file__))
os.makedirs(os.path.join(_cur_dir, 'result'), exist_ok=True)

s_time = time.time()

dataset = []

for ev4 in ev4_list:
    for pv4 in pv4_list:
        for pv5 in pv5_list:
            for ev3 in ev3_list:
                for ev1 in ev1_list:
                    for ev5 in ev5_list:
                        for ev6 in ev6_list:
                            for ev7 in ev7_list:
                                dataset.append({
                                    'ev': [ev1, ev2, ev3, ev4, ev5, ev6, ev7, ev8, ev9],
                                    'pv': [.1, .02, .7, pv4, pv5, .03]
                                })

results = []
workbook = load_workbook(os.path.join(_cur_dir, 'databases', '3 Matrix Database.xlsx'))
sh_map = workbook[workbook.sheetnames[0]]
sh_log = workbook[workbook.sheetnames[1]]

for i, d in enumerate(dataset):
    print(f"========== Processing {i}")
    ev = d['ev']
    pv = d['pv']
    sim = TandaPaySimulator(ev=ev, pv=pv, matrix=True)
    r = sim.start_simulation()
    collapsed = 1 if r[1] / r[0] < .5 else 0
    results.append({'ev': ev, 'pv': pv, 'c': collapsed, 'result': r})
    sh_map.cell(i + 3, 1).value = i + 1
    sh_map.cell(i + 3, 2 + ev4_list.index(ev[3])).value = collapsed
    sh_map.cell(i + 3, 7 + pv4_list.index(pv[3])).value = collapsed
    sh_map.cell(i + 3, 11 + pv5_list.index(pv[4])).value = collapsed
    sh_map.cell(i + 3, 15 + ev3_list.index(ev[2])).value = collapsed
    sh_map.cell(i + 3, 18 + ev1_list.index(ev[0])).value = collapsed
    sh_map.cell(i + 3, 22 + ev5_list.index(ev[4])).value = collapsed
    sh_map.cell(i + 3, 24 + ev6_list.index(ev[5])).value = collapsed
    sh_map.cell(i + 3, 26 + ev7_list.index(ev[6])).value = collapsed

    sh_log.cell(i + 2, 1).value = i + 1
    for j in range(7):
        # EV3 ~ EV6 are percentage values
        ratio = 100 if 1 < j < 6 else 1
        sh_log.cell(i + 2, 2 + j).value = ev[j] * ratio
    for j in range(6):
        sh_log.cell(i + 2, 9 + j).value = pv[j] * 100
    for j, v in enumerate(r):
        sh_log.cell(i + 2, 15 + j).value = v

total = len(dataset)

for i, ev4 in enumerate(ev4_list):
    sh_map.cell(2, 2 + i).value = round(len([r for r in results if r['c'] and r['ev'][3] == ev4]) / total * 100, 2)
for i, pv4 in enumerate(pv4_list):
    sh_map.cell(2, 7 + i).value = round(len([r for r in results if r['c'] and r['pv'][3] == pv4]) / total * 100, 2)
for i, pv5 in enumerate(pv5_list):
    sh_map.cell(2, 11 + i).value = round(len([r for r in results if r['c'] and r['pv'][4] == pv5]) / total * 100, 2)
for i, ev3 in enumerate(ev3_list):
    sh_map.cell(2, 15 + i).value = round(len([r for r in results if r['c'] and r['ev'][2] == ev3]) / total * 100, 2)
for i, ev1 in enumerate(ev1_list):
    sh_map.cell(2, 18 + i).value = round(len([r for r in results if r['c'] and r['ev'][0] == ev1]) / total * 100, 2)
for i, ev5 in enumerate(ev5_list):
    sh_map.cell(2, 22 + i).value = round(len([r for r in results if r['c'] and r['ev'][4] == ev5]) / total * 100, 2)
for i, ev6 in enumerate(ev6_list):
    sh_map.cell(2, 24 + i).value = round(len([r for r in results if r['c'] and r['ev'][5] == ev6]) / total * 100, 2)
for i, ev7 in enumerate(ev7_list):
    sh_map.cell(2, 26 + i).value = round(len([r for r in results if r['c'] and r['ev'][6] == ev7]) / total * 100, 2)

result_file = os.path.join(_cur_dir, 'result', f"Matrix_{datetime.now().strftime('%m_%d_%Y__%H_%M_%S')}.xlsx")
workbook.save(result_file)
workbook.close()

print(f"Saved to {result_file}, elapsed: {time.time() - s_time}")
