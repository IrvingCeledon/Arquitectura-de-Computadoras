from tkinter import filedialog, messagebox
import os

class IOUtils:
    DEFAULT_FILENAME = "instructions.txt"
    
    def __init__(self, language_dictionary):
        self.tr = language_dictionary

    # ----- Public methods ----- #
    def load_from_file(self):
        file_path = self._get_file_path()
        
        if not file_path: 
            return None

        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            messagebox.showerror(
                self.tr["generic_error_title"], 
                f"{self.tr['error_while_opening_file_message']} {file_path}"
            )
        except Exception as e:
            messagebox.showerror(
                self.tr["generic_error_title"], 
                f"{self.tr['generic_error_message']} {e}"
            )

        return None    

    def save_as_txt(self, binary : str):
        if not binary:
            raise ValueError(self.tr["nothing_to_export_error"])
        
        folder_path = filedialog.askdirectory(title=self.tr["select_path"])
        
        if not folder_path:
            return

        file_path = os.path.join(folder_path, self.DEFAULT_FILENAME)
        
        with open(file_path, "w") as f:
            f.write(binary)
  
        messagebox.showinfo(
            self.tr["export_success_title"], 
            f"{self.tr['export_success_message']} {file_path}"
        )

    def apply_language(self, new_tr):
        self.tr = new_tr

    # ----- Internal methods ----- #
    def _get_file_path(self):
        return filedialog.askopenfilename(
            title=self.tr["select_file_title"],
            filetypes=(
                (self.tr["txt_option"], "*.txt"), 
                (self.tr["bin_option"], "*.bin"), 
                (self.tr["all_option"], "*.*")
            )
        )