from tkinter import *
import os
app=Tk()
app.title("Gui")
app.geometry('400x225')

main=Frame(app)
main.pack(side=TOP)
m_path=Entry(main)
m_path.pack(side=LEFT)
run=Button(main, text="Run", command=lambda :os.system(f"python main.py {m_path.get()}"))
run.pack()

analysis=Frame(app)
analysis.pack(side=BOTTOM)
a_path=Entry(analysis)
a_path.pack(side=LEFT)
run=Button(analysis, text="Run", command=lambda :os.system(f"python analysis.py {a_path.get()}"))
run.pack()
app.mainloop()
