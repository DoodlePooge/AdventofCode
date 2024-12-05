class Rule:
  def __init__(self, lead, follow):
    self.lead = lead
    self.follow = follow

def check_order(rule: Rule, update):
    if rule.lead in update and rule.follow in update:
        leadIn = update.index(rule.lead)
        followIn = update.index(rule.follow)

        return leadIn < followIn

    return True

def fix_order(update, rules) -> [int]:
    for rule in rules:
        if rule.lead in update and rule.follow in update:
            leadIn = update.index(rule.lead)
            followIn = update.index(rule.follow)

            if leadIn > followIn:
                update[leadIn], update[followIn] = update[followIn], update[leadIn]
    
    return update

def check_all(updates, rules) -> tuple[[int], [int]]:
    right = []
    wrong = []
    sum = 0

    for update in updates:
        valid = True
        for rule in rules:
            if not check_order(rule, update):
                valid = False
        if valid:
            right.append(update)
        else:
            wrong.append(update)
    
    return right, wrong


def traverse_file(fileName: str) -> tuple[[Rule], [[int]]]:
    file = open(fileName)
    lines = file.readlines()
    rules = []
    updates = []
    rulesDone = False

    for line in lines:
        if line == "\n":
            rulesDone = True
        else:
            if rulesDone:
                chars = line.split(',')
                numbers = [int(num) for num in chars]
                updates.append(numbers)
            else:
                nums = line.split('|')
                rules.append(Rule(int(nums[0]), int(nums[1])))

    return rules, updates


def main():
    rules, updates = traverse_file("input.txt")
    sum = 0

    right, wrong = check_all(updates, rules)
    fixed = []

    while len(wrong) > 0:
        for update in wrong:
            update = fix_order(update, rules)
        
        right, wrong = check_all(wrong, rules)
        fixed += right
    
    for update in fixed:
        sum += update[int(len(update)/2)]

    print(sum)

main()