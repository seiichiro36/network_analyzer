import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
from characteristic_impedance import Characteristic_impedance
from measurements_transform import Open, Short

fig = plt.figure(figsize=(12, 8))
# Frequency1 = np.linspace(60000, 30000000, 501)
#np.linespaceからnp.arangeに変更
Frequency = np.arange(60000, 30000001, 59880)

open = Open("OPEN.CSV")
open_complex_data = open.open_parameter()

short = Short("SHORT.CSV")
short_complex_data = short.short_parameter()

data = Characteristic_impedance(open_complex_data[2], short_complex_data[2])

characteristic_impedance = data.characteristic_impedance()


ax1 = fig.add_subplot(2, 2, 1)
ax1.set_xlabel("(a)   Frequency [Hz]")
ax1.set_ylabel("Real-Impedance [Ω]")

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_xlabel("(b)   Frequency [Hz]")
ax2.set_ylabel("Real-Impedance [Ω]")

ax3 = fig.add_subplot(2, 2, 3)
ax3.set_xlabel("(c)   Frequency [Hz]")
ax3.set_ylabel("Real-Impedance [Ω]")

ax4 = fig.add_subplot(2, 2, 4)
ax4.set_xlabel("(d)   Frequency [Hz]")
ax4.set_ylabel("Real-Impedance [Ω]")

ax1.plot(Frequency, open_complex_data[0], color="red" )
ax1.plot(Frequency, open_complex_data[1], color="blue")
ax2.plot(Frequency, short_complex_data[0], color="red")
ax2.plot(Frequency, short_complex_data[1], color="blue")
ax3.plot(Frequency, characteristic_impedance[0], color="red")
ax4.plot(Frequency, characteristic_impedance[1], color="blue")

fig.tight_layout()


ax1.ticklabel_format(style='plain',axis='x')
ax2.ticklabel_format(style='plain',axis='x')

ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax1.ticklabel_format(style="sci",  axis="x",scilimits=(6, 6))
ax2.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax2.ticklabel_format(style="sci",  axis="x",scilimits=(6, 6))
ax3.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax3.ticklabel_format(style="sci",  axis="x",scilimits=(6, 6))
ax4.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax4.ticklabel_format(style="sci",  axis="x",scilimits=(6, 6))

ax1.set_xlim([60000, 30000000])
ax2.set_xlim([60000, 30000000])
ax3.set_xlim([60000, 30000000])
ax4.set_xlim([60000, 30000000])

x_formatter = ScalarFormatter(useOffset=False)
ax1.yaxis.set_major_formatter(x_formatter)

plt.show()
