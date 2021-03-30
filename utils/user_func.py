def get_orig_subgroup(self, index):
    # UsRec1
    return self.sh['user'].cell(index + 2, 2).value


def get_remaining_num_orig_subgroup(self, index):
    # UsRec2
    return self.sh['user'].cell(index + 2, 3).value


def set_remaining_num_orig_subgroup(self, index, num):
    # UsRec2
    self.sh['user'].cell(index + 2, 3).value = max(num, 0)


def get_cur_subgroup(self, index):
    # UsRec3
    return self.sh['user'].cell(index + 2, 4).value


def set_cur_subgroup(self, index, num):
    # UsRec3
    self.sh['user'].cell(index + 2, 4).value = num


def get_remaining_num_cur_subgroup(self, index):
    # UsRec4
    return self.sh['user'].cell(index + 2, 5).value


def set_remaining_num_cur_subgroup(self, index, num):
    # UsRec4
    self.sh['user'].cell(index + 2, 5).value = max(num, 0)


def get_subgroup_status(self, index):
    # UsRec5
    return self.sh['user'].cell(index + 2, 6).value


def set_subgroup_status(self, index, state):
    # UsRec5
    self.sh['user'].cell(index + 2, 6).value = state


def get_primary_role(self, index):
    # UsRec6
    return self.sh['user'].cell(index + 2, 7).value


def set_primary_role(self, index, role):
    # UsRec6
    self.sh['user'].cell(index + 2, 7).value = role


def get_secondary_role(self, index):
    # UsRec7
    return self.sh['user'].cell(index + 2, 8).value


def get_cur_status(self, index):
    # UsRec8
    return self.sh['user'].cell(index + 2, 9).value


def set_cur_status(self, index, state):
    # UsRec8
    self.sh['user'].cell(index + 2, 9).value = state


def get_invalid_refund_available(self, index):
    # UsRec10
    return self.sh['user'].cell(index + 2, 11).value


def set_invalid_refund_available(self, index, val):
    # UsRec10
    self.sh['user'].cell(index + 2, 11).value = val


def get_total_payment_specific_user(self, index):
    # UsRec11
    return self.sh['user'].cell(index + 2, 12).value


def set_total_payment_specific_user(self, index, val):
    # UsRec11
    self.sh['user'].cell(index + 2, 12).value = val


def get_payable(self, index):
    # UsRec12
    return self.sh['user'].cell(index + 2, 13).value


def set_payable(self, index, state):
    # UsRec12
    self.sh['user'].cell(index + 2, 13).value = state


def get_defect_count(self, index):
    # UsRec13
    return self.sh['user'].cell(index + 2, 14).value


def set_defect_count(self, index, num):
    # UsRec13
    self.sh['user'].cell(index + 2, 14).value = num
