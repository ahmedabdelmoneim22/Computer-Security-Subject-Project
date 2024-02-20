#BY-Ahmed Abdel Moneim Abdel Halim.
from art import logo,logo1,logo2,logo3
#print(logo)
#Enter_technique = str(input("Enter technique (Ceaser/PolyAlphabetic/Transposition):").lower())
#if Enter_technique == 'ceaser':
def Ceaser_Cipher_Technique():
    print("Ceaser Cipher technique.")
    print(logo1)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"Here's the {cipher_direction}d result: {end_text}")
        CipherLabel.configure(text=f"The Cipher Text:-\n {end_text.upper()}")
        CipherLabel.place(x=30, y=240)
    #should_end = False
    #while not should_end:
        #direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        #text = input("Type your message:\n").lower()
        #shift = int(input("Type the shift number:\n"))
    direction = str(combo2.get())
    text = str(MessageEntry.get()).lower()
    shift = int(KeyEntry.get())
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        #restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        #if restart == "no":
        #    should_end = True
        #    print("Goodbye")
#elif Enter_technique == 'polyalphabetic':
def PolyAlphabetic_Cipher_Technique():
    print("PolyAlphabetic Cipher technique.")
    print(logo2)
    # index from 0 to 25.
    Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #message_Text = str(input("Enter Message Text:"))
    #message_Key = str(input("Enter Key:"))
    message_Text =  str(MessageEntry.get())
    message_Key = str(KeyEntry.get())
    cipher_Text = ""
    # Convert Message to List.
    Message_Text_List = list(message_Text.strip(" "))
    Message_Key_List = list(message_Key.strip(" "))
    # print(Message_Text_List)
    # print(Message_Key_List)
    # $$$$$$$$$$$$$$$$$$$$$$$$##
    for num1 in range(0, len(Message_Text_List)):
        if num1 >= len(Message_Key_List):
            Message_Key_List += Message_Key_List
        letter_Text_index = Alphabet.index(Message_Text_List[num1].lower())
        letter_Key_index = Alphabet.index(Message_Key_List[num1].lower())
        cipher_index = (int(letter_Text_index) + int(letter_Key_index)) % 26
        cipher_Text += Alphabet[cipher_index]
    print("The Cipher Text:", cipher_Text)
    CipherLabel.configure(text=f"The Cipher Text:-\n {cipher_Text.upper()}")
    CipherLabel.place(x=30, y=210)
    # meetmeaftertheparty.
    # Decisive.
#elif Enter_technique == 'transposition':
def Transposition_Cipher_technique():
    print("Transposition Cipher technique.")
    print(logo3)
    #Message:"depositatenmillionpoundinibrahiemaccountyz"#42.
    #Key:"2641753"#7.
    #message_Text = str(input("Enter Message Text:"))
    #message_Key = str(input("Enter Key:"))
    message_Text = str(MessageEntry.get())
    message_Key = str(KeyEntry.get())
    cipher_Text = ""
    if len(message_Text) == 42 and len(message_Key) == 7:
        Message_Text_List = list(message_Text.strip(" "))
        Message_Key_List = list(message_Key.strip(" "))
        Column = []
        Number = 0
        len_Message = len(Message_Key_List)
        for num in range(0, len(Message_Key_List)):
            Column.append(Message_Text_List[0 + Number])
            Column.append(Message_Text_List[len_Message + Number])
            Column.append(Message_Text_List[len_Message + len_Message + Number])
            Column.append(Message_Text_List[len_Message + len_Message + len_Message + Number])
            Column.append(Message_Text_List[len_Message + len_Message + len_Message + len_Message + Number])
            Column.append(
                Message_Text_List[len_Message + len_Message + len_Message + len_Message + len_Message + Number])
            Number += 1
        print(len(Message_Text_List))
        Value = {
            f"{Message_Key_List[0]}": Column[0:6],
            f"{Message_Key_List[1]}": Column[6:12],
            f"{Message_Key_List[2]}": Column[12:18],
            f"{Message_Key_List[3]}": Column[18:24],
            f"{Message_Key_List[4]}": Column[24:30],
            f"{Message_Key_List[5]}": Column[30:36],
            f"{Message_Key_List[6]}": Column[36:42]}
        sorted_value = sorted(Value)
        cipher_Text = Value[sorted_value[0]] + Value[sorted_value[1]] + Value[sorted_value[2]] + Value[sorted_value[3]] \
                      + Value[sorted_value[4]] + Value[sorted_value[5]] + Value[sorted_value[6]]
        cipher_Text = "".join(cipher_Text)
        print(cipher_Text)
        CipherLabel.configure(text=f"The Cipher Text:-\n {cipher_Text.upper()}")
        CipherLabel.place(x=30,y=210)
    else:
        print("Please Enter 42 Message Letter and 7 Key Number.")
#else:print("Wrong Input Try Agen.")
################################################################
##########$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#########################
#text top and cipher button.
################################################################
def Cipher_Technique():
    comboButton.configure(state="disabled")
    if combo.get() == "Ceaser Cipher":
        MessageLabel.pack(side="left", anchor="n")  # anchor Option,("n", "s", "e", "w", "nw", etc).
        MessageEntry.place(x=130, y=155, width=290)
        KeyLabel.place(x=-35, y=175)
        KeyEntry.place(x=130, y=178, width=100, height=25)
        combo2.place(x=270, y=178,width=150,height=28)
        # Set the Default value of the Combobox.
        combo2.current(0)
        theResult.configure(command=Ceaser_Cipher_Technique)
        theResult.place(x=270, y=210, width=150)
    elif combo.get() == "PolyAlphabetic Cipher":
        MessageLabel.pack(side="left", anchor="n")  # anchor Option,("n", "s", "e", "w", "nw", etc).
        MessageEntry.place(x=130, y=155, width=290)
        KeyLabel.place(x=-35, y=175)
        KeyEntry.place(x=130, y=178, width=100, height=25)
        theResult.configure(command=PolyAlphabetic_Cipher_Technique)
        theResult.place(x=270, y=178, width=150)
    elif combo.get() == "Transposition Cipher":
        MessageLabel.pack(side="left",anchor= "n")# anchor Option,("n", "s", "e", "w", "nw", etc).
        MessageEntry.place(x=130,y=155,width=290)
        KeyLabel.place(x=-35,y=175)
        KeyEntry.place(x=130, y=178, width=100,height=25)
        theResult.configure(command=Transposition_Cipher_technique)
        theResult.place(x=270,y=178,width=150)
        #Transposition_Cipher_technique().
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Computer Security Project.")
window.geometry("500x400")
window.configure(background="Black")
LabelTitle = tk.Label(window,text="Computer Security App",
                      font=("Arial", 25),fg="red",background="Black",width=26)#,padx=100,pady=100.
LabelTitle.pack()
LabelSpace = tk.Label(window,text="",background="Black")
LabelSpace.pack()
# Create a Combobox with some options.
combo = ttk.Combobox(window,
                     values=["Ceaser Cipher", "PolyAlphabetic Cipher", "Transposition Cipher"],
                     width=30, font=("Arial", 13),foreground="Red",height=30)
combo.pack()
# Set the Default value of the Combobox.
combo.current(0)
print(combo.get())
LabelBSpace = tk.Label(window,text="",background="Black")
LabelBSpace.pack()
comboButton = tk.Button(window, text="Enter",width=8,activebackground="Black",
                        height=1,fg="red",font=("Arial", 15), command=Cipher_Technique)
comboButton.pack()
#MessageAndKeyLabel#
MessageLabel = tk.Label(window,text="Message Text:-",font=("Arial",13),fg="red",background="Black",width=13)
KeyLabel = tk.Label(window, text="Key:-", font=("Arial", 13), fg="red", background="Black",width=13)
CipherLabel = tk.Label(window,text ="",font=("Arial",13),fg="Blue",background="Black")
#MessageAndKeyButton#
theResult = tk.Button(window,text="Result",font=("Arial", 10),
                              fg="red",activebackground="black")
#MessageAndKeyEntry#
MessageEntry = tk.Entry(window)
KeyEntry = tk.Entry(window)
#MessageAndKeyConbobox#
combo2 = ttk.Combobox(window,
                     values=["encode", "decode"],
                     width=15, font=("Arial", 10),foreground="Red")

#####Exit#######
import sys
def EndGame():#End & Stop The Program.
    sys.exit("End")
ExitButton = tk.Button(window, text="Exit",width=8,activebackground="Black",
                        height=1,fg="red",font=("Arial", 15), command=EndGame)
ExitButton.place(x=200,y=355)
#####MainLoop###
window.resizable(False,False)#Window-Fixed.
window.mainloop()
"""
Technique-Cipher-Used:-
1)Caesar-cipher;
2)PolyAlphabetic-Cipher;
3)Transposition-cipher;
"""


