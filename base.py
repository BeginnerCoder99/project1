# base.py

class BaseComponent:
    def run(self):
        raise NotImplementedError("Subclasses must implement the run() method")
