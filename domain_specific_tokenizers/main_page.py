"""
    A program belépési pontja és a fő ablak létrehozásáért felel
"""
from tkinter.ttk import Label, Button, Style
from domain_specific_tokenizers.window_creator import WindowCreator
from domain_specific_tokenizers import tokenizers_page
from domain_specific_tokenizers import model_test_page
from domain_specific_tokenizers import models_page
from domain_specific_tokenizers import domains_page


def main():
    """
       A program belépési pontja
    """

    win = WindowCreator(1000, 750, 3, 5, "Főablak", True).win

    lbl = Label(win, font=('Arial', 30, 'bold'), wraplength=1000,
                justify='center',
                text="Neurális nyelvmodellek doménadaptációja \
                    feladatspecifikus szótár kialakításával \n\n Demo app")
    lbl.grid(columnspan=3, column=0, row=0)

    button_style = Style()
    button_style.configure('TButton', font=('Arial', 25, 'bold'))

    test_model_button = Button(win, text="Modell kipróbálása",
                               command=lambda: model_test_page.model_test())
    test_model_button.grid(columnspan=3, column=0, row=1)

    tokenizer_info_button = Button(win, text="Tokenizálók",
                                   command=lambda:
                                   tokenizers_page.tokenizer_info())
    tokenizer_info_button.grid(columnspan=1, column=0, row=2)

    model_info_button = Button(win, text="Modellek",
                               command=lambda: models_page.model_info())
    model_info_button.grid(columnspan=1, column=1, row=2)

    datasets_info_button = Button(win, text="Adathalmazok",
                                  command=lambda: domains_page.datasets_info())
    datasets_info_button.grid(columnspan=1, column=2, row=2)
    win.mainloop()


if __name__ == '__main__':
    main()
