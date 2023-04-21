import matplotlib.pyplot as plt
import numpy as np

from actual_damping import actual_data
from graph_pahse import beta, Frequency_aa
from characteristic_impedance import Characteristic_impedance

Frequency = np.arange(60000, 30000001, 59880)
fig = plt.figure(figsize=(12, 8))


actual_data_list = actual_data.tolist()

# TODO: 仮　速攻訂正すべし
del actual_data_list[-1]



complex = np.array(actual_data_list) + np.array(beta) * 1j

Zins = 50 * np.tanh(complex * 10.8)
Zino = 50 / np.tanh(complex * 10.8)


characteristic_impedance_theoritical = Characteristic_impedance(Zins, Zino)


ax1 = fig.add_subplot(2, 2, 1)
ax1.set_xlabel("(b)   Frequency [Hz]")
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_xlabel("(b)   Frequency [Hz]")
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_xlabel("(b)   Frequency [Hz]")


ax1.plot(Frequency_aa, characteristic_impedance_theoritical.characteristic_impedance()[0])
ax2.plot(Frequency_aa, Zins.real)
ax3.plot(Frequency_aa, Zino.real)
plt.show()


