import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
from actual_damping import actual_data
import itertools



#スケール用関数
def change(value):
    t = float(value)
    y = np.sqrt(t * x)
    line.set_ydata(y)
    canvas.draw()
    
root = tkinter.Tk()
root.title("matplotlib 埋め込み")

#グラフデータ
x = np.linspace(0, 300000000, 501)
y = np.sqrt(x)

y1 = actual_data
y1 = list(itertools.chain.from_iterable(y1))


#グラフ用オブジェクト生成
fig = Figure(figsize=(12, 8))   #Figure
ax = fig.add_subplot(1, 1, 1)           #Axes
line, = ax.plot(x, y)                  #2DLine
ax.plot(x, y1)                 


#Figureを埋め込み
canvas = FigureCanvasTkAgg(fig, root)

canvas.get_tk_widget().pack()

#ツールバーを表示
toolbar=NavigationToolbar2Tk(canvas, root)
ax.set_xlim([0, 300000000])
# ax.set_ylim([0, 0.08])

#スケール
s = tkinter.Scale(
    root,
    orient="horizontal",    #方向
    command=change,  #調整時に実行
    )
s.pack()

root.mainloop()
