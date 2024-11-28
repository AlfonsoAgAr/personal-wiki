from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save_message(self, user, message):
        pass

    @abstractmethod
    def load_messages(self):
        pass
