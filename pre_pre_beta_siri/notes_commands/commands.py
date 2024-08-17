from notes_commands.main_command import make_command

COMMANDS = {
    "notes": make_command(),
    "notes-test-data": make_command("test-data"),
    "notes-help": make_command("help"),
    "notes-list": make_command("list"),
    "notes-find": make_command("find"),
    "notes-add": make_command("add"),
    "notes-delete": make_command("delete"),
    "notes-update": make_command("update"),
}
