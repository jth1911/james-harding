# custom_new_example.py
class SomeClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # Customize your instance here...
        return instance

