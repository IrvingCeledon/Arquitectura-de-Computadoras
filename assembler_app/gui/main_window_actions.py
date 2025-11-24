class MainWindowActions:
    def __init__(self, root, ui, settings, assembler_controller, io_controller, change_language):
        self.root = root
        self.ui = ui
        self.settings = settings
        self.assembler = assembler_controller
        self.io = io_controller
        self.change_language = change_language

    def bind_controllers(self):
        self.assembler.set_text_containers(self.ui.text_input, self.ui.text_output)
        self.io.set_text_containers(self.ui.text_input, self.ui.text_output)