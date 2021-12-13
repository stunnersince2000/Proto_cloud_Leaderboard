from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1080x800')

root.title("LeaderBoards")
root.config(bg = 'light yellow')

Main_frame=Frame(root)
Main_frame.pack(fill=BOTH,expand=1)

My_canvas=Canvas(Main_frame)
My_canvas.pack(side=LEFT,fill=BOTH,expand=1)

scrollbar = ttk.Scrollbar(Main_frame, orient=VERTICAL, command=My_canvas.yview)
scrollbar.pack( side = RIGHT, fill = Y )


My_canvas.configure(yscrollcommand=scrollbar.set)
My_canvas.bind('<Configure>', lambda e: My_canvas.configure(scrollregion = My_canvas.bbox("all")))

second_frame = Frame(My_canvas)

My_canvas.create_window((0,0), window=second_frame, anchor="nw")

#INPUT AND OUTPUT TEXT WIDGET
k=0
a=50
ind=1

#start
Label(second_frame, text = "LEADER BOARDS", font = "Magneto 20", bg='light yellow').grid(row=0, column=3, pady=10, padx=10)
Label(second_frame,text ="ENTER CANDIDATE DETAILS", font = 'arial 15 bold',bg='light pink').grid(row=3, column=0, pady=10, padx=10)
Label(second_frame,text ="CANDIDATE "+str(ind), font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 2,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered.grid(row=a + k + 3, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 4, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality.grid(row=a + k + 7, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#end

#2
Label(second_frame, text = "LEADER BOARDS", font = "Magneto 20", bg='light yellow').grid(row=0, column=3, pady=10, padx=10)
Label(second_frame,text ="ENTER CANDIDATE DETAILS", font = 'arial 15 bold',bg='light pink').grid(row=3, column=0, pady=10, padx=10)
Label(second_frame,text ="CANDIDATE "+str(ind), font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 2,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered.grid(row=a + k + 3, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 4, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality.grid(row=a + k + 7, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#3
Label(second_frame, text = "LEADER BOARDS", font = "Magneto 20", bg='light yellow').grid(row=0, column=3, pady=10, padx=10)
Label(second_frame,text ="ENTER CANDIDATE DETAILS", font = 'arial 15 bold',bg='light pink').grid(row=3, column=0, pady=10, padx=10)
Label(second_frame,text ="CANDIDATE "+str(ind), font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 2,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered.grid(row=a + k + 3, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 4, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality.grid(row=a + k + 7, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1
# print(Input_text_correctly_answered,Input_text_Punctuality,Input_text_Questioning)
trans_btn = Button(root, text = 'SUBMIT\n ==>',font = 'arial 12 bold',pady = 5 ,state="active",bg = 'light blue',relief="ridge", activeforeground = 'purple',activebackground = 'sky blue')
trans_btn.place(x = 487, y = a)



#Using matplotlib for graphs


scrollbar.config( command = My_canvas.yview )
root.mainloop()