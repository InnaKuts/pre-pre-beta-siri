from rich.console import Console
from rich.table import Table
from model.record import Record
from notes import Note


def pretty_records(records: [Record]):
    table = Table(title="Records")
    fields = [
        ('Name', lambda r: r.name.value),
        ('Phones', lambda r: "\n".join([p.value for p in r.phones])),
        ('Birthday', lambda r: r.birthday.value.strftime('%d.%m.%Y') if r.birthday else "N/A"),
        ('Email', lambda r: r.email if r.email else "N/A"),
        ('Address', lambda r: r.address.value if r.address else "N/A"),
    ]
    for field in fields:
        table.add_column(field[0])
    for record in records:
        values = [f[1](record) for f in fields]
        table.add_row(*values, style='bright_green')
    console = Console()
    console.print(table)


def pretty_notes(notes: [Note]):
    table = Table(title="Notes")
    fields = [
        ('Title', lambda n: n.title.value),
        ('Description', lambda n: n.description.value),
        ('Tags', lambda n: "; ".join([p for p in n.tags])),
        ('Contact', lambda n: n.contact.value if n.contact else "N/A"),
    ]
    table.add_column("#")
    for field in fields:
        table.add_column(field[0])
    for (index, note) in enumerate(notes):
        values = [f[1](note) for f in fields]
        table.add_row(str(index + 1), *values, style='bright_green')
    console = Console()
    console.print(table)
