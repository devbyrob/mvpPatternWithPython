from tkinter import*


class CRUDVIEW:
    
    def __init__(self, controller):
        self.controller = controller
        self.__root = Tk()

        self.__menu_bar = Menu(self.__root)
        self.__root.config(menu=self.__menu_bar)

        self.__option_menu = Menu(self.__menu_bar, tearoff=0)
        self.__option_menu.add_command(label="Clear Data", command=self.clear_screen)

        self.__menu_bar.add_cascade(label="Options", menu=self.__option_menu)

        self.__frame_inf = Frame(self.__root)
        self.__frame_inf.pack()
        self.__frame_buttons = Frame(self.__root)
        self.__frame_buttons.pack()

        self.__code = StringVar()
        self.__name = StringVar()
        self.__price = StringVar()

        self.__code_entry = Entry(self.__frame_inf, textvariable=self.__code)
        self.__code_entry.grid(row=0, column=1, padx=10, pady=10)

        self.__name_entry = Entry(self.__frame_inf, textvariable=self.__name)
        self.__name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.__price_entry = Entry(self.__frame_inf, textvariable=self.__price)
        self.__price_entry.grid(row=2, column=1, padx=10, pady=10)

        self.__code_label = Label(self.__frame_inf, text="Code: ")
        self.__code_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.__name_label = Label(self.__frame_inf, text="Name: ")
        self.__name_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.__price_label = Label(self.__frame_inf, text="Price: ")
        self.__price_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        self.__reg_button = Button(self.__frame_buttons, text="Reg", command=self.reg_data)
        self.__reg_button.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.__search_button = Button(self.__frame_buttons, text="Search", command=self.search_data)
        self.__search_button.grid(row=0, column=1, sticky="e", padx=10, pady=10)

        self.__update_button = Button(self.__frame_buttons, text="Update", command=self.update_data)
        self.__update_button.grid(row=0, column=2, sticky="e", padx=10, pady=10)

        self.__delete_button = Button(self.__frame_buttons, text="Delete", command=self.delete_data)
        self.__delete_button.grid(row=0, column=3, sticky="e", padx=10, pady=10)

        self.__root.mainloop()

    def reg_data(self):
        self.controller.create_registry(self.__name.get(), self.__price.get())
        self.clear_screen()

    def search_data(self):
        code = self.__code.get()
        product = self.controller.find_registry(code)
        for p in product:
            self.__show_data(p[0], p[1], p[2])

    def __show_data(self, code, name, price):
        self.__code.set(code)
        self.__name.set(name)
        self.__price.set(price)

    def update_data(self):
        self.controller.update_registry(self.__code.get(), self.__name.get(), self.__price.get())

    def clear_screen(self):
        self.__code.set("")
        self.__name.set("")
        self.__price.set("")

    def delete_data(self):
        self.controller.delete_registry(self.__code.get())
        self.clear_screen()

    def __show_data(self, code, name, price):
        self.__code.set(code)
        self.__name.set(name)
        self.__price.set(price)
