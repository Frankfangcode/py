import sys
import subprocess

# 直接把你的 Groq API Key 貼在這裡（gsk_ 開頭）
GROQ_API_KEY = "在這裡貼上你的key"

def get_api_key():
    if not GROQ_API_KEY or GROQ_API_KEY == "在這裡貼上你的key":
        print("❌ 還沒填 Groq API Key。")
        print("   請打開 ask.py，把 GROQ_API_KEY 換成你 gsk_ 開頭的 key。")
        sys.exit(1)
    return GROQ_API_KEY

def install_if_missing():
    try:
        import groq
    except ImportError:
        print("📦 正在安裝 groq 套件...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "groq", "--break-system-packages"])
        print("✅ 安裝完成！\n")

def ask(client, messages):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

def main():
    install_if_missing()
    from groq import Groq

    client = Groq(api_key=get_api_key())

    system_prompt = {
        "role": "system",
        "content": (
            "你是一個專門回答 Python 問題的 AI 助手。"
            "回答要簡潔清楚，附上程式碼範例。"
            "用繁體中文回答。"
        )
    }

    messages = [system_prompt]

    print(" Python answer")
    print("input Python question，enter q to quit\n")

    while True:
        try:
            user_input = input("you: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nbye！")
            break

        if not user_input:
            continue
        if user_input.lower() in ["q", "quit", "exit", "bye"]:
            print("bye！")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            print("AI: ", end="", flush=True)
            reply = ask(client, messages)
            print(reply)
            print()
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"❌ error：{e}")
            messages.pop()

if __name__ == "__main__":
    main()