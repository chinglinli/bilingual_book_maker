
import openai
from os import environ as env

openai.api_key = env.get("OPENAI_API_KEY")

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# 對話歷史Win11NB modify
conversation_history = ""

# GPT-1 提問
question1 = "如何提高供應鏈效率？"
conversation_history += f"User: {question1}\n"
answer1 = generate_text(conversation_history)
conversation_history += f"GPT-1: {answer1}\n"

# GPT-2 提問
question2 = "實現供應鏈透明度的好方法是什麼？"
conversation_history += f"User: {question2}\n"
answer2 = generate_text(conversation_history)
conversation_history += f"GPT-2: {answer2}\n"

# 請求摘要
summary_prompt = f"根據前面的對話，請總結關於提高供應鏈效率的 why、how 和 what：\n{conversation_history}"
summary = generate_text(summary_prompt)
print(summary)
input()