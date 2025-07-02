# 🔗 Mini-Chain

**Mini-Chain** is a simple yet functional blockchain prototype implemented in Python. It helps developers, students, and enthusiasts understand the core principles behind blockchain technology without the overhead of cryptocurrencies, peer-to-peer networking, or mining.

---

## 🚀 What Is Mini-Chain?

Mini-Chain is a minimal blockchain implementation built entirely in Python. It provides a **foundational framework** for learning how blockchains work — including block creation, linking via hashes, and storing immutable data. 

It’s a great starting point for:

- Learning how blocks are created and hashed
- Understanding how each block links to the previous one
- Exploring how a chain of trust and immutability is formed
- Rapidly prototyping blockchain logic before adding features like wallets or consensus

---

## 🧠 Why Mini-Chain Matters

Despite the hype, blockchain fundamentals are often misunderstood. Mini-Chain solves this problem by stripping blockchain down to its core essentials, letting you:

- Learn how block hashes work
- See how blockchains grow over time
- Understand how data integrity is maintained
- Modify or extend with your own logic (transactions, validators, P2P, etc.)

---

## 🏗️ Project Structure

📁 mini-chain/
- 🐍 block.py: Contains the Block class and block creation logic
- 🐍 main.py: Runs the blockchain, adds blocks, and prints them
- 📄 README.md: You're reading it!


### 🧱 `block.py`

- `Block` class: defines what each block contains and how it’s hashed.
- `create_genesis_block()`: creates the first block in the chain.
- `next_block(last_block)`: creates the next block, linked to the previous one.

### 🧪 `main.py`

- Imports the logic from `block.py`
- Builds a chain of 20 blocks
- Prints each block’s index and hash as they’re added

---

## ▶️ How to Run

> ⚙️ Requirements: Python 3.x (no external dependencies)

1. Clone the repository or download the files.
2. In your terminal, navigate to the project folder.
3. Run:

```bash
python main.py
```

You’ll see output like:
Block #1 has been added to the blockchain!
Hash: 89b0e2...

Block #2 has been added to the blockchain!
Hash: a7d231...
