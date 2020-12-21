with open("input.txt") as inp:
    raw_text = inp.read()

text_sections = raw_text.split('\n\n')
raw_rules = text_sections[0].split('\n')
messages = text_sections[1].split('\n')[:-1]
rule_dict = {}
string_rules = {}
list_rules = {}

for raw_rule in raw_rules:
    if '"' in raw_rule:
        string_rules[raw_rule[:raw_rule.index(':')]] = raw_rule[raw_rule.index(':') + 2:]\
            .replace('"', '')
    elif '|' in raw_rule:
        rule_dict[raw_rule[:raw_rule.index(':')]] = raw_rule[raw_rule.index(':') + 2:].split(' | ')
    else:
        rule_dict[raw_rule[:raw_rule.index(':')]] = [raw_rule[raw_rule.index(':') + 2:]]


def find_valid_strings(rule: str, path: int = 0) -> list:
    try:
        subrule_section = rule_dict[rule][path]
    except IndexError:
        return []
    subrules = subrule_section.split(' ')
    prev_chunks = ['']

    for subrule in subrules:
        if subrule in string_rules:
            chunks = [string_rules[subrule]]
        elif subrule in list_rules:
            chunks = list_rules[subrule]
        else:
            chunks = find_valid_strings(subrule)
            chunks += find_valid_strings(subrule, 1)
            list_rules[subrule] = chunks

        new_chunks = []
        for prev_chunk in prev_chunks:
            for chunk in chunks:
                new_chunks.append(prev_chunk + chunk)
        prev_chunks = new_chunks.copy()
    return prev_chunks


valid_strings = set(find_valid_strings('0'))
valid_messages = 0
for message in messages:
    if message in valid_strings:
        valid_messages += 1
print(valid_messages)
# >>> 149
