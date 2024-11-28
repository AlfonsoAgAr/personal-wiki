class ChatAssistant:
    def __init__(self, model, storage):
        self.model = model
        self.storage = storage

    def get_response(self, user_input):

        self.storage.save_message(user="Tú", message=user_input)

        response = self.model.generate_response(user_input)

        self.storage.save_message(user="Asistente", message=response)

        return response
