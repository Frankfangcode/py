
































import sys
import subprocess

# 把你的 OpenAI API Key 貼在這裡（sk- 開頭）
OPENAI_API_KEY = ""

# 要使用的模型，可換成 gpt-4o、gpt-4o-mini、gpt-4-turbo 等
MODEL = "gpt-4o-mini"

def get_api_key():
    if not OPENAI_API_KEY or OPENAI_API_KEY == "在這裡貼上你的key":
        print("❌ 還沒填 OpenAI API Key。")
        print("   請打開 ask_gpt.py，把 OPENAI_API_KEY 換成你 sk- 開頭的 key。")
        print("   取得 Key：https://platform.openai.com/api-keys")
        sys.exit(1)
    return OPENAI_API_KEY

def install_if_missing():
    try:
        import openai
    except ImportError:
        print("📦 正在安裝 openai 套件...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openai", "--break-system-packages"])
        print("✅ 安裝完成！\n")

def ask(client, messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

def main():
    install_if_missing()
    from openai import OpenAI

    client = OpenAI(api_key=get_api_key())

    system_prompt = {
        "role": "system",
        "content": (
            "你是一個專門回答 Python 問題的 AI 助手。"
            "回答要簡潔清楚，附上程式碼範例。"
            "用繁體中文回答。"
        )
    }

    messages = [system_prompt]

    print(f"🤖 ChatGPT ({MODEL}) Python 問答")
    print("輸入 Python 問題，輸入 q 離開\n")

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

    #sk
#-proj-D0-7QR9xTQO0uIm
# T7wnB0wjGj3AL1kdEtFyf2klEedrKdkcvc_k92S-
# sPy9yyW33jiTVL4RQ5QT3BlbkFJOBxKhJuhJF8-
# _7DK68CEKXNBVwgApBDGpNTzh6AW--
# bvJzgjVL3VEVSXHj
# davGeQtysQ73gX8A