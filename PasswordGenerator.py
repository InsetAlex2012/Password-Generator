#https://github.com/TkinterEP/ttkthemes/tree/master/screenshots

from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
import random

import datetime

x = datetime.datetime.now()

day = x.day
month = x.month

encryption_key = (int(day) + int(month)) * 2



lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

generator_copy_animation_after_id = None

encryptor_copy_animation_after_id = None

root = ThemedTk(theme="breeze")

screen_width_middle = int(root.winfo_screenwidth() / 2 - 600 / 2)
screen_height_middle = int(root.winfo_screenheight() / 2 - 540 / 2)

root.geometry(f"600x540+{screen_width_middle}+{screen_height_middle}")
root.title("Password Generator! - Python Project")
root.configure(themebg="breeze")
root.resizable(False, False)

dice_img = PhotoImage(file="dice.png")
root.iconphoto(True, dice_img)

password = ""
string_password = StringVar()

encrypted_password = ""
encrypted_string_password = StringVar()

def generate():
    global password

    length = password_length_combobox.get()
    strength = password_strength.get()

    password = ""

    for i in range(int(length)):
        if strength == 1:
            random_character = random.choice(lower)
        elif strength == 2:
            random_character = random.choice(upper)
        elif strength == 3:
            random_character = random.choice(digits)
        else:
            return
        password += random_character
    string_password.set(password)

def generator_copy():
    global password, generator_copy_animation_after_id

    generator_copy_cancel_animation()

    generator_copy_button.configure(text="Copied!")
    root.clipboard_clear()
    root.clipboard_append(password)

    generator_copy_animation_after_id = generator_copy_button.after(1000, generator_copy_end_animation)

def generator_copy_cancel_animation():
    global generator_copy_animation_after_id
    if generator_copy_animation_after_id is not None:
        generator_copy_button.after_cancel(generator_copy_animation_after_id)
        generator_copy_animation_after_id = None

def generator_copy_end_animation():
    global generator_copy_animation_after_id
    generator_copy_button.configure(text="Copy")
    generator_copy_animation_after_id = None



def encrypt():
    global encrypted_password

    non_encrypted_password = encryptor_entry.get()

    encrypted_password = ""

    for character in non_encrypted_password:
        character_position = digits.index(character)

        encrypted_password += str(digits[(character_position + encryption_key) % 72])
    encrypted_string_password.set(encrypted_password)

def encryptor_copy():
    global encrypted_password, encryptor_copy_animation_after_id

    encryptor_copy_cancel_animation()

    encryptor_copy_button.configure(text="Copied!")
    root.clipboard_clear()
    root.clipboard_append(encrypted_password)

    encryptor_copy_animation_after_id = encryptor_copy_button.after(1000, encryptor_copy_end_animation)

def encryptor_copy_cancel_animation():
    global encryptor_copy_animation_after_id
    if encryptor_copy_animation_after_id is not None:
        encryptor_copy_button.after_cancel(encryptor_copy_animation_after_id)
        encryptor_copy_animation_after_id = None

def encryptor_copy_end_animation():
    global encryptor_copy_animation_after_id
    encryptor_copy_button.configure(text="Copy")
    encryptor_copy_animation_after_id = None

password_strength = IntVar()
password_strength.set(2)

title_label = Label(root, text="Password Generator!", background="light blue", font=("Rubik Mono One", 26), justify="center")
title_label.pack(pady=20)

generator_frame = Frame(root)
generator_frame.pack(pady=10)

generator_label = Label(generator_frame, text="  Password Creation  ", background="#00A7D1", font=("Rubik Mono One", 15), justify="center")
generator_label.pack(pady=5)

password_length_combobox = Combobox(generator_frame, cursor="hand2", font=("Rubik Mono One", 12), width=10, state="readonly")
password_length_combobox["values"] = (4, 6, 8, 10, 12)
password_length_combobox.current(2)
password_length_combobox.pack(pady=5)

radio_style = Style()
radio_style.configure("TRadiobutton", font=("Rubik Mono One", 10))

generator_radio_frame = Frame(generator_frame)
generator_radio_frame.pack(pady=5)

generator_strength_radio_1 = Radiobutton(generator_radio_frame, text="Weak", value=1, variable=password_strength, style="TRadiobutton", cursor="hand2")
generator_strength_radio_1.pack(side=LEFT, padx=5)

generator_strength_radio_2 = Radiobutton(generator_radio_frame, text="Intermediate", value=2, variable=password_strength, style="TRadiobutton", cursor="hand2")
generator_strength_radio_2.pack(side=LEFT, padx=5)

generator_strength_radio_3 = Radiobutton(generator_radio_frame, text="Strong", value=3, variable=password_strength, style="TRadiobutton", cursor="hand2")
generator_strength_radio_3.pack(side=LEFT, padx=5)

generator_output_entry = Entry(generator_frame, textvariable=string_password, font=("Arial", 15), width=25, state="readonly")
generator_output_entry.pack(pady=5)

style = Style()
style.configure("TButton", font=("Rubik Mono One", 15))

generator_button_frame = Frame(generator_frame)
generator_button_frame.pack(pady=5)

generator_generate_button = Button(generator_button_frame, text="Generate", style="TButton", command=generate)
generator_generate_button.pack(side=LEFT, padx=5)

generator_copy_button = Button(generator_button_frame, text="Copy", style="TButton", command=generator_copy)
generator_copy_button.pack(side=LEFT, padx=5)

encryptor_frame = Frame(root)
encryptor_frame.pack(pady=20)

encryptor_label = Label(encryptor_frame, text="  Password Encryption  ", background="#0083A3", font=("Rubik Mono One", 15), justify="center")
encryptor_label.pack(pady=5)

encryptor_entry = Entry(encryptor_frame, font=("Arial", 15), width=25, textvariable=encrypted_string_password)
encryptor_entry.pack(pady=5)

encryptor_button_frame = Frame(encryptor_frame)
encryptor_button_frame.pack(pady=5)

encryptor_encrypt_button = Button(encryptor_button_frame, text="Encrypt", style="TButton", command = encrypt)
encryptor_encrypt_button.pack(side=LEFT, padx=5)

encryptor_copy_button = Button(encryptor_button_frame, text="Copy", style="TButton", command = encryptor_copy)
encryptor_copy_button.pack(side=LEFT, padx=5)

signature_label = Label(root, text="By AlexIsNotInset", font=("Rubik Mono One", 15))
signature_label.pack(pady=10)

root.mainloop()