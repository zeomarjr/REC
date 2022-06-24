import tkinter
from tkinter import *


root = Tk()
root.title('CADASTRO DE ESTOQUE')
opcoes_list = ['Opção 1', 'Opção 2', 'Opção 3']
value_inside = tkinter.StringVar(root)
value_inside.set('SELECIONAR')


fr1 = LabelFrame(root)
fr2 = LabelFrame(root)
fr3 = LabelFrame(root)
fr4 = LabelFrame(root)

q_menu = tkinter.OptionMenu(fr2, value_inside, *opcoes_list)

# geometria
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


# criar os widgets frame 1
lb0_fr1 = Label(fr1, text='CADASTRO DE ESTOQUE', font='Arial 25', fg='red', bg='black')
but1_fr1 = Button(fr1, text='Cadastrar Peças', font='Arial 16', fg='black', command=lambda: [fr1.pack_forget(), fr2.pack()])
but2_fr1 = Button(fr1, text='Listar Peças', font='Arial 16', fg='black', command=lambda: [fr1.pack_forget(), fr4.pack()])

# criar os widgets frame 2
lb1_fr2 = Label(fr2, text='Cód. do Produto', font='Arial 16', fg='black')
ent1_fr2 = Entry(fr2, font='Arial 16')
lb2_fr2 = Label(fr2, text='Descrição do Produto', font='Arial 16', fg='black')
ent2_fr2 = Entry(fr2, font='Arial 16')
lb3_fr2 = Label(fr2, text='Fabricante', font='Arial 16', fg='black')
but3_fr2 = Button(fr2, text='Cadastrar Fabricante', font='Arial 16', command=lambda: [fr3.pack()])
lb4_fr2 = Label(fr2, text='Quantidade', font='Arial 16', fg='black')
ent4_fr2 = Entry(fr2, font='Arial 16')
lb5_fr2 = Label(fr2, text='Valor', font='Arial 16', fg='black')
ent5_fr2 = Entry(fr2, font='Arial 16')
but4_fr2 = Button(fr2, text='Finalizar Cadastro', font='Arial 16', fg='black')
but5_fr2 = Button(fr2, text='Voltar', font='Arial 16', fg='black', command=lambda: [fr2.pack_forget(), fr1.pack()])

# criar os widgets frame 3
lb6_fr3 = Label(fr3, text='Cadastro Fabricante', font='Arial 16', fg='red')
ent6_fr3 = Entry(fr3, font='Arial 16')
but6_fr3 = Button(fr3, text='Cadastrar', font='Arial 16', fg='black', command=lambda: [fr3.pack_forget(), fr2.pack()])

# criar os widgets frame 4
lb7_fr4 = Label(fr4, text='Consultar Estoque', font='Arial 16', fg='red')
ent7_fr4 = Entry(fr4, font='Arial 16')
but7_fr4 = Button(fr4, text='Listar', font='Arial 16', fg='black')
but8_fr4 = Button(fr4, text='Voltar', font='Arial 16', fg='black', command=lambda: [fr4.pack_forget(), fr1.pack()])


# Frame Pack
fr1.pack()


# frame1
lb0_fr1.grid(row=1, column=1, sticky=NSEW)
but1_fr1.grid(row=3, column=1, columnspan=2, sticky=NSEW)
but2_fr1.grid(row=4, column=1, columnspan=2, sticky=NSEW)

# frame2
lb1_fr2.grid(row=2, column=0, sticky=NSEW)
ent1_fr2.grid(row=2, column=1, sticky=NSEW)
lb2_fr2.grid(row=3, column=0, sticky=NSEW)
ent2_fr2.grid(row=3, column=1, sticky=NSEW)
lb3_fr2.grid(row=4, column=0, sticky=NSEW)
q_menu.grid(row=4, column=1, sticky=NSEW)
but3_fr2.grid(row=4, column=2, sticky=NSEW)
lb4_fr2.grid(row=5, column=0, sticky=NSEW)
ent4_fr2.grid(row=5, column=1, sticky=NSEW)
lb5_fr2.grid(row=5, column=2, columnspan=1, sticky=NSEW)
ent5_fr2.grid(row=5, column=3, columnspan=1, sticky=NSEW)
but4_fr2.grid(row=7, column=1, sticky=NSEW)
but5_fr2.grid(row=7, column=2, sticky=NSEW)

# frame3
lb6_fr3.grid(row=1, column=0, sticky=NSEW)
ent6_fr3.grid(row=2, column=0, sticky=NSEW)
but6_fr3.grid(row=2, column=1, sticky=NSEW)

# frame4
lb7_fr4.grid(row=1, column=0, sticky=NSEW)
ent7_fr4.grid(row=2, column=0, sticky=NSEW)
but7_fr4.grid(row=2, column=1, sticky=NSEW)
but8_fr4.grid(row=3, column=1, sticky=NSEW)

root.mainloop()
