# Llama2: SDE INTERVIEW SUPPORT BOT
Jobot is an AI-driven chatbot leveraging state-of-the-art Large Language Models (LLMs) to simulate technical interview scenarios for aspiring software developers. Built on a robust foundation of advanced natural language processing (NLP), information retrieval, and embeddings-based search techniques, the project integrates tools like FAISS for vector search, LangChain for conversational AI orchestration, and the Llama2 model for contextual understanding. By providing intelligent, interactive coaching on programming concepts and problem-solving techniques, Jobot empowers users to improve their technical communication and analytical skills while receiving real-time, personalized feedback.

Key Features:
Technologies Used:

Programming Languages: Python
AI Models: Llama2 (Quantized)
Frameworks and Libraries: LangChain, FAISS, Hugging Face Transformers
Data Preprocessing: Pandas, NumPy
Vector Store: FAISS (Facebook AI Similarity Search)
Environment Management: Virtual environments using Conda
Lightweight deployment using quantization for efficient CPU usage.
Quantized Llama2 on CPU Systems:
This project utilizes the quantized version of the Llama2 model, making it highly efficient for systems with limited GPU resources or entirely CPU-based systems. The quantized model significantly reduces memory usage and computational requirements while maintaining high performance. By leveraging this optimization, Jobot enables users with low-spec hardware to run a chatbot powered by Large Language Models (LLMs) seamlessly. This democratizes access to AI technologies, ensuring a broader range of users can benefit from advanced interview coaching without needing expensive hardware.

This project is ideal for those seeking to refine their technical skills and ace software development interviews while ensuring accessibility for everyone, regardless of hardware constraints.

Hi fellow AI enthusiasts! I would like to share the steps you all can follow to clone the project in your system and have fun playing around and experimenting with it. Here are the steps for successful execution:

1. Clone the Repository
```shell
git clone <repository-url>
cd <repository-folder>
```

2. Set Up a Virtual Environment
   Install Python (3.8 or above required). Then create and activate a virtual environment:

For Windows:
```shell
python -m venv langchain
langchain\Scripts\activate
```
For macOS/Linux:
```shell
python3 -m venv langchain
source langchain/bin/activate
```

3. Install Required Dependencies
   Install all project dependencies from requirements.txt:
```shell
pip install -r requirements.txt
```

4. Download Required Model and Data Files

Download the Llama2 model from Hugging Face.
Place the model files in the designated directory (e.g., models/llama2/).

5. Configure the Environment
Set up API keys or environment variables, if required (e.g., OpenAI, Hugging Face).
Create a .env file (if applicable) and define necessary environment variables.
Example .env file:
```env
OPENAI_API_KEY=your_api_key
HUGGINGFACE_API_KEY=your_api_key
```

6. Prepare the Vector Store (FAISS Database)
   If not already created, run the following command to index documents:
```shell
python ingest.py
```

7. Start the Chatbot
Run the chatbot application locally:
```shell
chainlit run app.py
```

8. Access the Application
   Open your browser and navigate to:
   http://localhost:8000

9. Test and Interact with the Chatbot
   Ask questions related to your trained dataset.
   Evaluate chatbot responses for accuracy and relevance.
