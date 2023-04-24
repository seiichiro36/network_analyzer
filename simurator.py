import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
from theoretical_propagation_constant import complex

#スケール用関数
def change(value):
    length = float(value)
    Zins = 50 * np.tanh(complex * length)
    Zino = 50 / np.tanh(complex * length)
    line1.set_ydata(Zins)
    line2.set_ydata(Zino)
    canvas.draw()
    
root = tkinter.Tk()
root.title("matplotlib 埋め込み")

#グラフデータ
Frequency = np.arange(60000, 30000001, 59880)
y = 0 * Frequency

# y1 = actual_data
# y1 = list(itertools.chain.from_iterable(y1))


#グラフ用オブジェクト生成
fig = Figure(figsize=(12, 8)) 
ax = fig.add_subplot(1, 1, 1)        
line1, = ax.plot(Frequency, y)                 
line2, = ax.plot(Frequency, y)                 

#Figureを埋め込み
canvas = FigureCanvasTkAgg(fig, root)

canvas.get_tk_widget().pack()

#ツールバーを表示
toolbar=NavigationToolbar2Tk(canvas, root)
# ax.set_xlim([0, 300000000])
ax.set_ylim([0, 1000])

#スケール
s = tkinter.Scale(
    root,
    orient="horizontal",    #方向
    command=change,  #調整時に実行
    width=30,
    length=500,
    from_=0,
    to=30,
    resolution=0.1
    )
s.pack()

root.mainloop()
