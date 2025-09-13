# Synapse AI⚡

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?style=for-the-badge&logo=streamlit)
![Gemini API](https://img.shields.io/badge/Gemini%20API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)

![GitHub stars](https://img.shields.io/github/stars/OmKadane/synapse-ai?style=for-the-badge&logo=github)
![GitHub forks](https://img.shields.io/github/forks/OmKadane/synapse-ai?style=for-the-badge&logo=github)
![Maintained](https://img.shields.io/badge/Maintained-Yes-green.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

An advanced, role-based AI chat application built with Python, Streamlit, and the Google Gemini API. Interact with specialized AI agents in a sleek, real-time, streaming interface.

---

## 🗺️ Table of Contents
- [App Preview](#%EF%B8%8F-app-preview)
- [Features](#-features)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Getting Started](#-getting-started)
- [Running the Application](#%EF%B8%8F-running-the-application)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## 🖼️ App Preview

![Synapse AI Demo Response](https://ibb.co/prGCwJzX)

---

## ✨ Features
* **🎭 Selectable Agent Roles**: Switch between different AI personas like a Researcher, Analyzer, or Coordinator.
* **⚡ Real-Time Streaming**: Get instant, token-by-token responses from the AI for a fluid conversational experience.
* **📂 Sidebar Controls**: A clean, collapsible sidebar holds all controls, keeping the chat interface tidy.
* **ℹ️ Dynamic Agent Descriptions**: Understand each agent's specialty with contextual descriptions in the sidebar.
* **🗑️ Clear Chat History**: Easily reset the conversation with a single click.
* **🎨 Modern UI with Avatars**: A sleek, custom-styled dark theme with user and assistant avatars for clarity.
* **💡 Simulation Mode**: The app runs in a fully functional demo mode if no API key is provided.

---

## 🛠️ Tech Stack
* **Backend**: Python
* **Frontend**: Streamlit
* **AI Model**: Google Gemini Pro (via `google-generativeai`)
* **Dependencies**: `python-dotenv` for environment management

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

#### Prerequisites
* Python 3.8 or higher
* An active Google Gemini API Key

#### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/OmKadane/synapse-ai.git
    cd synapse-ai
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your environment variables:**
    Create a file named `.env` in the root of the project folder and add your Gemini API key:
    ```env
    GOOGLE_API_KEY="your_actual_api_key_paste_it_here"
    ```

---

## 🏃‍♂️ Running the Application

Once the installation is complete, run the following command in your terminal:
```bash
streamlit run synapse_ai_app.py
```

---

## 📂 Project Structure

Here is an overview of the project's file structure:
```
synapse-ai/
├── .env                # Stores your secret API key (ignored by Git)
├── .gitignore          # Specifies files for Git to ignore
├── README.md           # You are here!
├── requirements.txt    # Lists project dependencies for pip
└── synapse-ai_app.py   # The main Streamlit application script
```

---

## 📄 License

Distributed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.
