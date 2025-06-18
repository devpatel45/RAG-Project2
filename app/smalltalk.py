import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client_talk = Groq()

def small_talk(query):
    prompt = f""" Given the question generate the answer Give answer as you are a helping assistant and you are not meant to chat but help them
    QUESTION: {query}
    """
    
    completion = client_talk.chat.completions.create(
        model=os.environ['GROQ_MODEL'],
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ]
    )
    return completion.choices[0].message.content
if __name__ == "__main__":
    result = small_talk("Is any one there")
    print(result)