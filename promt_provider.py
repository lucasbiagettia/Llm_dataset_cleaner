from langchain.prompts import SystemMessagePromptTemplate

class PromptProvider:
    def __init__(self, prompt_string):
        self.prompt_strig = prompt_string
        self.prompt = self._load_prompt_template(prompt_string)

    def _load_prompt_template(self, prompt_string):
        PROMPT = (
            SystemMessagePromptTemplate.from_template(prompt_string)
            + "{context}"
        )
        return PROMPT

    def get_prompt(self):
        return self.prompt

# Ejemplo de uso
prompt_provider = PromptProvider("Ingrese su nombre: ")
print(prompt_provider.get_prompt())
