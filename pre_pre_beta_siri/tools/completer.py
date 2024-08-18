"""
Скрипт для автодоповнення команд в консолі.
"""
from prompt_toolkit.completion import Completer, Completion

class CommandCompleter(Completer):

    def __init__(self, commands):
        super().__init__()
        self.commands = commands

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor
       
        if ' ' in text_before_cursor:
            return
        
        for cmd in self.commands:
            if cmd.startswith(text_before_cursor):
                yield Completion(cmd, start_position=-len(text_before_cursor))