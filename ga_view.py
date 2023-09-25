import json
import tkinter as tk
from tkinter import ttk, filedialog

from settings import Settings

CAPTION = "Generic Algorithm"
WINDOW_SIZE = 1000, 600

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self._settings = Settings()
        self.title(CAPTION)
        size = WINDOW_SIZE
        self.geometry(f'{size[0]}x{size[1]}')

        self._control_panel = ControlPanel(master=self)
        self._control_panel.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=True)


class ControlPanel(ttk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self._fun_callback = None
        self._btn_select_file = ttk.Button(self, text="Открыть файл", command=self._open_file)
        self._btn_select_file.pack(expand=True, fill="both")

    def _open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                json_map = json.load(file)
                if self._fun_callback:
                    self._fun_callback(json_map)

    def set_callback(self, fun_callback):
        self._fun_callback = fun_callback


view = MainView()
view.mainloop()
