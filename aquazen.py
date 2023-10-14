
import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a friendly chatbot that helps in water cleanliness system"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "AquaZen")

demo.launch(share=True)
