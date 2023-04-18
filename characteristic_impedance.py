from measurements_transform import Open, Short
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


open = Open("OPEN.CSV")
open_complex_data = open.open_parameter()

short = Short("SHORT.CSV")
short_complex_data = short.short_parameter()


class Characteristic_impedance:
    def __init__(self, open_complex_data, short_complex_data) -> None:
        self.open_complex_data = open_complex_data
        self.short_complex_data = short_complex_data

    def characteristic_impedance(self):
        characteristic_impedance = []

        def calc(a, b):
            return np.sqrt(a*b)

        for k in range(len(self.open_complex_data)):
            characteristic_impedance.append(
                calc(self.open_complex_data[k], self.short_complex_data[k]))

        characteristic_impedance_real = np.array(characteristic_impedance).real
        characteristic_impedance_imag = np.array(characteristic_impedance).imag

        return characteristic_impedance_real, characteristic_impedance_imag


fig = plt.figure(figsize=(12, 8))
# Frequency1 = np.linspace(60000, 30000000, 501)
# np.linespaceからnp.arangeに変更
Frequency = np.arange(60000, 30000001, 59880)

characteristic_impedance = Characteristic_impedance(open_complex_data[2], short_complex_data[2])

ax1 = fig.add_subplot(2, 1, 1)
ax1.set_xlabel("Frequency [Hz]")
ax1.set_ylabel("[Ω]")

if __name__ == "__main__":
    ax1.ticklabel_format(style='plain', axis='x')

    ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax1.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))

    ax1.set_xlim([60000, 30000000])

    x_formatter = ScalarFormatter(useOffset=False)
    ax1.yaxis.set_major_formatter(x_formatter)

    ax1.legend(loc='lower left')  # 凡例

    ax1.plot(Frequency, characteristic_impedance.characteristic_impedance()[0], color="red",
             label="calcuration wave by gamma real")

    ax1.legend(loc='lower left')  # 凡例

    plt.show()


# if __name__ == "__main__":
#     ax1.ticklabel_format(style='plain', axis='x')

#     ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
#     ax1.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))

#     ax1.set_xlim([60000, 30000000])

#     x_formatter = ScalarFormatter(useOffset=False)
#     ax1.yaxis.set_major_formatter(x_formatter)
