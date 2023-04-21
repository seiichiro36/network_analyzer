import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
from measurements_transform import Open, Short
from propagation_constant import Propagation_constant
from actual_damping import actual_data

fig = plt.figure(figsize=(12, 8))
# Frequency1 = np.linspace(60000, 30000000, 501)
# np.linespaceからnp.arangeに変更
Frequency = np.arange(60000, 30000001, 59880)

open = Open("OPEN.CSV")
open_complex_data = open.open_parameter()

short = Short("SHORT.CSV")
short_complex_data = short.short_parameter()

data = Propagation_constant(open_complex_data[2], short_complex_data[2], 10.8)

propagation_constant = data.propagation_constant()

damping_constant = propagation_constant[0]

ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel("(b)   Frequency [Hz]")
ax1.set_ylabel("[Np/m]")

ax1.plot(Frequency, damping_constant, color="red")
ax1.plot(Frequency, actual_data, color="blue")



fig.tight_layout()

ax1.ticklabel_format(style='plain', axis='x')

ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax1.ticklabel_format(style="sci",  axis="x", scilimits=(6, 6))

ax1.set_xlim([60000, 30000000])

x_formatter = ScalarFormatter(useOffset=False)
ax1.yaxis.set_major_formatter(x_formatter)

ax1.legend(loc='lower left')  # 凡例

plt.show()

# fig.savefig("./figure/phase.pdf")
