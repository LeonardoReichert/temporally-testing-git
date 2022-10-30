
from tkinter import *;

root = Tk();
root.geometry("200x150");
root.title("Testing Git");

Label(root, text="This is a test of git! :D").pack();
Label(root, text="other test of git! :D").pack();

Button(root, text="exit", command=root.destroy).pack(side="bottom");

root.mainloop();

