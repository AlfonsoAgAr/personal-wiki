from chat.assistant import ChatAssistant
from chat.openai_model import OpenAIModel
from storage.json_storage import JSONStorage

def main():
    print("Bienvenido al asistente. Escribe 'salir' para terminar.")

    model = OpenAIModel(api_key="tu_clave_de_api", model="gpt-4o-mini")
    storage = JSONStorage("conversations.json")
    assistant = ChatAssistant(model=model, storage=storage)

    while True:
        user_input = input("Tu: ")
        if user_input.lower() == "salir":
            print("¡Hasta luego!")
            break

        response = assistant.get_response(user_input)
        print(f"Asistente: {response}")

if __name__ == "__main__":
    main()
