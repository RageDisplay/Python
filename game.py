from tkinter import *
import random as rdm
import numpy as np
import matplotlib.pyplot as plt

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        self.win = self.drow = self.lose = self.count = 0
        firstbutton = Button(root, text="Камень",bg="#8D6E63", font=("Calibri", 50),  command=lambda btn=1: self.btn_click(btn))
        secondbutton = Button(root, text="Ножницы", bg="#9E9E9E", font=("Calibri", 50), command=lambda btn=2: self.btn_click(btn))
        thirdbutton = Button(root, text="Бумага",bg="#EFEBE9", font=("Calibri", 50), command=lambda btn=3: self.btn_click(btn))
        fourthbutton = Button(root, text="Перезапуск",bg="#A7FFEB", font=("Calibri", 25), command=lambda btn=0: self.btn_click(btn))
        fifthbutton = Button(root,text="График", bg="#A7FFEB", font=("Calibri", 25), command=lambda btn=4: self.btn_click(btn))
        
        firstbutton.place(x=10, y=200, width=300, height=70)
        secondbutton.place(x=350, y=200, width=300, height=70)
        thirdbutton.place(x=690, y=200, width=300, height=70)
        fourthbutton.place(x=10, y = 450, width=170, height=35)
        fifthbutton.place(x=825, y=450, width=170, height=35 )

        self.lbl = Label(root, text="Игра начинается", bg="#B2DFDB", font=("Calibri", 30, "bold"))
        self.lbl.place(x=355, y=100)
        
        self.lbl2 = Label(root, justify="left", font=("Calibri", 20), text=f"Побед: {self.win}\nПроигрышей:"f" {self.lose}\nНичей: {self.drow}",bg="#E1BEE7")
        self.lbl2.place(x=5, y=5)
        
        self.lbl3 = Label(root, text="Камень, ножницы или бумага ?", bg="#66FFCC", font=("Calibri", 30, "bold"))
        self.lbl3.place(x=220, y=20)
        
    def btn_click(self, choise):
        enemy_choise = rdm.randint(1, 3)
        i = np.arange(1,self.count+1)
        j = np.empty((self.count), dtype=int)
        
        if (choise == 4):            
            plt.title("График")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.plot(i, j, color ="green")
            plt.show()

        elif (choise == enemy_choise):
            self.drow += 1
            self.count +=1
            j = np.append(j,[0])
            self.lbl.configure(text="Ничья", bg="#FFC233")
            self.lbl.place(x=440, y=100)
            
        elif (choise == 1 and enemy_choise == 2) or (choise == 2 and enemy_choise == 3) or (choise == 3 and enemy_choise == 1):
            self.win += 1
            self.count +=1
            j = np.append(j,[1])
            self.lbl.configure(text="Победа", bg="#8BC34A")
            self.lbl.place(x=430, y=100)
            
        elif (choise == 0):
            self.win = self.drow = self.lose = self.count = 0
            
        else:
            self.lose += 1
            self.count +=1
            j = np.append(j,[-1])
            self.lbl.configure(text="Проигрыш", bg ="#D50000")
            self.lbl.place(x=410, y=100)

        self.lbl2.configure(text=f"Побед: {self.win}\nПроигрышей:"f" {self.lose}\nНичей: {self.drow}")
        del enemy_choise

if __name__ == '__main__':
    root = Tk()
    root.geometry("1000x500")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root["bg"] = "#FFE0B2"
    app = Main(root)
    app.pack()
    root.mainloop()