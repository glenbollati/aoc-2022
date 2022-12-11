#!/usr/bin/python3
monkeys = []

class Monkey:
    def __init__(self):
        self.items = []
        self.op_type = None
        self.op_val = None
        self.test = None
        self.monkey_true = None
        self.monkey_false = None
        self.inspections = 0

    def run_turn(self):
        for item in self.items:
            self.inspections += 1
            old_item = item
            if self.op_type == '*':
                if self.op_val == "old":
                    item = (item * item) // 3
                else:
                    item = (item * int(self.op_val)) // 3
            elif self.op_type == '+':
                if self.op_val == "old":
                    item = (item + item) // 3
                else:
                    item = (item + int(self.op_val)) // 3
            else:
                panic()

            if item % self.test == 0:
                monkeys[self.monkey_true].items.append(item)
                self.items.remove(old_item)
            else:
                monkeys[self.monkey_false].items.append(item)
                self.items.remove(old_item)

    def run_turn_v2(self):
        for item in self.items:
            self.inspections += 1
            old_item = item
            if self.op_type == '*':
                if self.op_val == "old":
                    item = (item * item)
                else:
                    item = (item * int(self.op_val))
            elif self.op_type == '+':
                if self.op_val == "old":
                    item = (item + item)
                else:
                    item = (item + int(self.op_val))
            else:
                panic()

            if item % self.test == 0:
                monkeys[self.monkey_true].items.append(item)
                self.items.remove(old_item)
            else:
                monkeys[self.monkey_false].items.append(item)
                self.items.remove(old_item)

def run_round(v2):
    for m in monkeys:
        if len(m.items) == 0:
            continue
        while (len(m.items) > 0):
            if v2:
                m.run_turn_v2()
            else:
                m.run_turn()

monkey = None

lines = open("11.txt").readlines()
for line in lines:
    if line.isspace():
        if monkey is not None:
            monkeys.append(monkey)
        continue

    if line.startswith("Monkey"):
        monkey = Monkey()
        continue

    spl = line.replace(",", "").strip().split()
    if spl[0] == "Starting":
        for item in spl[2:]:
            monkey.items.append(int(item))
    elif spl[0] == "Operation:":
        monkey.op_type = spl[4]
        monkey.op_val  = spl[5]
    elif spl[0] == "Test:":
        monkey.test = int(spl[3])
    elif spl[1] == "true:":
        monkey.monkey_true = int(spl[5])
    elif spl[1] == "false:":
        monkey.monkey_false = int(spl[5])
    else:
        assert False

monkeys.append(monkey)

# part 1
for i in range(20):
    run_round(False)

inspections = []
for i in range(len(monkeys)):
    inspections.append(monkeys[i].inspections)

inspections.sort(reverse = True)

print(inspections[0] * inspections[1]) # 55216

# part 2
for i in range(10000):
    run_round(True)

inspections = []
for i in range(len(monkeys)):
    inspections.append(monkeys[i].inspections)

inspections.sort(reverse = True)

print(inspections[0] * inspections[1]) # 55216
# 14398080063 too high
