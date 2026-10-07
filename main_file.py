

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="gemma4:e4b")

template = '''
you are a helpfull assistant. you need to provide answers for the questions about pizza restaurant.

here are some relevant reviews : {reviews}

here is the question to be answered : {question}
'''

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


while True:

    print('\n\n------------------------------------------------------')
    question = input('Ask your question (q to Quit) :')
    print ('\n\n-----------------------------------------------------')

    if question == 'q':
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({'reviews': reviews, 'question': question})

    print ('result: ', result)