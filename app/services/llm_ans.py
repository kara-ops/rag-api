from google import genai
from google.genai import types
from app.config import settings


client = genai.Client(api_key=settings.GEMINI_API_KEY)
def generate_ans(ques:str,chunks:list[str]):
    prompt_str = f"""You are a helpful assistant. Answer the question using ONLY the context provided below.
            If the answer is not in the context, say "I cannot find this in the provided document."
            Do not use any outside knowledge.

            Context:
            {"".join(chunks)}

           Question:
           {ques}

            Answer:"""
    
    result="creater of this rag is broke, he cant afford a ai"
    # result = client.models.generate_content(
    #     model="gemini-2.0-flash-lite",
    #     contents=prompt_str
    # )
    return result