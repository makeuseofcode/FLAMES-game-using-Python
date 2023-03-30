from tkinter import *

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]

def tell_status():
    p1 = Person1_field.get()
    p1 = p1.lower()
    p1.replace(" ", "")
    p1_list = list(p1)
    p2 = Person2_field.get()
    p2 = p2.lower()
    p2.replace(" ", "")
    p2_list = list(p2)
    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index + 1:]
    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[: split_index]
            result = right + left
        else:
            result = result[: len(result) - 1]
    Status_field.insert(0, result[0])

def clear_all():
    Person1_field.delete(0, END)
    Person2_field.delete(0, END)
    Status_field.delete(0, END)
    Person1_field.focus_set()

root = Tk()
root.configure(background='#A020F0')
root.geometry("700x200")
root.title("FLAMES Game")

label1 = Label(root, text="Name 1: ", fg='#ffffff',bg='#A020F0', font=("arial",20,"bold"), padx='20')
label2 = Label(root, text="Name 2: ", fg='#ffffff',bg='#A020F0', font=("arial",20,"bold"), padx='20')
label3 = Label(root, text="Relationship Status: ", fg='#ffffff', bg='#A020F0',font=("arial",20,"bold"), padx='20')

label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=4, column=0)

Person1_field = Entry(root, font=("arial", 15, "bold"))
Person2_field = Entry(root, font=("arial", 15, "bold"))
Status_field = Entry(root, font=("arial",15,"bold"))

Person1_field.grid(row=1, column=1, ipadx="50")
Person2_field.grid(row=2, column=1, ipadx="50")
Status_field.grid(row=4, column=1, ipadx="50")

button1 = Button(root, text="Submit", bg="#00ff00", fg="black", command=tell_status,font=("arial",13,"bold") )
button2 = Button(root, text="Clear", bg="#00ff00", fg="black", command=clear_all, font=("arial",13,"bold"))
button1.grid(row=3, column=1)
button2.grid(row=5, column=1)

root.mainloop()
