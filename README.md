# 🪙 CAP Auto Claim Bot

A simple bot to automatically mint cUSD tokens on the [CAP Testnet](https://cap.app/testnet) using Web3.

## ⚙️ Features
- Auto claim every 60 seconds
- Web3-based transaction signing
- Supports any working RPC
- Pretty CLI logs with colors & emojis

---

## 🚀 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/zimma-web/cap-autoclaim-bot.git
cd cap-autoclaim-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
If `requirements.txt` doesn't exist, install manually:
```bash
pip install web3 python-dotenv termcolor
```

### 3. Create `.env` file
Create a `.env` file in the project root:
```ini
RPC_URL=https://your-cap-testnet-rpc-url
PRIVATE_KEY=0xYOUR_PRIVATE_KEY
MY_WALLET=0xYOUR_WALLET_ADDRESS
```
> ⚠️ NEVER share your private key. Keep this file private!

### 4. Run the Bot
```bash
python bot.py
```
The bot will:
- Connect to the RPC
- Build + sign a mint transaction
- Send and confirm the TX
- Repeat every 60 seconds

---

## 🛠 Requirements
- Python 3.8+
- A valid wallet with private key
- A working RPC URL from CAP testnet

Example public RPC: `https://rpc.cap.ankr.com/YOUR_API_KEY`

---

## 📸 Sample Output
```
==============================
🔗  RPC Connected : https://rpc.cap.ankr.com
👛  Wallet        : 0x1234...abcd
🌐  Chain ID      : 6342
==============================

💰 Starting Mint #1...
📤 Sending TX...
✅ TX Sent: 0xabc123...
🎉 Success! cUSD minted.
⏳ Waiting 60 seconds before next mint...
```

---

## 💡 Tips
- You can host this bot on Termux, VPS, or Raspberry Pi.
- Always rotate your RPCs if you're rate-limited.
- Use `.gitignore` to keep your `.env` safe:
  ```
  .env
  __pycache__/
  ```

---

## 📄 License
MIT © [zimma-web](https://github.com/zimma-web)
