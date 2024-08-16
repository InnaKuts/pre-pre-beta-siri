from notes import Notebook, Note


def add_test_data(cmd: str, notebook: Notebook):
    if cmd != "test-data":
        return False
    for note in generate_test_data():
        notebook.add_note(note)
    print("Test data added")
    return True


def generate_test_data():
    return [
        Note(
            title="Buy Milk",
            description="Remember to buy 2 liters of whole milk.",
            tags=["dairy", "essentials"]
        ),
        Note(
            title="Pick Up Eggs",
            description="Need a dozen eggs for the weekend breakfast.",
            tags=["dairy", "breakfast"]
        ),
        Note(
            title="Fruits and Vegetables",
            description="Get apples, bananas, and some fresh spinach.",
            tags=["health", "essentials"]
        ),
        Note(
            title="Weekly Grocery Shopping",
            description="Buy items for weekly meals: bread, pasta, chicken, and rice.",
            tags=["essentials", "weekly"]
        ),
        Note(
            title="Stock up on Snacks",
            description="Get some chips, nuts, and granola bars for the pantry.",
            tags=["snacks", "pantry"]
        )
    ]
