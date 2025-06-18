import os 
import pandas as pd
from pathlib import Path
import chromadb
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


groq_client = Groq()
chromadb_client = chromadb.Client()
collection_name_faq = 'faqs'



def ingest_faq_data(path):
    if collection_name_faq not in [c.name for c in chromadb_client.list_collections()]:
        print("Ingesting FAQ data into Chromadb...")
        collection = chromadb_client.get_or_create_collection(name=collection_name_faq)
        df = pd.read_csv(path)
        docs = df['question'].to_list()
        metadata = [{'answer': ans} for ans in df['answer'].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]

        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )

        print(f"FAQ Data successfully ingested into chroma collection: {collection_name_faq}")
    else:
        print(f"Collection {collection_name_faq} already exits!")



def get_relevant_qa(query):
    collection = chromadb_client.get_collection(name=collection_name_faq)
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result

    
def faq_chain(query):
    result = get_relevant_qa(query)
    context = ''.join([r.get('answer')for r in result['metadatas'][0]])
    answer = generate_answer(query, context)
    return answer
    

def generate_answer(query, context):
    prompt = f""" Given the question and context below, generate the answer based on the context only.
    if you don't find the answer inside the context then say "I don't any information on this context".
    Do not make things up. Give answer as ur the helping assistent


    QUESTION: {query}

    CONTEXT: {context}
    """

    chat_completion = groq_client.chat.completions.create(
        messages=[
              {
                "role": "user",
                "content": prompt,
            }
        ],

        model=os.environ['GROQ_MODEL']
    )
    return chat_completion.choices[0].message.content
    



if __name__ == "__main__":
    # ingest_faq_data(faqs_path)
    query = "Do you take cash as a payment option?"
    # result = get_relevant_qa(query)
    # print(result)
    answer = faq_chain(query)
    print("\n",answer)