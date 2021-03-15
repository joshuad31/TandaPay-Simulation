import time
import json


def generate_matrix()
    EV4_ARRAY = [15,18,21,24,27]
    PV4_ARRAY = [8,12,16,20]
    PV5_ARRAY = [77,83,89,95]
    EV3_ARRAY = [40,55,70]
    EV1_ARRAY = [60,68,70,85]
    EV5_ARRAY = [10,20]
    EV6_ARRAY = [65,85]
    EV7_ARRAY = [2,3]

    PV1 = 20
    PV2 = 4
    PV3 = 70
    PV6 = 3
    EV8 = 3
    EV2 = 1000
    EV9 = 0.33333

    matrix = []

    for ev4 in EV4_ARRAY:
        for pv4 in PV4_ARRAY:
            for pv5 in PV5_ARRAY:
                for ev3 in EV3_ARRAY:
                    for ev1 in EV1_ARRAY:
                        for ev5 in EV5_ARRAY:
                            for ev6 in EV6_ARRAY:
                                for ev7 in EV7_ARRAY:
                                    matrix.append([ev1,EV2,ev3,ev4,ev5,ev6,ev7,EV8,EV9,PV1,PV2,PV3,pv4,pv5,PV6])

    with open('matrix.json', 'w') as f:
        f.write(json.dumps({'progress':0, 'matrix':matrix}))

if __name__ == '__main__':
    start = time.time()
    generate_matrix()
    print(f'Elapsed: {time.time() - start} seconds')