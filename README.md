# Llama2: SDE INTERVIEW SUPPORT BOT

The Jobot is a powerful tool designed to provide Software Development information and interview assistance by answering user queries using state-of-the-art large language model(Llama2) and vector stores.

Hi fellow AI enthusiasts! I would like to share the steps you all can follow to clone the project in your system and have fun playing around and experimenting with it. Here are the steps for successful execution:

1. Clone the Repository

git clone <repository-url>
cd <repository-folder>

2. Set Up a Virtual Environment
   Install Python (3.8 or above required). Then create and activate a virtual environment:

For Windows:
python -m venv langchain
langchain\Scripts\activate

For macOS/Linux:
python3 -m venv langchain
source langchain/bin/activate

3. Install Required Dependencies
   Install all project dependencies from requirements.txt:

pip install -r requirements.txt

4. Download Required Model and Data Files

Download the Llama2 model from Hugging Face.
Place the model files in the designated directory (e.g., models/llama2/).

5. Configure the Environment

Set up API keys or environment variables, if required (e.g., OpenAI, Hugging Face).
Create a .env file (if applicable) and define necessary environment variables.
Example .env file:

OPENAI_API_KEY=your_api_key
HUGGINGFACE_API_KEY=your_api_key

6. Prepare the Vector Store (FAISS Database)
   If not already created, run the following command to index documents:

python ingest.py 7. Start the Chatbot
Run the chatbot application locally:

chainlit run app.py

8. Access the Application
   Open your browser and navigate to:
   http://localhost:8000

9. Test and Interact with the Chatbot
   Ask questions related to your trained dataset.
   Evaluate chatbot responses for accuracy and relevance.
