import matplotlib.pyplot as plt
import numpy as np
score=np.array([[85,76,92], [77,80,65]])
mean_score=np.mean(score, axis=0)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(score[0], label='Student1')
plt.plot(score[1], label='Student2')
plt.plot(mean_score, label='Average')
plt.legend()
plt.grid(True)
labels=['a','b','c','d']
sizes=[35,25,20,20]
plt.pie(sizes, labels=labels, autopct='%1.1f')
plt.show()
from tkinter import *
q='문제'
options=['a', 'b', 'c', 'd', 'e']
w=Tk()
w.title('문제')
w.geometry('450x300')
q_label=Label(w,text=q)
for i in range(5):
    btn=Button(w,text=options[i], width=20)
    btn.pack()
w.mainloop
