import re

data = open('input.txt', 'rt')
content = data.read()
content_list = content.split('\n\n')
result = 0

for i in range(len(content_list)):
    line = content_list[i]
    count = line.count(":")

    if count < 7:
        continue
    if count == 8 or (count == 7 and "cid" not in line):
        eyr = int(re.findall('(?<=eyr:).\w*', line)[0])
        if eyr < 2020 or eyr > 2030:
            continue

        byr = int(re.findall('(?<=byr:).\w*', line)[0])
        if byr < 1920 or byr > 2002:
            continue

        # check pid
        if not re.findall('(?<=pid:)\d{9}', line):
            continue

        iyr = int(re.findall('(?<=iyr:).\w*', line)[0])
        if iyr < 2010 or iyr > 2020:
            continue

        hcl = re.findall('(?<=hcl:).\w*', line)[0]
        if not re.findall('#[a-f0-9]{6}', hcl):
            continue

        ecl = re.findall('(?<=ecl:).\w*', line)[0]
        if ecl not in 'amb blu brn gry grn hzl oth':
            continue

        hgt = re.findall('(?<=hgt:).\w*', line)[0]
        if len(hgt) < 4 or (not 'cm' in hgt and not 'in' in hgt):
            continue
        hgt_value = int(re.findall('\d*(?=cm|in)', hgt)[0])
        if not hgt_value:
            continue

        if 'cm' in hgt and (hgt_value < 150 or hgt_value > 193):
            continue
        elif 'in' in hgt and (hgt_value < 59 or hgt_value > 76):
            continue
        result += 1

print(result)
