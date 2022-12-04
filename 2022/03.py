data = open('03.txt', 'r')
# data = ['vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
# 'ttgJtRGJQctTZtZT',
# 'CrZsJsPPZsGzwwsLwLmpwMDw']

lines = [line.strip() for line in data]
upp_offset = 38
low_offset = 96

sum_errors = 0
sum_badges = 0

def map_ch_to_value(ch):
    val = ord(ch)
    if val >= 97:
        return val - low_offset
    return val - upp_offset

def map_value_to_ch(val):
    if val >= 27:
        return chr(val + upp_offset)
    return chr(val + low_offset)

def match(*args):
    size = len(args)
    values = [0]*size

    for i, input in enumerate(args):
        for ch in input:
            values[i] |= 1 << map_ch_to_value(ch)

    result = values[0]
    for i, value in enumerate(values, 1):
        result &= value

    return bin(result).count("0") - 1


for i in range(0, len(lines), 3):
    elf_a = lines[i]
    elf_b = lines[i+1]
    elf_c = lines[i+2]

    sum_errors += match(elf_a[:len(elf_a)//2], elf_a[len(elf_a)//2:])
    sum_errors += match(elf_b[:len(elf_b)//2], elf_b[len(elf_b)//2:])
    sum_errors += match(elf_c[:len(elf_c)//2], elf_c[len(elf_c)//2:])
    sum_badges += match(elf_a, elf_b, elf_c)

print(sum_errors)
print(sum_badges)
