"""
    Modellek kipróbálásért felelő oldal
"""

from tkinter import StringVar, Text, END
from tkinter.ttk import Style, Label, Combobox, Button
from domain_specific_tokenizers.window_creator import WindowCreator
from domain_specific_tokenizers import model_handler
from domain_specific_tokenizers import read_config


def model_test():
    """
        Modellek kipróbálására szolgáló oldal
    """

    options = read_config.read_config()["TokenizerOptions"]
    model_test_window = WindowCreator(1000, 500, 2, 25,
                                      "Modellek kipróbálása").win

    model_test_style = Style(model_test_window)
    model_test_style.configure('ModelTest.TButton', font=('Arial', 16, 'bold'))

    tokenizer_label = Label(model_test_window, font=('Arial', 20),
                            text="Válassz a tokenizálók közül")
    tokenizer_label.grid(columnspan=1, column=0, row=0, padx=(100, 10))

    selected_tokenizer = StringVar()
    selected_tokenizer.set(options[0])
    tokenizer_dropdown = Combobox(model_test_window,
                                  textvariable=selected_tokenizer,
                                  values=options)
    tokenizer_dropdown.config(width=35)
    tokenizer_dropdown.grid(columnspan=1, column=0, row=1, padx=(100, 10))

    models_label = Label(model_test_window, font=('Arial', 20),
                         text="Válassz a modellek közül")
    models_label.grid(columnspan=1, column=1, row=0, padx=(10, 100))

    selected_model = StringVar()
    selected_model.set(options[0])
    model_dropdown = Combobox(model_test_window,
                              textvariable=selected_model,
                              values=options)
    model_dropdown.config(width=35)
    model_dropdown.grid(columnspan=1, column=1, row=1, padx=(10, 100))

    model_input = Text(model_test_window, height=20, width=70,
                       padx=10, pady=10)
    model_input.grid(columnspan=2, rowspan=15, row=2)

    run_button = Button(model_test_window, text="Osztályozás",
                        style="ModelTest.TButton",
                        command=lambda: start_inference(
                            selected_tokenizer.get(),
                            selected_model.get(),
                            model_input))
    run_button.grid(columnspan=2, column=0, row=18)


def start_inference(tokenizer: str, model: str, model_input: Text):
    """
        Modellek futtatását elindító függvény
    """

    input_text = model_input.get('1.0', 'end-1c')
    normalized = normalize_names(tokenizer, model)
    trained_model = model_handler.TrainedModel(normalized[0], normalized[1])
    tokenized_input = trained_model.tokenize_input(input_text)
    model_input.insert(END, f"\nÉrtékelés: \n -> {trained_model.rate_input(tokenized_input)}")


def normalize_names(tokenizer: str, model: str):
    """
        Átalakítja a modellek és tokenizálók nevét olyan formára ami
        egyezik a HuggingFace-re feltöltött modellek elérési útjával
    """
    normalized_tokenizer = tokenizer.strip().lower().replace('&', 'and').\
        replace(' ', '_')
    normalized_model = model.strip().lower().replace('&', 'and').\
        replace(' ', '_')
    return (normalized_tokenizer, normalized_model)
