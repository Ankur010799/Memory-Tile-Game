import tkinter as tk


class Tile:

    def __init__(self, frame, content, action, row, column):
        self.content = content
        self.button = tk.Button(frame, text=' ', bg="#ffffff", activebackground="#cccccc",
                                height=3, width=4, command=action)
        self.button.grid(row=row, column=column)
        self.is_matched = False

    def is_content_same(self, other):
        return self.content == other.content

    def matched(self):
        self.is_matched = True
        self.button.config(state=tk.DISABLED)
        self.show()

    def hide(self):
        if not self.is_matched:
            self.button.after(1000, lambda: self.button.config(bg="#ffffff", activebackground="#cccccc"))

    def show(self):
        self.button.config(bg=self.content, activebackground=self.content)
