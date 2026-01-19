# Symbolic Rule-Based AI: Cybersecurity Expert System

A Python-based implementation of a **Symbolic Artificial Intelligence** system designed for cybersecurity threat detection. This project demonstrates the core principles of "Good Old-Fashioned AI" (GOFAI) by using an inference engine to process human-readable rules and facts.

## 🚀 Overview

Unlike modern Machine Learning which relies on statistical probabilities, this system uses **Symbolic Logic**. It separates the "Knowledge Base" (Security Rules) from the "Inference Engine" (Decision Logic), providing 100% transparency and explainability for every alert triggered.



## 🧠 Technical Milestones

- **Knowledge Representation:** Rules are defined as symbols and logical constraints rather than hard-coded nested loops.
- **Forward Chaining:** The system starts with user-provided facts (Working Memory) and searches for matching rules to reach a conclusion.
- **Decoupled Architecture:** The system is designed so that the Rules can be updated or expanded without ever touching the core Inference Engine code.
- **Explainable AI (XAI):** Every detection is backed by the specific logic triggers that caused it, making it ideal for security auditing.

## 🛠️ How It Works

The system follows a three-step process:
1. **Facts (Working Memory):** The system collects current network status from the user (e.g., failed logins, CPU spikes).
2. **Knowledge Base:** A set of predefined "If-Then" rules defining specific cyber threats.
3. **Inference Engine:** A logical processor that uses pattern matching (Unification) to determine if the facts satisfy any rule requirements.



## 💻 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/symbolic-ai-cybersecurity.git](https://github.com/your-username/symbolic-ai-cybersecurity.git)
