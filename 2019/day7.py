import IntCode

inputs = ""
f = open("day7_input.txt", "r")
for line in f:
    inputs += line
f.close()
inputs = inputs.split(',')
numbers = []
for i in inputs:
    numbers.append(int(i))

amplitudes = []
phases = [i for i in range(5, 10)]
for aa in phases:
    for bb in phases:
        if bb == aa:
            continue
        for cc in phases:
            if cc == aa or cc == bb:
                continue
            for dd in phases:
                if dd == cc or dd == bb or dd == aa:
                    continue
                for ee in phases:
                    if ee == dd or ee == cc or ee == bb or ee == aa:
                        continue
                    phase_setting = [aa, bb, cc, dd, ee]
                    amp_inputs = [0]
                    for op in range(5):
                        out = IntCode.opcode(numbers, [phase_setting[op], amp_inputs[op]])
                        amp_inputs.append(out)
                    # print(amp_inputs)
                    amplitudes.append(amp_inputs[-1])
amplitudes.sort()
print(amplitudes[-1])

