from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

#ui PART START

root = Tk()
root.geometry('1080x800')

root.title("LeaderBoards-Dinesh")
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
FinalList=[]



#1

#start
Label(second_frame, text = "LEADER BOARD", font = "arial 20 bold", bg='light yellow').grid(row=0, column=4, pady=10, padx=10)


Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name1 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name1.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered1 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered1.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning1 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning1.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality1 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality1.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1
#end

# #2

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name2 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name2.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered2 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered2.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning2 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning2.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality2 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality2.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#3

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name3 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name3.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered3 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered3.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning3 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning3.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality3 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality3.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#4

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name4 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name4.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered4 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered4.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning4 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning4.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality4 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality4.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#5
Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name5 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name5.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered5 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered5.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning5 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning5.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality5 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality5.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#6


Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name6 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name6.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered6 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered6.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning6 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning6.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality6 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality6.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#7

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name7 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name7.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered7 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered7.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning7 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning7.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality7 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality7.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1
#8

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name8 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name8.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered8 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered8.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning8 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning8.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality8 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality8.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1


#9

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name9 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name9.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered9 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered9.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning9 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning9.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality9 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality9.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#10

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name10 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name10.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered10 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered10.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning10 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning10.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality10 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality10.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#11

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name11 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name11.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered11 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered11.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning11 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning11.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality11 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality11.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1


#12

Label(second_frame,text ="                 ENTER CANDIDATE NAME "+str(ind)+"                 ", font = 'arial 15 bold',bg='light pink').grid(row=a+k+1, column=0, pady=10, padx=10)
Input_text_Name12 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Name12.grid(row=a + k + 2, column=0, pady=10, padx=10)

Label(second_frame, text="Score for Correctly Answered", font='arial 15 bold', bg='light pink').grid(row=a + k + 4,
                                                                                                     column=0, pady=10,
                                                                                                     padx=10)
Input_text_correctly_answered12 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_correctly_answered12.grid(row=a + k + 5, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Questioning", font='arial 15 bold', bg='light pink').grid(row=a + k + 6, column=0,
                                                                                              pady=10, padx=10)
Input_text_Questioning12 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Questioning12.grid(row=a + k + 7, column=0, pady=10, padx=10)
Label(second_frame, text="Score for Punctuality", font='arial 15 bold', bg='light pink').grid(row=a + k + 8, column=0,
                                                                                              pady=10, padx=10)
Input_text_Punctuality12 = Text(second_frame, font='arial 10', height=2, wrap=WORD, padx=3, pady=3, width=60)
Input_text_Punctuality12.grid(row=a + k + 9, column=0, pady=10, padx=10)
a += 50;k+=a;ind+=1

#fIRST BUTTON

def validate1():
    la1=[Input_text_Name1.get(1.0,END).strip(),Input_text_correctly_answered1.get(1.0,END).strip(), Input_text_Questioning1.get(1.0,END).strip(), Input_text_Punctuality1.get(1.0,END).strip()]
    la2 = [Input_text_Name2.get(1.0,END).strip(),Input_text_correctly_answered2.get(1.0, END).strip(), Input_text_Questioning2.get(1.0, END).strip(),
           Input_text_Punctuality2.get(1.0, END).strip()]
    la3 = [Input_text_Name3.get(1.0,END).strip(),Input_text_correctly_answered3.get(1.0, END).strip(), Input_text_Questioning3.get(1.0, END).strip(),
           Input_text_Punctuality3.get(1.0, END).strip()]
    la4 = [Input_text_Name4.get(1.0,END).strip(),Input_text_correctly_answered4.get(1.0, END).strip(), Input_text_Questioning4.get(1.0, END).strip(),
           Input_text_Punctuality4.get(1.0, END).strip()]
    la5 = [Input_text_Name5.get(1.0,END).strip(),Input_text_correctly_answered5.get(1.0, END).strip(), Input_text_Questioning5.get(1.0, END).strip(),
           Input_text_Punctuality5.get(1.0, END).strip()]
    la6 = [Input_text_Name6.get(1.0,END).strip(),Input_text_correctly_answered6.get(1.0, END).strip(), Input_text_Questioning6.get(1.0, END).strip(),
           Input_text_Punctuality6.get(1.0, END).strip()]
    la7 = [Input_text_Name7.get(1.0,END).strip(),Input_text_correctly_answered7.get(1.0, END).strip(), Input_text_Questioning7.get(1.0, END).strip(),
           Input_text_Punctuality7.get(1.0, END).strip()]
    la8 = [Input_text_Name8.get(1.0,END).strip(),Input_text_correctly_answered8.get(1.0, END).strip(), Input_text_Questioning8.get(1.0, END).strip(),
           Input_text_Punctuality8.get(1.0, END).strip()]
    la9 = [Input_text_Name9.get(1.0,END).strip(),Input_text_correctly_answered9.get(1.0, END).strip(), Input_text_Questioning9.get(1.0, END).strip(),
           Input_text_Punctuality9.get(1.0, END).strip()]
    la10 = [Input_text_Name10.get(1.0,END).strip(),Input_text_correctly_answered10.get(1.0, END).strip(), Input_text_Questioning10.get(1.0, END).strip(),
           Input_text_Punctuality10.get(1.0, END).strip()]
    la11 = [Input_text_Name11.get(1.0,END).strip(),Input_text_correctly_answered11.get(1.0, END).strip(), Input_text_Questioning11.get(1.0, END).strip(),
           Input_text_Punctuality11.get(1.0, END).strip()]
    la12 = [Input_text_Name12.get(1.0,END).strip(),Input_text_correctly_answered12.get(1.0, END).strip(), Input_text_Questioning12.get(1.0, END).strip(),
           Input_text_Punctuality12.get(1.0, END).strip()]
    x=[]
    Ca=sorted([[la1[0],la1[1]],[la2[0],la2[1]],[la3[0],la3[1]],[la4[0],la4[1]],[la5[0],la5[1]],[la6[0],la6[1]],[la7[0],la7[1]],[la8[0],la8[1]],[la9[0],la9[1]],[la10[0],la10[1]],[la11[0],la11[1]],[la12[0],la12[1]]],key=lambda x:int(x[1]),reverse=1)
    for k in Ca[:5]:
        x.append(k[0])


    # print(Ques[:5])
    # print(Pun[:5])

    h=[]
    for k in Ca[:5]:h.append(int(k[1]))

    co = ['red', 'green', 'blue', 'black', 'yellow']
    plt.bar(x,h,width=0.2,color=co)
    plt.xlabel("RANK")
    plt.ylabel("SCORES")
    plt.title("Top Candidates Who Answered Well")
    plt.show()

#SECOND TB
def validate2():
    la1 = [Input_text_Name1.get(1.0, END).strip(), Input_text_correctly_answered1.get(1.0, END).strip(),
           Input_text_Questioning1.get(1.0, END).strip(), Input_text_Punctuality1.get(1.0, END).strip()]
    la2 = [Input_text_Name2.get(1.0, END).strip(), Input_text_correctly_answered2.get(1.0, END).strip(),
           Input_text_Questioning2.get(1.0, END).strip(),
           Input_text_Punctuality2.get(1.0, END).strip()]
    la3 = [Input_text_Name3.get(1.0, END).strip(), Input_text_correctly_answered3.get(1.0, END).strip(),
           Input_text_Questioning3.get(1.0, END).strip(),
           Input_text_Punctuality3.get(1.0, END).strip()]
    la4 = [Input_text_Name4.get(1.0, END).strip(), Input_text_correctly_answered4.get(1.0, END).strip(),
           Input_text_Questioning4.get(1.0, END).strip(),
           Input_text_Punctuality4.get(1.0, END).strip()]
    la5 = [Input_text_Name5.get(1.0, END).strip(), Input_text_correctly_answered5.get(1.0, END).strip(),
           Input_text_Questioning5.get(1.0, END).strip(),
           Input_text_Punctuality5.get(1.0, END).strip()]
    la6 = [Input_text_Name6.get(1.0, END).strip(), Input_text_correctly_answered6.get(1.0, END).strip(),
           Input_text_Questioning6.get(1.0, END).strip(),
           Input_text_Punctuality6.get(1.0, END).strip()]
    la7 = [Input_text_Name7.get(1.0, END).strip(), Input_text_correctly_answered7.get(1.0, END).strip(),
           Input_text_Questioning7.get(1.0, END).strip(),
           Input_text_Punctuality7.get(1.0, END).strip()]
    la8 = [Input_text_Name8.get(1.0, END).strip(), Input_text_correctly_answered8.get(1.0, END).strip(),
           Input_text_Questioning8.get(1.0, END).strip(),
           Input_text_Punctuality8.get(1.0, END).strip()]
    la9 = [Input_text_Name9.get(1.0, END).strip(), Input_text_correctly_answered9.get(1.0, END).strip(),
           Input_text_Questioning9.get(1.0, END).strip(),
           Input_text_Punctuality9.get(1.0, END).strip()]
    la10 = [Input_text_Name10.get(1.0, END).strip(), Input_text_correctly_answered10.get(1.0, END).strip(),
            Input_text_Questioning10.get(1.0, END).strip(),
            Input_text_Punctuality10.get(1.0, END).strip()]
    la11 = [Input_text_Name11.get(1.0, END).strip(), Input_text_correctly_answered11.get(1.0, END).strip(),
            Input_text_Questioning11.get(1.0, END).strip(),
            Input_text_Punctuality11.get(1.0, END).strip()]
    la12 = [Input_text_Name12.get(1.0, END).strip(), Input_text_correctly_answered12.get(1.0, END).strip(),
            Input_text_Questioning12.get(1.0, END).strip(),
            Input_text_Punctuality12.get(1.0, END).strip()]
    x = []
    Ques = sorted(
        [[la1[0], la1[2]], [la2[0], la2[2]], [la3[0], la3[2]], [la4[0], la4[2]], [la5[0], la5[2]], [la6[0], la6[2]],
         [la7[0], la7[2]], [la8[0], la8[2]], [la9[0], la9[2]], [la10[0], la10[2]], [la11[0], la11[2]],
         [la12[0], la12[2]]], key=lambda x: int(x[1]), reverse=1)
    for k in Ques[:5]:
        x.append(k[0])

    # print(Ques[:5])
    # print(Pun[:5])

    h = []
    for k in Ques[:5]: h.append(int(k[1]))
    co = ['red', 'green', 'blue', 'black', 'yellow']
    plt.bar(x, h, width=0.2, color=co)
    plt.xlabel("RANKS")
    plt.ylabel("SCORE")
    plt.title("Top Candidates Who Asked Queries Most")
    plt.show()

def validate3():
    la1 = [Input_text_Name1.get(1.0, END).strip(), Input_text_correctly_answered1.get(1.0, END).strip(),
           Input_text_Questioning1.get(1.0, END).strip(), Input_text_Punctuality1.get(1.0, END).strip()]
    la2 = [Input_text_Name2.get(1.0, END).strip(), Input_text_correctly_answered2.get(1.0, END).strip(),
           Input_text_Questioning2.get(1.0, END).strip(),
           Input_text_Punctuality2.get(1.0, END).strip()]
    la3 = [Input_text_Name3.get(1.0, END).strip(), Input_text_correctly_answered3.get(1.0, END).strip(),
           Input_text_Questioning3.get(1.0, END).strip(),
           Input_text_Punctuality3.get(1.0, END).strip()]
    la4 = [Input_text_Name4.get(1.0, END).strip(), Input_text_correctly_answered4.get(1.0, END).strip(),
           Input_text_Questioning4.get(1.0, END).strip(),
           Input_text_Punctuality4.get(1.0, END).strip()]
    la5 = [Input_text_Name5.get(1.0, END).strip(), Input_text_correctly_answered5.get(1.0, END).strip(),
           Input_text_Questioning5.get(1.0, END).strip(),
           Input_text_Punctuality5.get(1.0, END).strip()]
    la6 = [Input_text_Name6.get(1.0, END).strip(), Input_text_correctly_answered6.get(1.0, END).strip(),
           Input_text_Questioning6.get(1.0, END).strip(),
           Input_text_Punctuality6.get(1.0, END).strip()]
    la7 = [Input_text_Name7.get(1.0, END).strip(), Input_text_correctly_answered7.get(1.0, END).strip(),
           Input_text_Questioning7.get(1.0, END).strip(),
           Input_text_Punctuality7.get(1.0, END).strip()]
    la8 = [Input_text_Name8.get(1.0, END).strip(), Input_text_correctly_answered8.get(1.0, END).strip(),
           Input_text_Questioning8.get(1.0, END).strip(),
           Input_text_Punctuality8.get(1.0, END).strip()]
    la9 = [Input_text_Name9.get(1.0, END).strip(), Input_text_correctly_answered9.get(1.0, END).strip(),
           Input_text_Questioning9.get(1.0, END).strip(),
           Input_text_Punctuality9.get(1.0, END).strip()]
    la10 = [Input_text_Name10.get(1.0, END).strip(), Input_text_correctly_answered10.get(1.0, END).strip(),
            Input_text_Questioning10.get(1.0, END).strip(),
            Input_text_Punctuality10.get(1.0, END).strip()]
    la11 = [Input_text_Name11.get(1.0, END).strip(), Input_text_correctly_answered11.get(1.0, END).strip(),
            Input_text_Questioning11.get(1.0, END).strip(),
            Input_text_Punctuality11.get(1.0, END).strip()]
    la12 = [Input_text_Name12.get(1.0, END).strip(), Input_text_correctly_answered12.get(1.0, END).strip(),
            Input_text_Questioning12.get(1.0, END).strip(),
            Input_text_Punctuality12.get(1.0, END).strip()]
    x = []
    Pun = sorted(
        [[la1[0], la1[3]], [la2[0], la2[3]], [la3[0], la3[3]], [la4[0], la4[3]], [la5[0], la5[3]], [la6[0], la6[3]],
         [la7[0], la7[3]], [la8[0], la8[3]], [la9[0], la9[3]], [la10[0], la10[3]], [la11[0], la11[3]],
         [la12[0], la12[3]]], key=lambda x: x[1], reverse=1)
    for k in Pun[:5]:
        x.append(k[0])

    # print(Ques[:5])
    # print(Pun[:5])

    h = []
    for k in Pun[:5]: h.append(int(k[1]))

    co=['red','green','blue','black','yellow']

    plt.bar(x, h, width=0.2,color=co)
    plt.xlabel("RANK")
    plt.ylabel("SCORE")
    plt.title("Top Candidates Who Are Punctual")
    plt.show()






trans_btn = Button(root, text = 'SHOW GRAPH FOR TOP 5 CORRECTLY ANSWERED CANDIDATES\n ==>',command=validate1,font = 'arial 12 bold',pady = 5 ,state="active",bg = 'light blue',relief="ridge", activeforeground = 'purple',activebackground = 'sky blue')
trans_btn.place(x = 500, y = 300)
trans_btn = Button(root, text = 'SHOW GRAPH FOR TOP 5 QUESTIONS ASKED BY CANDIDATES\n ==>',command=validate2,font = 'arial 12 bold',pady = 5 ,state="active",bg = 'light blue',relief="ridge", activeforeground = 'purple',activebackground = 'sky blue')
trans_btn.place(x = 500, y = 400)
trans_btn = Button(root, text = 'SHOW GRAPH FOR TOP 5 PUNCTUAL CANDIDATE\n ==>',command=validate3,font = 'arial 12 bold',pady = 5 ,state="active",bg = 'light blue',relief="ridge", activeforeground = 'purple',activebackground = 'sky blue')
trans_btn.place(x = 500, y = 500)




scrollbar.config( command = My_canvas.yview )
root.mainloop()