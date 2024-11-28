from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def generate_response(self, prompt):
        pass
