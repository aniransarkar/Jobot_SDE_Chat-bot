from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl

DB_FAISS_PATH = 'vectorstore/db_faiss'

custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt

#Retrieval QA Chain
def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )
    return qa_chain

#Loading the model
def load_llm():
    # Load the locally downloaded model here
    llm = CTransformers(
        model = "TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

#QA Model Function
# def qa_bot():
#     embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
#                                        model_kwargs={'device': 'cpu'})
#     db = FAISS.load_local(DB_FAISS_PATH, embeddings)
#     llm = load_llm()
#     qa_prompt = set_custom_prompt()
#     qa = retrieval_qa_chain(llm, qa_prompt, db)

#     return qa
def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)

    return qa


#output function
# def final_result(query):
#     qa_result = qa_bot()
#     response = qa_result({'query': query})
#     return response

import re  # Import regular expressions for text cleaning

def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})

    # Remove unwanted characters like newlines and extra whitespace
    clean_response = re.sub(r'\s+', ' ', response['result']).strip()  # Replaces any whitespace sequence with a single space
    response['result'] = clean_response

    return response


#chainlit code
@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to Jobot: Your SDE Interview Support bot. What is your query?"
    await msg.update()

    cl.user_session.set("chain", chain)


@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")
    
    # Send a loading message with "typing" animation
    loading_msg = cl.Message(content="Generating response, please wait...")
    await loading_msg.send()

    # Retrieve the answer
    res = await chain.acall(message.content)

    # Clean up the main answer text
    full_answer = re.sub(r'\s+', ' ', res["result"]).strip()

    # Optionally simplify source display
    sources = res["source_documents"]
    source_text = ""
    if sources:
        for source in sources:
            # Extract and clean the page content for each source, limiting to 200 chars
            content = re.sub(r'\s+', ' ', source.page_content).strip()
            source_text += f"\nSource: {content[:200]}..."  # Limit to 200 chars for readability

    # Append source text if available
    # if source_text:
    #     full_answer += f"\nSources:{source_text}"
    # else:
    #     full_answer += "\nNo sources found"

    # Typing effect: send message chunk by chunk
    chunk_size = 20  # Define the number of characters to display at once
    typed_text = ""
    for i in range(0, len(full_answer), chunk_size):
        typed_text += full_answer[i:i + chunk_size]
        loading_msg.content = typed_text
        await loading_msg.update()
        await cl.sleep(0.2)  # Adjust delay for the speed of typing effect





# @cl.on_message
# async def main(message: cl.Message):
#     chain = cl.user_session.get("chain")

#     # Initial loading message
#     loading_msg = cl.Message(content="Generating response, please wait...")
#     await loading_msg.send()

#     # Retrieve the answer
#     res = await chain.acall(message.content)
    
#     # Clean up the main answer text
#     answer = re.sub(r'\s+', ' ', res["result"]).strip()

#     # Optionally simplify source display
#     sources = res["source_documents"]
#     source_text = ""
#     if sources:
#         for source in sources:
#             # Extract and clean the page content for each source, limiting to 200 chars
#             content = re.sub(r'\s+', ' ', source.page_content).strip()
#             source_text += f"\nSource: {content[:200]}..."  # Limit to 200 chars for readability
    
#     # Append source text if available
#     if source_text:
#         answer += f"\nSources:{source_text}"
#     else:
#         answer += "\nNo sources found"

#     # Update the loading message with the final answer
#     loading_msg.content = answer
#     await loading_msg.update()



# @cl.on_message
# async def main(message: cl.Message):
#     chain = cl.user_session.get("chain")

#     # Call chain directly without callback handler
#     res = await chain.acall(message.content)
    
#     # Clean up the main answer text
#     answer = re.sub(r'\s+', ' ', res["result"]).strip()

#     # Optionally simplify source display
#     sources = res["source_documents"]
#     source_text = ""
#     if sources:
#         for source in sources:
#             # Extract and clean the page content for each source, limiting to 200 chars
#             content = re.sub(r'\s+', ' ', source.page_content).strip()
#             source_text += f"\nSource: {content[:200]}..."  # Limit to 200 chars for readability
    
#     # Append source text if available
#     if source_text:
#         answer += f"\nSources:{source_text}"
#     else:
#         answer += "\nNo sources found"

#     # Send the cleaned, single instance of the answer
#     await cl.Message(content=answer).send()



# @cl.on_message
# async def main(message: cl.Message):
#     chain = cl.user_session.get("chain")
#     cb = cl.AsyncLangchainCallbackHandler(
#         stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
#     )
#     cb.answer_reached = True
#     res = await chain.acall(message.content, callbacks=[cb])
    
#     # Clean up the main answer text
#     answer = re.sub(r'\s+', ' ', res["result"]).strip()

#     # Optionally simplify source display
#     sources = res["source_documents"]
#     source_text = ""
#     if sources:
#         for source in sources:
#             # Extract and clean the page content for each source
#             content = re.sub(r'\s+', ' ', source.page_content).strip()
#             source_text += f"\nSource: {content[:200]}..."  # Limit to 200 chars for readability
    
#     if source_text:
#         answer += f"\nSources:{source_text}"
#     else:
#         answer += "\nNo sources found"

#     await cl.Message(content=answer).send()

# @cl.on_message
# async def main(message: cl.Message):
#     chain = cl.user_session.get("chain") 
#     cb = cl.AsyncLangchainCallbackHandler(
#         stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
#     )
#     cb.answer_reached = True
#     res = await chain.acall(message.content, callbacks=[cb])
#     answer = res["result"]
#     sources = res["source_documents"]

#     if sources:
#         answer += f"\nSources:" + str(sources)
#     else:
#         answer += "\nNo sources found"

#     await cl.Message(content=answer).send()