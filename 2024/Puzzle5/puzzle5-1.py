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

    for update in updates:
        valid = True
        for rule in rules:
            if not check_order(rule, update):
                valid = False
        if valid:
            sum += update[int(len(update)/2)]

    print(sum)

main()