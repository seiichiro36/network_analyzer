from Impedance_by_propagation_constant import x_actual, y_actual, x_lossless, y_lossless
import matplotlib.pyplot  as plt
import numpy as np 
from characteristic_impedance import Characteristic_impedance
from matplotlib.ticker import ScalarFormatter
from measurements_transform import Open, Short

open = Open("OPEN.CSV")
open_complex_data = open.open_parameter()

short = Short("SHORT.CSV")
short_complex_data = short.short_parameter()


fig = plt.figure(figsize=(12, 8))
# Frequency1 = np.linspace(60000, 30000000, 501)
# np.linespaceからnp.arangeに変更
Frequency = np.arange(60000, 30000001, 59880)


# TODO: 変数の名前
characteristic_impedance = Characteristic_impedance(open_complex_data[2], short_complex_data[2])
characteristic_impedance_by_gamma_on_actual = Characteristic_impedance(x_actual, y_actual)
characteristic_impedance_by_gamma_on_lossless = Characteristic_impedance(x_lossless, y_lossless)


ax1 = fig.add_subplot(2, 1, 1)
ax1.set_xlabel("Frequency [Hz]")
ax1.set_ylabel("Characteristic Impedance real-part[Ω]")

ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlabel("Frequency [Hz]")
ax2.set_ylabel("Characteristic Impedance imag-part[Ω]")


ax1.plot(Frequency, characteristic_impedance_by_gamma_on_actual.characteristic_impedance()[0], color="red", label="calcurated waveform by gamma real on actual" )
ax1.plot(Frequency, characteristic_impedance_by_gamma_on_lossless.characteristic_impedance()[0], color="blue", label="calcurated waveform by gamma real on lossless")
ax1.plot(Frequency, characteristic_impedance.characteristic_impedance()[0], color="green", label="original waveform", ls="dashed")

ax2.plot(Frequency, characteristic_impedance_by_gamma_on_actual.characteristic_impedance()[1], color="red", label="calcurated waveform by gamma real on actual")
ax2.plot(Frequency, characteristic_impedance_by_gamma_on_lossless.characteristic_impedance()[1], color="blue", label="calcurated waveform by gamma real on lossless")
ax2.plot(Frequency, characteristic_impedance.characteristic_impedance()[1], color="green", label="original waveform", ls="dashed")


fig.tight_layout()

ax1.ticklabel_format(style='plain', axis='x')

ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax1.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))

ax2.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax2.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))
# ax2.ticklabel_format(style="sci",  axis="y", scilimits=(-12, -12))


ax1.set_xlim([60000, 30000000])
ax2.set_xlim([60000, 30000000])
# ax2.set_ylim([-1, 1])

x_formatter = ScalarFormatter(useOffset=False)
ax1.yaxis.set_major_formatter(x_formatter)

ax1.legend(loc='lower left')  # 凡例

# plt.savefig('./figure/fig1.pdf')

plt.show()

