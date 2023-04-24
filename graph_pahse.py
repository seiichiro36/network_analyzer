import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

from measurements_transform import Open, Short
from propagation_constant import Propagation_constant
from theoretical import beta

# Frequency1 = np.linspace(60000, 30000000, 501)
# np.linespaceからnp.arangeに変更
Frequency = np.arange(60000, 30000001, 59880)


def linear_transform(phase_constant):
    phase = []
    for i in range(0, len(phase_constant)):
        phase.append(phase_constant[i])
    Frequency_gamma = []
    for i in range(0, len(Frequency)):
        Frequency_gamma.append(Frequency[i])

    initial_point = phase[0]
    start_point = []
    end_point = []
    final_point = phase[-1]

    total_break_point = []

    for j in range(0, len(phase_constant)):
        # out of range対策
        if j+1 == len(phase_constant):
            break
        # 位相の一番下のところ
        if phase[j] > phase[j+1]:
            start_point.append(phase[j+1])
            end_point.append(phase[j])

    between_phase = phase[phase.index(
        initial_point): phase.index(start_point[0])]

    break_point = phase.index(start_point[0])
    total_break_point.append(break_point)
    del Frequency_gamma[break_point]

    for m in range(len(end_point) - 1):
        amount_of_change = start_point[m]
        between_start_end = phase[phase.index(
            start_point[m])+1: phase.index(end_point[m+1])+1]
        between_start_end = between_start_end + \
            between_phase[-1] + amount_of_change * -1
        between_phase.extend(between_start_end)

        break_point = phase.index(start_point[m+1])
        total_break_point.append(break_point)
        del Frequency_gamma[break_point]

    amount_of_change = start_point[-1]
    between_start_end_final = phase[phase.index(
        start_point[-1])+1: phase.index(final_point)+1]
    between_start_end_final = between_start_end_final + \
        between_phase[-1] + amount_of_change*-1
    between_phase.extend(between_start_end_final)

    phase = between_phase

    return Frequency_gamma, phase, total_break_point, start_point, end_point


open = Open("OPEN.CSV")
open_complex_data = open.open_parameter()

short = Short("SHORT.CSV")
short_complex_data = short.short_parameter()

data = Propagation_constant(open_complex_data[2], short_complex_data[2], 10.8)

propagation_constant = data.propagation_constant()

phase_constant = propagation_constant[1]

Frequency_gamma = linear_transform(phase_constant)[0]
phase_constant_linear = linear_transform(phase_constant)[1]

start_point = linear_transform(phase_constant)[3]

end_point = linear_transform(phase_constant)[4]




beta1 = beta[0: phase_constant.tolist().index(start_point[0])]
Frequency1 = Frequency[0: phase_constant.tolist().index(start_point[0])]

beta2 = beta[phase_constant.tolist().index(start_point[0]): phase_constant.tolist().index(start_point[1])] - beta[phase_constant.tolist().index(start_point[0])] - beta[phase_constant.tolist().index(start_point[0])]
    
Frequency2 = Frequency[phase_constant.tolist().index(
    start_point[0]): phase_constant.tolist().index(start_point[1])]

beta3 = beta[phase_constant.tolist().index(start_point[1]): phase_constant.tolist().index(start_point[2])] - beta[phase_constant.tolist().index(start_point[1])] - beta[phase_constant.tolist().index(start_point[0])]
Frequency3 = Frequency[phase_constant.tolist().index(
    start_point[1]): phase_constant.tolist().index(start_point[2])]

beta4 = beta[phase_constant.tolist().index(start_point[2]): -1] - beta[phase_constant.tolist(
).index(start_point[2])] - beta[phase_constant.tolist().index(start_point[0])]
Frequency4 = Frequency[phase_constant.tolist().index(start_point[2]): -1]


beta = beta1.tolist() + beta2.tolist() + beta3.tolist() + beta4.tolist()
Frequency_aa = Frequency1.tolist() + Frequency2.tolist() + Frequency3.tolist() + Frequency4.tolist()

if __name__== "__main__":
    fig = plt.figure(figsize=(12, 8))
    
    ax2 = fig.add_subplot(1, 1, 1)
    ax2.set_xlabel("(b)   Frequency [Hz]")
    ax2.set_ylabel("[rad/m]")
    
    ax2.plot(Frequency, phase_constant, color="red", label="phase constant from actual data")
    ax2.plot(Frequency_gamma, phase_constant_linear, color="hotpink")
    ax2.plot(Frequency, beta, color="green")

    ax2.plot(Frequency1, beta1, color="blue", label="phase constant from the form (1)")
    ax2.plot(Frequency2, beta2, color="blue")
    ax2.plot(Frequency3, beta3, color="blue")
    ax2.plot(Frequency4, beta4, color="blue")


    fig.tight_layout()

    ax2.ticklabel_format(style='plain', axis='x')

    ax2.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax2.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))
    
    ax2.set_xlim([60000, 30000000])
    
    x_formatter = ScalarFormatter(useOffset=False)
    
    ax2.legend(loc='lower left')  # 凡例

    plt.show()

    # fig.savefig("./figure/phase.pdf")