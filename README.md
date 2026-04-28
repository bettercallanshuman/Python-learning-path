# CLI Text Analyzer (v1.0)

A robust Command Line Interface (CLI) utility built to perform real-time text analysis and dynamic data sanitization. This project marks the transition from basic Python syntax to applied logic and product engineering.

## 🎯 Project Overview
The CLI Text Analyzer simulates a backend "content moderator" or "data processor." It takes a raw string input and passes it through three distinct analytical engines to extract metadata and perform specific data transformations.

## 🚀 Features

### 1. The Statistician (Text Analytics)
* **Total Character Count:** Calculates the absolute length of the input string.
* **The "Gap Principle" Word Count:** Implements a custom mathematical logic to estimate word count based on whitespace separators ($Words = Spaces + 1$).
* **Edge Case Handling:** Documented awareness of empty string logic gaps for future iterative improvements.

### 2. The Detective (Search & Discovery)
* **Sub-string Indexing:** Locates the precise memory coordinate (index) of a target word within the block.
* **Frequency Tracking:** Calculates the total occurrences of a specific term to identify patterns or spam.

### 3. The Dynamic Cleaner (Sanitization)
* **Intelligent Masking:** Unlike static censorship, this engine uses dynamic string multiplication.
* **Logic:** `len(target) * "*"` — Ensuring the mask length perfectly matches the "banned" word's length for a professional UI experience.

## 🧠 Engineering Thought Process
This build focuses on **Zero-Library Dependencies**. Every feature was architected using core Python String methods and logic, demonstrating mastery of:

* **Immutability:** Managing data states across different string transformations.
* **Data Type Integrity:** Solving `TypeError` obstacles by distinguishing between index coordinates (`int`) and string content (`str`).
* **FAANG-Aligned Workflow:** Utilizing a professional Git strategy with `wip:` (Work In Progress) and `feat:` (Feature) commit conventions.

[Image of software development lifecycle finalize and deploy]

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/bettercallanshuman/python-core-fundamentals.git](https://github.com/bettercallanshuman/python-core-fundamentals.git)

2. **Navigate to the project:**
   cd Project-Text_Analyzer

3. **Run the tool:**
   python text_analyzer.py

## Developed by Anshuman Das