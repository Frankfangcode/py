# 🐍 Python AI 助手

一個在終端機執行的命令列問答工具，使用 [Groq](https://groq.com/) 的 `llama-3.3-70b-versatile` 模型，專門回答 Python 問題，並以**繁體中文**回覆、附上程式碼範例。

支援多輪對話（會記得前面聊過的內容）。

## 功能特色

- 💬 終端機即時問答，保留對話歷史
- 🐍 system prompt 已設定為「Python 專家、回答簡潔、附程式碼、用繁體中文」
- 📦 第一次執行會自動安裝 `groq` 套件
- 🚪 輸入 `q` / `quit` / `exit` / `bye` 即可離開

## 需求

- Python 3.8 以上
- 一組 Groq API Key（免費申請）

## 安裝與設定

### 1. 取得程式

```bash
git clone <你的-repo-網址>
cd test2
```

### 2. 申請 Groq API Key

1. 前往 [https://console.groq.com/keys](https://console.groq.com/keys)
2. 註冊／登入後建立一組新的 API Key（以 `gsk_` 開頭）
3. 複製下來

### 3. 填入 API Key

打開 `ask.py`，把第 6 行的預設文字換成你的 key：

```python
GROQ_API_KEY = "gsk_你的金鑰貼這裡"
```

> ⚠️ **安全提醒**：不要把填了真實金鑰的 `ask.py` 上傳到 GitHub 等公開平台，否則金鑰會外洩被盜用。若要公開分享程式碼，建議改用環境變數讀取（見下方）。

## 執行

```bash
python3 ask.py
```

啟動後就能直接輸入問題：

```
🐍 Python AI 助手 已啟動
輸入你的 Python 問題，輸入 q 離開

你: 怎麼讀取一個文字檔？
AI: 你可以用 open() ...

你: q
掰掰！
```

## 進階：用環境變數保管金鑰（推薦）

把金鑰寫死在程式碼裡並不安全。比較好的做法是改成從環境變數讀取，這樣程式碼可以安全公開，別人 clone 下來只要設定一個環境變數就能用。

將 `ask.py` 第 6 行改成：

```python
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("❌ 請先設定環境變數 GROQ_API_KEY")
    raise SystemExit(1)
```

然後在執行前設定環境變數：

```bash
# Mac / Linux
export GROQ_API_KEY="gsk_你的金鑰"

# Windows (PowerShell)
$env:GROQ_API_KEY="gsk_你的金鑰"
```

## 常見問題

**Q: 安裝 groq 套件失敗？**
程式預設使用 `pip install groq --break-system-packages`。若失敗，可手動建立虛擬環境後安裝：

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install groq
```

**Q: 出現金鑰相關錯誤？**
請確認 `ask.py` 裡的 `GROQ_API_KEY` 已換成真正的 key（`gsk_` 開頭），而不是預設文字。

## 授權

自由使用與修改。

