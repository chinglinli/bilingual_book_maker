
# -*- coding: utf-8 -*-
import openai
import os
from os import environ as env

# 使用您的 OpenAI API 密鑰進行身份驗證
#openai.api_key = os.getenv("OPENAI_API_KEY")  # 將您的 API 密鑰設置為環境變量，或者直接在這裡填寫
openai.api_key = env.get("OPENAI_API_KEY")
def chat_gpt_response(prompt):
    response = openai.Completion.create(
       engine="text-davinci-002",
       #engine="text-babbage-001",
        prompt=prompt,
        temperature=0.5,
        max_tokens=500,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def chat_gpt_conversation(start_prompt, rounds=5, summary_round=None):
    conversation_history = start_prompt
    gpt1_message = ""
    gpt2_message = ""
    for i in range(rounds):
        gpt1_message = chat_gpt_response(conversation_history)
        conversation_history += f"\nGP-1: {gpt1_message}"

        #gpt2_message = chat_gpt_response(conversation_history + f"\nGP-1: {gpt1_message}")
        gpt2_message = f"\nGP-2:請解釋為什麼  "
        conversation_history += f"\nGP-2: {gpt2_message}"

        if summary_round is not None and i == summary_round - 1:
            summary_prompt = f"\nGP-1: {gpt1_message}\nGP-2: {gpt2_message}\n"
            summary = chat_gpt_response(summary_prompt)
            break

    return conversation_history, summary if summary_round is not None else None


if __name__ == "__main__":
    start_prompt = "what is chatgpt"
    rounds = 5
    summary_round = 5
    conversation_history, summary = chat_gpt_conversation(start_prompt, rounds, summary_round)

    print("history")
    print(conversation_history)
    print("\n Sumary")
    print(summary)