import time
import json


def generate_matrix():
    ev4_array = [15, 18, 21, 24, 27]
    pv4_array = [8, 12, 16, 20]
    pv5_array = [77, 83, 89, 95]
    ev3_array = [40, 55, 70]
    ev1_array = [60, 68, 70, 85]
    ev5_array = [10, 20]
    ev6_array = [65, 85]
    ev7_array = [2, 3]

    pv1 = 20
    pv2 = 4
    pv3 = 70
    pv6 = 3
    ev8 = 3
    ev2 = 1000
    ev9 = 0.33333

    matrix = []

    for ev4 in ev4_array:
        for pv4 in pv4_array:
            for pv5 in pv5_array:
                for ev3 in ev3_array:
                    for ev1 in ev1_array:
                        for ev5 in ev5_array:
                            for ev6 in ev6_array:
                                for ev7 in ev7_array:
                                    matrix.append(
                                        [ev1, ev2, ev3, ev4, ev5, ev6, ev7, ev8, ev9, pv1, pv2, pv3, pv4, pv5, pv6])

    with open('matrix.json', 'w') as f:
        f.write(json.dumps({'progress': 0, 'matrix': matrix}))


if __name__ == '__main__':
    start = time.time()
    generate_matrix()
    print(f'Elapsed: {time.time() - start} seconds')
