import ntpath
import os
from datetime import datetime
import random
from openpyxl import load_workbook

from settings import RESULT_DIR
from utils.functions import init_user_rec, init_sys_rec, user_func_1, user_func_2, sys_func_3, sys_func_4, sys_func_6, \
    sys_func_7, sys_func_8, sys_func_9
from utils.logger import logger


class TandaPaySimulator(object):

    def __init__(self, conf, ev, pv):
        self.conf = conf
        self.ev = ev
        self.pv = pv
        self.wb = {}
        self.sh = {}
        self.excel_files = {}
        self.counter = 0

        self.sy_rec_p = [None, ] * 21
        self.sy_rec_f = [None, ] * 21
        self.sy_rec_r = [None, ] * 21

    def _checksum(self, syfunc: int):
        c_count = 0
        c_value = 0
        checked_vals = []
        for i in range(self.ev[0]):
            c_us_rec3_val = self.sh['user'].cell(i + 2, 4).value
            c_us_rec8_val = self.sh['user'].cell(i + 2, 9).value
            if c_us_rec3_val == 0 or c_us_rec8_val == 'defected':
                continue
            c_us_rec4_val = self.sh['user'].cell(i + 2, 5).value
            if c_us_rec3_val not in checked_vals:
                for j in range(self.ev[0]):
                    c_ur3_sub_val = self.sh['user'].cell(j + 2, 4).value
                    c_ur8_sub = self.sh['user'].cell(j + 2, 9)
                    if c_ur3_sub_val == 0 or c_ur8_sub.value == 'defected':
                        continue
                    c_ur4_sub = self.sh['user'].cell(j + 2, 5)
                    if c_ur3_sub_val == c_us_rec3_val:
                        c_count += 1
                        c_value += c_ur4_sub.value
                if c_value % c_count != 0:
                    msg = f'______________ Period {self.counter} :: SyFunc {syfunc} _checksum failed(i={i}): ' \
                          f'c_value({c_value}) % c_count({c_count}) = {c_value % c_count}.. This should be 0!'
                    logger.error(msg)
                if c_count != c_us_rec4_val:
                    msg = f'______________ Period {self.counter} :: SyFunc {syfunc} _checksum failed(i={i}): ' \
                          f'UsRec4 value({c_us_rec4_val}) doesn\'t match with {c_count}'
                    logger.error(msg)
                checked_vals.append(c_us_rec3_val)
                c_count = 0
                c_value = 0

    def _checksum_sr1(self, _sy_rec1_val: int, syfunc: int):
        counter = len([i for i in range(self.ev[0]) if self.sh['user'].cell(i + 2, 4).value == 0])
        if self.ev[0] - _sy_rec1_val != counter:
            logger.debug(f'______________ Period {self.counter}')
            msg = f'SyFunc {syfunc} _checksum_sr1 failed: counter = {counter} - ' \
                  f'supposed to be {self.ev[0] - _sy_rec1_val}'
            logger.error(msg)

    def get_select_users(self, _filter: str, u_rec: int) -> list:
        """
        Returns list of user indexes (for Excel) where User Record 'u_rec' is equal to '_filter' argument
        """
        return [i + 2 for i in range(self.ev[0]) if self.sh['user'].cell(i + 2, u_rec + 1).value == _filter]

    def assign_variables(self):
        for i in range(1, 20):
            self.sy_rec_p[i] = self.sh['system'].cell(self.counter * 3 - 1, i + 2)
            self.sy_rec_f[i] = self.sh['system'].cell(self.counter * 3, i + 2)
            self.sy_rec_r[i] = self.sh['system'].cell(self.counter * 3 + 1, i + 2)

    def init_sheet(self, target_dir, db_type):
        db_file = self.conf['database'][db_type]
        self.wb[db_type] = load_workbook(db_file)
        self.sh[db_type] = self.wb[db_type].active
        if db_type == 'user':
            for row in self.sh['user']['A2:N200']:
                for cell in row:
                    cell.value = None
        elif db_type == 'system':
            for row in self.sh['system']['C2:U37']:
                for cell in row:
                    cell.value = None
        self.excel_files[db_type] = os.path.join(target_dir, ntpath.basename(self.conf['database'][db_type]))
        self.save_to_excel(db_type)

    def save_to_excel(self, db_type):
        self.wb[db_type].save(self.excel_files[db_type])

    def start_simulate(self, count):
        target_dir = os.path.join(RESULT_DIR, datetime.now().strftime('%m_%d_%Y__%H_%M_%S'))
        os.makedirs(target_dir)
        for k in {"system", "user"}:
            self.init_sheet(target_dir, k)

        logger.debug(f'EV1: {self.ev[0]}')

        self.counter = 1
        while self.counter <= count:
            logger.info(f'Current period is: {self.counter}')
            if self.counter == 1:
                init_user_rec(self)
                init_sys_rec(self)
                # Subgroup  # FUNCTION FOR SUBGROUP EXECUTION
                step1_ev1 = self.ev[0]
                step2 = self.ev[0] / 5
                step3 = round(step2 / 2.3333)
                step4 = step3 * 5
                step5 = step1_ev1 - step4
                step6 = step5 / 6
                step7 = round(step6 / 2)
                step8 = step7 * 6
                step9 = step5 - step8
                step10 = step9 / 7
                step11 = int(step10 / 2)
                step12 = step11 * 7
                step13 = step9 - step12
                step14 = int(step13 / 4)
                step15 = step13 % 4
                if step15 == 1:
                    step3 = step3 - 1
                    step7 = step7 + 1
                elif step15 == 2:
                    step3 = step3 - 1
                    step11 = step11 + 1
                elif step15 == 3:
                    step3 = step3 - 1
                    step14 = step14 + 2

                # now assigning number to the group, condition checking for group == 4
                group_num = 1
                group_mem_count = 0
                temp_val_four = step14 * 4
                offset = 0
                for i in range(temp_val_four):
                    self.sh['user'].cell(i + offset + 2, 2).value = group_num  # 'D'
                    self.sh['user'].cell(i + offset + 2, 3).value = 4
                    self.sh['user'].cell(i + offset + 2, 4).value = group_num  # 'D'
                    self.sh['user'].cell(i + offset + 2, 5).value = 4
                    group_mem_count += 1
                    if group_mem_count == 4:
                        group_num += 1
                        group_mem_count = 0
                offset += temp_val_four

                # condition checking for group == 5
                temp_val_five = step3 * 5
                for i in range(temp_val_five):
                    self.sh['user'].cell(i + offset + 2, 2).value = group_num  # 'A'
                    self.sh['user'].cell(i + offset + 2, 3).value = 5
                    self.sh['user'].cell(i + offset + 2, 4).value = group_num  # 'A'
                    self.sh['user'].cell(i + offset + 2, 5).value = 5
                    group_mem_count += 1
                    if group_mem_count == 5:
                        group_num += 1
                        group_mem_count = 0
                offset += temp_val_five

                # condition checking for group == 6
                temp_val_six = step7 * 6
                for i in range(temp_val_six):
                    self.sh['user'].cell(i + offset + 2, 2).value = group_num  # 'B'
                    self.sh['user'].cell(i + offset + 2, 3).value = 6
                    self.sh['user'].cell(i + offset + 2, 4).value = group_num  # 'B'
                    self.sh['user'].cell(i + offset + 2, 5).value = 6
                    group_mem_count += 1
                    if group_mem_count == 6:
                        group_num += 1
                        group_mem_count = 0
                offset += temp_val_six

                # condition checking for group == 7
                temp_val_seven = step11 * 7
                for i in range(temp_val_seven):
                    self.sh['user'].cell(i + offset + 2, 2).value = group_num       # 'C'
                    self.sh['user'].cell(i + offset + 2, 3).value = 7
                    self.sh['user'].cell(i + offset + 2, 4).value = group_num       # 'C'
                    self.sh['user'].cell(i + offset + 2, 5).value = 7
                    group_mem_count += 1
                    if group_mem_count == 7:
                        group_num += 1
                        group_mem_count = 0

                checksum = offset + temp_val_seven
                if checksum != self.ev[0]:
                    raise ValueError(f"Initial group checksum failed: checksum:{checksum} != EV1:{self.ev[0]}")
                logger.debug({"D": temp_val_four, "A": temp_val_five, "B": temp_val_six, "C": temp_val_seven})

                # setting valid to UsRec5
                for i in range(self.ev[0]):
                    self.sh['user'].cell(i + 2, 6).value = 'valid'
                logger.debug(
                    f'Group of 4 members: {step14}, 5 members: {step3}, 6 members: {step7}, '
                    f'7 members: {step11}, Total group: {step14 * 4 + step3 * 5 + step7 * 6 + step11 * 7})')

                self.save_to_excel('user')

                # ROLE 1
                # EV 4 = Percentage of honest defectors
                role_ev4 = int(self.ev[0] * self.ev[3])
                defectors = random.sample(range(self.ev[0]), role_ev4)
                non_defectors = [i for i in range(self.ev[0]) if i not in defectors]
                # EV 5 = Percentage of low-morale members
                role_ev5 = int(self.ev[0] * self.ev[4])
                low_morale_list = random.sample(non_defectors, role_ev5)
                for i in range(self.ev[0]):
                    self.sh['user'].cell(i + 2, 7).value = 'defector' if i in defectors else \
                        'low-morale' if i in low_morale_list else 'unity-role'

                # ROLE 2
                # temp_val_four users and pick remaining users randomly to be equal with EV6
                remaining_pct = int(self.ev[5] * self.ev[0]) - temp_val_four
                if remaining_pct > 0:
                    rand_dep_user = random.sample(range(temp_val_four, self.ev[0]), remaining_pct)
                else:
                    rand_dep_user = []

                for i in range(self.ev[0]):
                    self.sh['user'].cell(i + 2, 8).value = 'dependent' if (i < temp_val_four or i in rand_dep_user) \
                        else 'independent'

                self.save_to_excel('user')
                logger.debug('Roles Assigned!')

            self.assign_variables()
            if self.counter == 1:
                user_func_1(self)
            if 1 < self.counter < 10:
                user_func_2(self)
            sys_func_3(self)
            sys_func_4(self)
            if self.counter == 1:
                for k in range(1, 20):
                    self.sy_rec_f[k].value = self.sy_rec_p[k].value
                    self.sy_rec_r[k].value = self.sy_rec_p[k].value

                #################
                # ___SyFunc5___
                #################
                self.sy_rec_f[9].value = self.sy_rec_f[3].value * self.sy_rec_f[19].value
                self.sh['system'].cell(4, 11).value = self.sy_rec_f[9].value
                self.save_to_excel('system')
            self._checksum(4)
            if self.counter != 1:
                for k in range(1, 20):
                    self.sy_rec_r[k].value = self.sy_rec_p[k].value

            sys_func_6(self)
            sys_func_7(self)
            sys_func_8(self)
            sys_func_9(self)

            # ___SyFunc11___  (Reorg Stage 7)
            _path = 0
            if self.counter != 10:
                total = self.sy_rec_r[3].value + self.sy_rec_r[5].value + self.sy_rec_r[7].value

                if total > 0:
                    _path = 1
                elif total == 0:
                    _path = 2

                if _path == 1:
                    reorg_row = self.counter * 3 + 1
                    new_pay_row = self.counter * 3 + 2
                    # copying values of previous to current
                    sy_rec_new_p = [None] * 21
                    sy_rec_r = [None] * 21
                    for k in range(1, 20):
                        sy_rec_r[k] = self.sh['system'].cell(reorg_row, k + 2)
                        sy_rec_new_p[k] = self.sh['system'].cell(new_pay_row, k + 2)
                        sy_rec_new_p[k].value = sy_rec_r[k].value

                    # Overwriting values in new row
                    sy_rec_new_p[18].value = sy_rec_new_p[17].value
                    for k in {3, 5, 6, 9, 10, 11, 13, 14, 15, 17}:
                        sy_rec_new_p[k].value = 0
                    self.save_to_excel('system')

                    self._checksum(11)
                    self._checksum_sr1(sy_rec_new_p[1].value, 11)

            # logging to log file
            if self.counter == 10 or _path == 2:
                logger.info(f'Run complete, logging simulation results')
                try:
                    percent = (self.sh['system'].cell(3, 5).value / self.ev[0]) * 100
                    inc_premium = round((self.sy_rec_f[19].value / self.sh["system"].cell(2, 21).value) * 100, 2)
                    result_file = os.path.join(target_dir, "result.txt")
                    with open(result_file, 'w') as f:
                        lines = [
                            f'{self.ev[0]} is the number of members at the start of the simulation\n',
                            f'{self.sy_rec_r[1].value} is the number of valid members remaining at the end '
                            f'of the simulation\n',
                            f'{round(((self.ev[0] - self.sy_rec_r[1].value) / self.ev[0]) * 100, 2)}% of '
                            f'policyholders left the group by end of simulation\n',
                            f'{round(self.sh["system"].cell(2, 21).value)} was the initial premium members were '
                            f'asked to pay.\n',
                            f'{inc_premium} is the final premium members were asked to pay.\n',
                            f'Premiums increased by {inc_premium}% by end of simulation\n',
                            f'self.SyRec 3 (period 0 finalize) = {self.sh["system"].cell(3, 5).value}\n',
                            f'{self.ev[3] * 100}% of policyholders who were assigned to defect\n',
                            f'{round(percent, 2)}% of policyholders who actually defected\n',
                            f'{(self.pv[4]) * 100}% was the initial collapse threshold set for PV 5\n'
                        ]
                        f.writelines(lines)
                    logger.info(''.join(lines))
                except Exception as e:
                    logger.exception(e)
            self.counter += 1

        logger.info(f'Iteration {count} times complete! Please run the entire application again.')
        return True
