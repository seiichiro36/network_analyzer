from compare_actual_theoritical import x, y
import matplotlib.pyplot  as plt
import numpy as np 
from characteristic_impedance import Characteristic_impedance
from matplotlib.ticker import ScalarFormatter


fig = plt.figure(figsize=(12, 8))
# Frequency1 = np.linspace(60000, 30000000, 501)
# np.linespaceからnp.arangeに変更
Frequency = np.arange(60000, 30000001, 59880)

characteristic_impedance_by_gamma = Characteristic_impedance(x, y)


ax1 = fig.add_subplot(2, 1, 1)
ax1.set_xlabel("Frequency [Hz]")
ax1.set_ylabel("[Ω]")

ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlabel("Frequency [Hz]")
ax2.set_ylabel("[Ω]")


ax1.plot(Frequency, characteristic_impedance_by_gamma.characteristic_impedance()[0], color="red", label="calcuration wave by gamma real")

ax2.plot(Frequency, characteristic_impedance_by_gamma.characteristic_impedance()[1], color="red", label="calcuration wave by gamma imag")

fig.tight_layout()

ax1.ticklabel_format(style='plain', axis='x')

ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax1.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))

ax1.set_xlim([60000, 30000000])

x_formatter = ScalarFormatter(useOffset=False)
ax1.yaxis.set_major_formatter(x_formatter)

ax1.legend(loc='lower left')  # 凡例

plt.show()