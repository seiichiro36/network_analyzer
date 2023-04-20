import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
from measurements_transform import Open, Short
from propagation_constant import Propagation_constant
from characteristic_impedance import Characteristic_impedance



# Frequency1 = np.linspace(60000, 30000000, 501)
# np.linespaceからnp.arangeに変更
Frequency = np.arange(60000, 30000001, 59880)

open = Open("OPEN.CSV")
open_complex_data = open.open_parameter()

short = Short("SHORT.CSV")
short_complex_data = short.short_parameter()

# 　減衰定数
data = Propagation_constant(open_complex_data[2], short_complex_data[2], 10.8)

propagation_constant = data.propagation_constant()

damping_constant = propagation_constant[0]
# 位相定数
phase_constant = propagation_constant[1]

propagation_constant = damping_constant + phase_constant * 1j

# 短絡・解放した際の送電端インピーダンスより導出した特性インピーダンス
characteristic_impedance = Characteristic_impedance(open_complex_data[2], short_complex_data[2])
characteristic_impedance_complex = characteristic_impedance.characteristic_impedance()[0] + characteristic_impedance.characteristic_impedance()[1] * 1j

x_actual = characteristic_impedance_complex * np.tanh((propagation_constant)*10.8)

y_actual = characteristic_impedance_complex / (np.tanh((propagation_constant) * 10.8))

x_lossless = 50 * np.tanh((propagation_constant)*10.8)

y_lossless = 50 / (np.tanh((propagation_constant) * 10.8))


if __name__ == "__main__":
    fig = plt.figure(figsize=(12, 8))
    
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("[Ω]")

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.set_xlabel("Frequency [Hz]")
    ax2.set_ylabel("[Ω]")

    ax1.plot(Frequency, x.real, color="red", label="calcuration wave")
    ax1.plot(Frequency, short_complex_data[0], color="blue", label="actual wave")
    ax1.plot(Frequency, x.imag, color="red", label="calcuration wave")
    ax1.plot(Frequency, short_complex_data[1], color="blue", label="actual wave")

    ax2.plot(Frequency, y.real, color="red", label="calcuration wave")
    ax2.plot(Frequency, open_complex_data[0], color="blue", label="actual wave")
    ax2.plot(Frequency, y.imag, color="red", label="calcuration wave")
    ax2.plot(Frequency, open_complex_data[1], color="blue", label="actual wave")

    fig.tight_layout()

    ax1.ticklabel_format(style='plain', axis='x')

    ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax1.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))

    ax1.set_xlim([60000, 30000000])

    x_formatter = ScalarFormatter(useOffset=False)
    ax1.yaxis.set_major_formatter(x_formatter)

    ax1.legend(loc='lower left')  # 凡例
    
    ax1.ticklabel_format(style='plain', axis='x')

    ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax1.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))

    ax1.set_xlim([60000, 30000000])

    x_formatter = ScalarFormatter(useOffset=False)
    ax1.yaxis.set_major_formatter(x_formatter)

    ax1.legend(loc='lower left')  # 凡例

    plt.show()
