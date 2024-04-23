from tkinter import Tk, Toplevel, Canvas


class WindowCreator:
    def __init__(self, window_width: int = 500,
                 window_height: int = 500,
                 columnspan: int = 1,
                 rowspan: int = 1,
                 title: str = "Ablak",
                 main_window: bool = False) -> None:

        self.window_width = window_width
        self.window_height = window_height
        self.columspan = columnspan
        self.rowspan = rowspan
        self.title = title
        self.main_window = main_window
        self.win = self.create_window()

    def create_window(self):
        if self.main_window:
            win = Tk()
        else:
            win = Toplevel()
        win.title(self.title)
        canvas = Canvas(win, width=self.window_width,
                        height=self.window_height)
        canvas.grid(columnspan=self.columspan, rowspan=self.rowspan)
        return win
