from groq import Groq
from google.genai import types
from app.config import settings


client = Groq(api_key=settings.GROQ_API_KEY)
def generate_ans(ques:str,chunks:list[str]):
    prompt_str = f"""You are a helpful assistant. Answer the question using ONLY the context provided below.
            If the answer is not in the context, say "I cannot find this in the provided document."
            Do not use any outside knowledge.

            Context:
            {"".join(chunks)}

           Question:
           {ques}

            Answer:"""
    
    # result="creater of this rag is broke, he cant afford a ai"
    result = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt_str}]
    )
    return result.choices[0].message.content
