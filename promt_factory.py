from langchain.prompts import SystemMessagePromptTemplate, PromptTemplate


class PromptFactory:
    def get_custom_prompt(self, custom_prompt):
        return self._load_prompt_template(custom_prompt)

    def get_question_generator_prompt(self, n_questions=10):


        prompt_string = '''En base al documento que se te proporciona como contexto genera {} preguntas de forma aleatoria.
        Debes devolver un XML con una única etiqueta root y una clave q con una lista de preguntas.
        Ejemplo del XML:
        <root>
            <q>Pregunta 1</q>
            <q>Pregunta 2</q>
            <q>Pregunta 3</q>
            <q>Pregunta 4</q>
            <q>Pregunta 5</q>
            <q>Pregunta 6</q>
            <q>Pregunta 7</q>
            <q>Pregunta 8</q>
            <q>Pregunta 9</q>
            <q>Pregunta 10</q>
        </root>

        {{contexto}}
        '''

        prompt_string = prompt_string.format(n_questions)

      
        return self._load_prompt_template(prompt_string)




    
    def _load_prompt_template(self, prompt_string):


        PROMPT = PromptTemplate(
            template=prompt_string, input_variables=["contexto"]
        )
        return PROMPT



