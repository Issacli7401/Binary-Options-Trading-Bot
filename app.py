from belfort.core.items.item_manager import ItemManager


class App(object):

    def __init__(self):
        """
        Initialises a new instance of the App class.
        """
        self.__item_manager = ItemManager()

    def load(self):
        """
        Loads all components within the App class.
        """
        if self.__item_manager is None:
            raise TypeError("The ItemManager must be initialised before load.")
        else:
            self.__item_manager.load()

