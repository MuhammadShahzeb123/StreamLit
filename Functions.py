import openai 
import os

class Main:
    def Get_answer(question):
        Answer = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return Answer["choices"][0]["text"]

    def Python_Code(query):
        role = "You are expert Python Programmer for over 20 Years. You have to help me out with the Problem and convert in into a code that can solve my Problem."
        comment = "Please code it with Python and don't implement any comments. Don't write anything except Code even don't write that I can do this and that...."
        Python_Code = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{role} My Problem: {query}.{comment}",
        temperature=1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return Python_Code["choices"][0]["text"]

    def terminal(command):
        while True:
            if command == "break":
                break
            os.system(command)

    def PythonCodeChecker(self) -> str:
        Code = Main.Python_Code()
        os.system(f"python {Code}")