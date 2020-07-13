from .item import Item


class ItemManager(object):

    def __init__(self):
        """
        Initialises a new instance of the ItemManager class.
        """
        self._items = []

    def load(self):
        """
        Loads all components within the ItemManager class.
        """
        if len(self._items) > 0:
            self._items.clear()

        # ...
