import random
from utils.logger import logger


def init_user_rec(self):
    for i in range(self.ev[0]):
        val1 = self.sh['user'].cell(i + 2, 1)
        val1.value = 'user{}'.format(i + 1)
        # assigning UsRec9 into the database
        val2 = self.sh['user'].cell(i + 2, 10)
        val2.value = 0
        # assigning UsRec10 into the database
        val3 = self.sh['user'].cell(i + 2, 11)
        val3.value = 0
        # assigning UsRec11 into the database
        val4 = self.sh['user'].cell(i + 2, 12)
        val4.value = self.ev[0]
        # assigning us_rec12 into the database
        val5 = self.sh['user'].cell(i + 2, 13)
        val5.value = 'yes'
        # assigning UsRec13 into the database
        val6 = self.sh['user'].cell(i + 2, 14)
        val6.value = 0
    self.save_to_excel('user')
    logger.debug('Initial values for UsRec variables set!')


def init_sys_rec(self):
    # PAGE 8, 9
    for i in range(2):
        val = self.sh['system'].cell(i + 2, 3)
        val.value = self.ev[0]
        val = self.sh['system'].cell(i + 2, 4)
        val.value = self.ev[9] / self.ev[0]
        for k in range(5, 21):
            val = self.sh['system'].cell(i + 2, k)
            val.value = 0 if k != 18 else 'no'
        val = self.sh['system'].cell(i + 2, 21)
        val.value = self.ev[9] / self.ev[0]

    for i in range(3, 30):
        for k in range(3, 22):
            val = self.sh['system'].cell(i + 2, k)
            val.value = 0
    self.save_to_excel('system')
    logger.debug('Initial values for SyRec variables set!')


def user_func_1(self):
    """"
    Pay Stage 1, USER DEFECTION FUNCTION
    """
    if self.counter == 1:
        defector_count = 0
        current_group_num = 1

        # Setting defector values in each subgroup
        defected_cache = {}
        defected_subt = {}
        low_morale_cache = []
        lm_def = []
        for i in range(self.ev[0]):
            us_rec1 = self.sh['user'].cell(i + 2, 2)
            us_rec13 = self.sh['user'].cell(i + 2, 14)

            us_rec6 = self.sh['user'].cell(i + 2, 7)
            us_rec7 = self.sh['user'].cell(i + 2, 8)

            if us_rec6.value == 'defector' or i == self.ev[0] - 1:
                if current_group_num not in defected_subt:
                    defected_subt[current_group_num] = 0
                # PATH 1 for dependent
                if us_rec1.value == current_group_num or i == self.ev[0] - 1:
                    if us_rec6.value == 'defector':
                        defector_count += 1
                        us_rec13.value = defector_count
                        if us_rec7.value == 'dependent':
                            defected_subt[current_group_num] += 1
                        if us_rec13.value >= self.ev[6] or us_rec7.value == 'independent':
                            # PATH 2 (Part 1 - assigning to cache for UsRec 6 & 13 incrementation in next
                            # for loop)
                            defected_cache[current_group_num] = defector_count
                if us_rec1.value != current_group_num or i == self.ev[0] - 1:
                    if current_group_num in defected_cache:
                        if defected_cache[current_group_num] < self.ev[6]:
                            if defected_subt[current_group_num] != 0:
                                defected_cache[current_group_num] = defector_count
                                defected_cache[current_group_num] -= defected_subt[current_group_num]
                                low_morale_cache.append(current_group_num)
                                lm_def.append(current_group_num)

                    if defector_count < self.ev[6] and current_group_num not in defected_cache and \
                            defector_count != 0:
                        # PATH 3 (Part 1 - assigning to cache for UsRec 6 & 7 values in next for loop)
                        low_morale_cache.append(current_group_num)
                    if i != self.ev[0] - 1:
                        defector_count = 1
                        current_group_num = us_rec1.value
                        if current_group_num not in defected_subt:
                            defected_subt[current_group_num] = 0
                        us_rec13.value = defector_count
                        if us_rec7.value == 'independent':
                            # PATH 2 (Part 1 - assigning to cache for UsRec 6 & 13 incrementation in next
                            # for loop)
                            defected_cache[current_group_num] = defector_count
                        elif us_rec7.value == 'dependent':
                            defected_subt[current_group_num] += 1
        self.save_to_excel('user')

        # PATH 2 & 3 (Part 2)
        for i in range(self.ev[0]):
            us_rec1 = self.sh['user'].cell(i + 2, 2)
            us_rec3 = self.sh['user'].cell(i + 2, 4)
            us_rec4 = self.sh['user'].cell(i + 2, 5)
            us_rec5 = self.sh['user'].cell(i + 2, 6)
            us_rec6 = self.sh['user'].cell(i + 2, 7)
            us_rec7 = self.sh['user'].cell(i + 2, 8)
            us_rec8 = self.sh['user'].cell(i + 2, 9)
            us_rec12 = self.sh['user'].cell(i + 2, 13)
            us_rec13 = self.sh['user'].cell(i + 2, 14)

            if us_rec1.value in defected_cache:
                # PATH 2 (Part 2)
                us_rec13.value = defected_cache[us_rec1.value]
                # group_mems = us_rec4.value - us_rec13.value
                if us_rec6.value == 'defector' and us_rec1.value not in lm_def:
                    # Defectors >= ev7
                    us_rec12.value = 'no'
                    us_rec8.value = 'defected'
                    self.sy_rec_p[1].value -= 1
                    self.sy_rec_p[5].value += 1
                    self.sy_rec_p[3].value += 1

                    for _ in range(self.ev[0]):
                        ur4 = self.sh['user'].cell(_ + 2, 5)
                        ur1 = self.sh['user'].cell(_ + 2, 2)
                        ur3 = self.sh['user'].cell(_ + 2, 4)
                        ur2 = self.sh['user'].cell(_ + 2, 3)

                        if ur4.value != 0:
                            if us_rec3.value == ur3.value:
                                ur4.value -= 1
                                # ur4.value = group_mems
                                if us_rec1.value == ur1.value:
                                    ur2.value -= 1
                    us_rec3.value = 0
                    us_rec4.value = 0
                    us_rec5.value = 'NR'
                    us_rec8.value = 'NR'
                    us_rec12.value = 'NR'
                    self.save_to_excel('user')

                if us_rec6.value == 'defector' and us_rec1.value in lm_def and us_rec7.value == 'independent':
                    # Defectors < ev7 and independent defectors exist
                    us_rec12.value = 'no'
                    us_rec8.value = 'defected'
                    self.sy_rec_p[1].value -= 1
                    self.sy_rec_p[5].value += 1
                    self.sy_rec_p[3].value += 1

                    for _ in range(self.ev[0]):
                        ur4 = self.sh['user'].cell(_ + 2, 5)
                        ur1 = self.sh['user'].cell(_ + 2, 2)
                        ur3 = self.sh['user'].cell(_ + 2, 4)
                        ur2 = self.sh['user'].cell(_ + 2, 3)
                        if ur4.value != 0:
                            if us_rec3.value == ur3.value:
                                ur4.value -= 1
                                # ur4.value = group_mems
                                if us_rec1.value == ur1.value:
                                    ur2.value -= 1
                    us_rec3.value = 0
                    us_rec4.value = 0
                    us_rec5.value = 'NR'
                    us_rec8.value = 'NR'
                    us_rec12.value = 'NR'
                    self.save_to_excel('user')

            if us_rec1.value in low_morale_cache and us_rec7.value == 'dependent':
                # PATH 3 (Part 2)
                if us_rec1.value in defected_cache:
                    us_rec13.value = defected_cache[us_rec1.value]
                else:
                    us_rec13.value = 0
                if us_rec6.value == 'defector':
                    us_rec6.value = 'low-morale'
        self.save_to_excel('user')
        self.save_to_excel('system')

        self._checksum(1)


def user_func_2(self):
    """"
    Pay Stage 2, USER DEFECTION FUNCTION
    """
    if self.counter != 1:
        slope = (self.pv[3] - self.pv[1]) / (self.pv[2] - self.pv[0])
        sy_rec19_prev = self.sh['system'].cell(self.rows[0] - 3, 21)
        try:
            a = float(self.sy_rec_p[19].value)
            b = float(sy_rec19_prev.value)
            inc_premium = (a / b) - 1
        except Exception as e:
            logger.exception(e)
            logger.debug(f'SyRec19.value: {self.sy_rec_p[19].value}')
            logger.debug(f'sy_rec19_prev.value: {sy_rec19_prev.value}')
            logger.debug(f'row1: {self.rows[0]}')
            logger.debug(f'row1-3: {self.rows[0] - 3}')
            inc_premium = 0

        valid_users = []
        for i in range(self.ev[0]):
            us_rec5 = self.sh['user'].cell(i + 2, 6)
            if us_rec5.value == 'valid':
                valid_users.append(i + 2)

        if inc_premium >= self.pv[0]:
            # PATH1
            skip_percent = (slope * inc_premium - slope * self.pv[0]) + self.pv[1]

            skip_hash = round(self.sy_rec_p[1].value * skip_percent)
            skip_users = random.sample(valid_users, skip_hash)

            for i in range(self.ev[0]):
                index = i + 2
                us_rec12 = self.sh['user'].cell(index, 13)
                if index in skip_users:
                    us_rec12.value = 'no'

        if inc_premium < self.pv[0]:
            try:
                num = (self.sy_rec_p[19].value / (float(self.ev[0] / self.ev[0])) - 1)
                if num >= self.pv[4]:
                    skip_hash = round(self.sy_rec_p[1].value * self.pv[5])
                    skip_users = random.sample(valid_users, skip_hash)

                    # rand_skip_users = []
                    # for _ in range(skip_hash):
                    #     n = random.randint(2,self.ev[0])
                    #     while True:
                    #         if n in rand_skip_users:
                    #             n = random.randint(2,self.ev[0])
                    #         elif n not in rand_skip_users:
                    #             rand_skip_users.append(n)
                    #             break
                    for i in skip_users:
                        us_rec12 = self.sh['user'].cell(i, 13)
                        us_rec12.value = 'no'
                    self.save_to_excel('user')
                if num < self.pv[4]:
                    # PATH3
                    if self.ev[7] == 0:
                        pass
                    if self.ev[7] == 1 or self.ev[7] == 2 or self.ev[7] == 3:
                        self.ev[7] -= 1
                        # valid_users = []
                        # for i in range(self.ev[0]):
                        #     val = self.sh['user'].cell(i+2,6)
                        #     if val.value == 'valid':
                        #         valid_users.append(i+2)
                        rand_sel = random.choice(valid_users)
                        rand_us_rec12 = self.sh['user'].cell(rand_sel, 13)
                        rand_us_rec12.value = 'no'
            except ZeroDivisionError:
                pass

            self.save_to_excel('user')


def sys_func_3(self):
    """"
    Pay Stage 3, Validate premium function
    """
    valid_users = self.get_valid_users()

    path_1 = []
    for i in valid_users:
        us_rec1 = self.sh['user'].cell(i, 2)
        us_rec3 = self.sh['user'].cell(i, 4)
        us_rec4 = self.sh['user'].cell(i, 5)
        us_rec5 = self.sh['user'].cell(i, 6)
        us_rec8 = self.sh['user'].cell(i, 9)
        us_rec12 = self.sh['user'].cell(i, 13)

        if us_rec12.value == 'no':
            us_rec8.value = 'skipped'
            path_1.append(i)
            self.sy_rec_p[1].value -= 1
            self.sy_rec_p[5].value += 1  # potential incorrect copying or adding

            for _ in range(self.ev[0]):
                ur4 = self.sh['user'].cell(_ + 2, 5)
                ur1 = self.sh['user'].cell(_ + 2, 2)
                ur3 = self.sh['user'].cell(_ + 2, 4)
                ur2 = self.sh['user'].cell(_ + 2, 3)

                if ur4.value != 0:
                    if us_rec3.value == ur3.value:
                        ur4.value -= 1
                        if us_rec1.value == ur1.value:
                            ur2.value -= 1

            us_rec8.value = "NR"
            us_rec3.value = 0
            us_rec4.value = 0
            us_rec5.value = "NR"
            us_rec12.value = "NR"
            self.save_to_excel('user')

        elif us_rec12.value == 'yes':
            us_rec8.value = 'paid'

    self.save_to_excel('user')
    self.save_to_excel('system')

    self._checksum(3)
    self._checksum_sr1(self.sy_rec_p[1].value, 3)


def sys_func_4(self):
    """"
    Pay Stage 4, Invalidate subgroup function
    """
    for i in range(self.ev[0]):
        ur4 = self.sh['user'].cell(i + 2, 5)
        ur8 = self.sh['user'].cell(i + 2, 9)
        ur5 = self.sh['user'].cell(i + 2, 6)
        ur10 = self.sh['user'].cell(i + 2, 11)
        ur11 = self.sh['user'].cell(i + 2, 12)

        if ur4.value == 1 or ur4.value == 2 or ur4.value == 3:
            if ur8.value == 'paid':
                # us_rec8 = 'paid-invalid'
                ur8.value = 'paid-invalid'
                # UsRec5 = 'invalid'
                ur5.value = 'invalid'
                ur10.value = ur11.value
                self.sy_rec_p[6].value += 1
    self.save_to_excel('user')
    self.save_to_excel('system')


def sys_func_6(self):
    """"
    Reorg Stage 1
    """

    for i in range(self.ev[0]):
        _path = 0
        us_rec1 = self.sh['user'].cell(i + 2, 2)
        us_rec2 = self.sh['user'].cell(i + 2, 3)
        us_rec3 = self.sh['user'].cell(i + 2, 4)
        us_rec4 = self.sh['user'].cell(i + 2, 5)
        us_rec5 = self.sh['user'].cell(i + 2, 6)
        us_rec6 = self.sh['user'].cell(i + 2, 7)
        us_rec7 = self.sh['user'].cell(i + 2, 8)
        us_rec8 = self.sh['user'].cell(i + 2, 9)
        us_rec12 = self.sh['user'].cell(i + 2, 13)
        # 1 2 3 2 4
        if us_rec8.value == 'paid-invalid':
            if us_rec6.value == 'low-morale':
                # Path 1
                prob = random.uniform(0, 1)
                if prob >= self.ev[8]:
                    _path = 3
                elif prob < self.ev[8]:
                    _path = 2

                if _path == 3:
                    if us_rec7.value == 'independent' or us_rec2.value >= 2:
                        # path4
                        self.sy_rec_r[8].value += 1
                    else:
                        _path = 2

                if _path == 2:
                    us_rec8.value = 'quit'
                    self.sy_rec_r[1].value -= 1
                    self.sy_rec_r[7].value += 1
                    for _i in range(self.ev[0]):
                        ur4 = self.sh['user'].cell(_i + 2, 5)
                        ur3 = self.sh['user'].cell(_i + 2, 4)
                        ur2 = self.sh['user'].cell(_i + 2, 3)
                        ur1 = self.sh['user'].cell(_i + 2, 2)

                        if ur4.value != 0:
                            if ur3.value == us_rec3.value:
                                ur4.value -= 1
                                if ur1.value == us_rec1.value:
                                    ur2.value -= 1
                    us_rec8.value = "NR"
                    us_rec3.value = 0
                    us_rec4.value = 0
                    us_rec5.value = "NR"
                    us_rec12.value = "NR"
    self.save_to_excel('user')
    self.save_to_excel('system')

    for i in range(self.ev[0]):
        _path = 0
        us_rec1 = self.sh['user'].cell(i + 2, 2)
        us_rec2 = self.sh['user'].cell(i + 2, 3)
        us_rec3 = self.sh['user'].cell(i + 2, 4)
        us_rec4 = self.sh['user'].cell(i + 2, 5)
        us_rec5 = self.sh['user'].cell(i + 2, 6)
        us_rec6 = self.sh['user'].cell(i + 2, 7)
        us_rec7 = self.sh['user'].cell(i + 2, 8)
        us_rec8 = self.sh['user'].cell(i + 2, 9)
        us_rec12 = self.sh['user'].cell(i + 2, 13)
        # 1 2 3 2 4
        if us_rec8.value == 'paid-invalid':
            if us_rec6.value != 'low-morale':
                if us_rec7.value == 'independent' or us_rec2.value >= 2:
                    # path4
                    self.sy_rec_r[8].value += 1
                else:
                    _path = 2

                if _path == 2:
                    us_rec8.value = 'quit'
                    self.sy_rec_r[1].value -= 1
                    self.sy_rec_r[7].value += 1
                    for _i in range(self.ev[0]):
                        ur4 = self.sh['user'].cell(_i + 2, 5)
                        ur3 = self.sh['user'].cell(_i + 2, 4)
                        ur2 = self.sh['user'].cell(_i + 2, 3)
                        ur1 = self.sh['user'].cell(_i + 2, 2)

                        if ur4.value != 0:
                            if ur3.value == us_rec3.value:
                                ur4.value -= 1
                                if ur1.value == us_rec1.value:
                                    ur2.value -= 1
                    us_rec8.value = "NR"
                    us_rec3.value = 0
                    us_rec4.value = 0
                    us_rec5.value = "NR"
                    us_rec12.value = "NR"
    self.save_to_excel('user')
    self.save_to_excel('system')

    self._checksum(6)
    self._checksum_sr1(self.sy_rec_r[1].value, 6)


def sys_func_7(self):
    """"
    Reorg Stage 2
    """

    _path = 0
    loop_reset = False
    invalid_loop = 0  # UsRec4 for group absorbing invalid member not reassigned twice
    found_subgrp = 0
    pass_over = ["defected", "skipped", "quit", "NR"]
    for i in range(self.ev[0]):
        ur8 = self.sh['user'].cell(i + 2, 9)
        ur4 = self.sh['user'].cell(i + 2, 5)
        if ur8.value == 'paid-invalid':

            if ur4.value == 1:
                base_ur4 = ur4.value
                invalid_loop += 1

                # Chnage ur4 values of group absorbing invalid member
                if invalid_loop == 1:
                    old_ur4 = 0
                    new_ur4 = 0  # Used to set subgroup so not override values in edge cases
                    for _i in range(self.ev[0]):
                        ur4_sub = self.sh['user'].cell(_i + 2, 5)
                        ur3_sub = self.sh['user'].cell(_i + 2, 4)
                        ur5_sub = self.sh['user'].cell(_i + 2, 6)
                        ur8_sub = self.sh['user'].cell(_i + 2, 9)
                        if new_ur4 == 0:
                            if ur4_sub.value == 6 and ur8_sub.value not in pass_over and \
                                    ur5_sub.value == 'valid':
                                found_subgrp = ur3_sub.value
                                ur4_sub.value = 7
                                old_ur4 = 6
                                new_ur4 = 7
                                _path = 1
                        elif ur4_sub.value == old_ur4 and ur8_sub.value not in pass_over and \
                                ur5_sub.value == 'valid':
                            if ur3_sub.value == found_subgrp:
                                ur4_sub.value = new_ur4

                    if _path != 1:
                        for _i in range(self.ev[0]):
                            ur4_sub = self.sh['user'].cell(_i + 2, 5)
                            ur3_sub = self.sh['user'].cell(_i + 2, 4)
                            ur5_sub = self.sh['user'].cell(_i + 2, 6)
                            ur8_sub = self.sh['user'].cell(_i + 2, 9)
                            if new_ur4 == 0:
                                if ur4_sub.value == 5 and ur8_sub.value not in pass_over and \
                                        ur5_sub.value == 'valid':
                                    found_subgrp = ur3_sub.value
                                    ur4_sub.value = 6
                                    old_ur4 = 5
                                    new_ur4 = 6
                            elif ur4_sub.value == old_ur4 and ur8_sub.value not in pass_over and \
                                    ur5_sub.value == 'valid':
                                if ur3_sub.value == found_subgrp:
                                    ur4_sub.value = new_ur4
                else:  # FIXME: correct value?
                    new_ur4 = 0

                if invalid_loop == base_ur4:
                    loop_reset = True
                ur4.value = new_ur4
                ur3 = self.sh['user'].cell(i + 2, 4)
                ur3.value = found_subgrp  # !!! not referenced
                ur5 = self.sh['user'].cell(i + 2, 6)
                ur5.value = 'valid'
                ur8.value = 'reorg'
                ur9 = self.sh['user'].cell(i + 2, 10)
                ur9.value = ur9.value + 1

                if loop_reset:
                    invalid_loop = 0
                    loop_reset = False
    self.save_to_excel('user')
    self._checksum(7)

    loop_reset = False
    invalid_loop = 0  # UsRec4 for group absorbing invalid member not reassigned twice
    _path = 0
    found_subgrp = 0
    reorg_cache = {}
    for i in range(self.ev[0]):
        ur8 = self.sh['user'].cell(i + 2, 9)
        ur3 = self.sh['user'].cell(i + 2, 4)
        ur4 = self.sh['user'].cell(i + 2, 5)
        if ur8.value == 'paid-invalid':
            if ur4.value == 2:
                base_ur4 = ur4.value
                invalid_loop += 1

                # Change ur4 values of group absorbing invalid member
                if invalid_loop == 1 and ur3.value not in reorg_cache:
                    old_ur4 = 0
                    new_ur4 = 0  # Used to set subgroup so not override values in edge cases
                    for _i in range(self.ev[0]):
                        ur4_sub = self.sh['user'].cell(_i + 2, 5)
                        ur3_sub = self.sh['user'].cell(_i + 2, 4)
                        ur8_sub = self.sh['user'].cell(_i + 2, 9)
                        if new_ur4 == 0:
                            if ur4_sub.value == 5 and ur8_sub.value not in pass_over:
                                found_subgrp = ur3_sub.value
                                ur4_sub.value = 7
                                old_ur4 = 5
                                new_ur4 = 7
                            elif ur4_sub.value == 4 and ur8_sub.value not in pass_over:
                                found_subgrp = ur3_sub.value
                                ur4_sub.value = 6
                                old_ur4 = 4
                                new_ur4 = 6
                        elif ur4_sub.value == old_ur4 and ur8_sub.value not in pass_over:
                            if ur3_sub.value == found_subgrp:
                                ur4_sub.value = new_ur4

                    reorg_cache.update({ur3.value: found_subgrp})
                else:
                    new_ur4 = 0

                if invalid_loop == base_ur4:
                    loop_reset = True
                if ur3.value in reorg_cache:
                    found_subgrp = reorg_cache[ur3.value]
                    loop_reset = True
                ur4.value = new_ur4
                ur3.value = found_subgrp
                ur5 = self.sh['user'].cell(i + 2, 6)
                ur5.value = 'valid'
                ur8.value = 'reorg'
                ur9 = self.sh['user'].cell(i + 2, 10)
                ur9.value = ur9.value + 1

                if loop_reset:
                    invalid_loop = 0
                    loop_reset = False
    self.save_to_excel('user')
    self._checksum(7)

    loop_reset = False
    invalid_loop = 0  # UsRec4 for group absorbing invalid member not reassigned twice
    _path = 0
    found_subgrp = 0
    reorg_cache = {}
    for i in range(self.ev[0]):
        ur8 = self.sh['user'].cell(i + 2, 9)
        ur4 = self.sh['user'].cell(i + 2, 5)

        if ur8.value == 'paid-invalid':
            ur3 = self.sh['user'].cell(i + 2, 4)

            if ur4.value == 3:
                base_ur4 = ur4.value
                invalid_loop += 1

                # Change ur4 values of group absorbing invalid member
                if invalid_loop == 1 and ur3.value not in reorg_cache:
                    grp_found = 0
                    old_ur4 = 0
                    new_ur4 = 0  # Used to set subgroup so not override values in edge cases
                    for _i in range(self.ev[0]):

                        ur4_sub = self.sh['user'].cell(_i + 2, 5)
                        ur3_sub = self.sh['user'].cell(_i + 2, 4)
                        ur5_sub = self.sh['user'].cell(_i + 2, 6)
                        ur8_sub = self.sh['user'].cell(_i + 2, 9)
                        if new_ur4 == 0:
                            if ur4_sub.value == 3 and ur3_sub.value != ur3.value and \
                                    ur8_sub.value not in pass_over:  # and ur5_sub.value == 'valid':
                                found_subgrp = ur3_sub.value
                                ur4_sub.value = 6
                                old_ur4 = 3
                                new_ur4 = 6
                                _path = 2
                                ur5_sub.value = 'valid'
                                ur8_sub.value = 'reorg'
                                ur9_sub = self.sh['user'].cell(_i + 2, 10)
                                ur9_sub.value = ur9_sub.value + 1
                                grp_found = ur3_sub.value
                        elif ur4_sub.value == old_ur4 and ur8_sub.value not in pass_over:
                            if ur3_sub.value == found_subgrp:
                                ur4_sub.value = new_ur4
                                ur5_sub.value = 'valid'
                                ur8_sub.value = 'reorg'
                                ur9_sub = self.sh['user'].cell(_i + 2, 10)
                                ur9_sub.value = ur9_sub.value + 1

                    if grp_found != 0:
                        reorg_cache.update({ur3.value: found_subgrp})

                    if grp_found == 0:
                        for _i in range(self.ev[0]):

                            ur4_sub = self.sh['user'].cell(_i + 2, 5)
                            ur3_sub = self.sh['user'].cell(_i + 2, 4)
                            # ur5_sub = self.sh['user'].cell(_i + 2, 6)
                            ur8_sub = self.sh['user'].cell(_i + 2, 9)
                            if new_ur4 == 0:
                                if ur4_sub.value == 4 and ur8_sub.value not in pass_over:
                                    found_subgrp = ur3_sub.value
                                    # old_subgroup = ur3.value
                                    ur4_sub.value = 7
                                    old_ur4 = 4
                                    new_ur4 = 7
                                    _path = 1

                            elif ur4_sub.value == old_ur4 and ur8_sub.value not in pass_over:
                                if ur3_sub.value == found_subgrp:
                                    ur4_sub.value = new_ur4
                        reorg_cache.update({ur3.value: found_subgrp})
                else:
                    new_ur4 = 0

                if invalid_loop == base_ur4:
                    loop_reset = True

                if ur3.value in reorg_cache:
                    found_subgrp = reorg_cache[ur3.value]
                    loop_reset = True

                if _path == 2:
                    ur4.value = new_ur4
                    ur3.value = found_subgrp
                    ur5 = self.sh['user'].cell(i + 2, 6)
                    ur5.value = 'valid'
                    ur8.value = 'reorg'
                    ur9 = self.sh['user'].cell(i + 2, 10)
                    ur9.value = ur9.value + 1

                if _path == 1:
                    ur4.value = new_ur4
                    ur3 = self.sh['user'].cell(i + 2, 4)
                    ur3.value = found_subgrp
                    ur5 = self.sh['user'].cell(i + 2, 6)
                    ur5.value = 'valid'
                    ur8.value = 'reorg'
                    ur9 = self.sh['user'].cell(i + 2, 10)
                    ur9.value = ur9.value + 1

                if loop_reset:
                    invalid_loop = 0
                    loop_reset = False

    self.save_to_excel('user')

    self._checksum(7)


def sys_func_8(self):
    """"
    Reorg Stage 4
    """

    prob = round(random.uniform(0, 1), 2)
    if self.ev[2] > prob:
        self.sy_rec_r[16].value = 'yes'
    elif self.ev[2] < prob:
        self.sy_rec_r[16].value = "no"
        self.sy_rec_r[17].value = self.sy_rec_r[2].value
    self.save_to_excel('system')

    #################
    # ___SyFunc8.5___
    #################
    self.assign_variables()
    """"
    Reorg Stage 4.5
    """
    self.sy_rec_r[11].value = self.sy_rec_r[5].value * self.sy_rec_r[19].value
    self.sy_rec_r[13].value = self.sy_rec_r[6].value * self.sy_rec_r[19].value
    self.save_to_excel('system')


def sys_func_9(self):
    """"
    Reorg Stage 5
    """

    try:
        self.sy_rec_r[2].value = float(self.ev[9]) / self.sy_rec_r[1].value
    except ZeroDivisionError:
        pass

    try:
        self.sy_rec_r[14].value = self.sy_rec_r[9].value + self.sy_rec_r[11].value + self.sy_rec_r[13].value
    except ZeroDivisionError:
        pass

    try:
        self.sy_rec_r[15].value = self.sy_rec_r[14].value / self.sy_rec_r[1].value
    except ZeroDivisionError:
        pass

    for i in range(self.ev[0]):
        us10 = self.sh['user'].cell(i + 2, 11)
        us11 = self.sh['user'].cell(i + 2, 12)
        if us10.value != 0:
            us11.value = self.sy_rec_r[2].value + self.sy_rec_r[15].value - us10.value
            us10.value = 0
        else:
            sr18 = self.sy_rec_r[18].value
            us11.value = self.sy_rec_r[2].value + self.sy_rec_r[15].value - sr18 if sr18 is not None else 0
    self.sy_rec_r[19].value = self.sy_rec_r[2].value + self.sy_rec_r[15].value
    self.save_to_excel('user')
    self.save_to_excel('system')