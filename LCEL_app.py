from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables (e.g. GROQ API keys)
load_dotenv()

st.sidebar.title("**Options**")
model_options = ["llama3-8b-8192", "llama3-70b-8192" , 'llama-3.1-8b-instant' ]
st.sidebar.markdown("### Select the Model of your Choice:")
model_name = st.sidebar.selectbox("", model_options)


# language = 

languages = [
    "English",
    "Mandarin Chinese",
    "Spanish",
    "Arabic",
    "French",
    "Russian",
    "Portuguese",
    "German",
    "Japanese",
    "Korean",
    "Italian",
    "Turkish",
    "Dutch",
    "Polish",
    "Ukrainian",
    "Urdu","Pashto" , "Sindhi" , "Swiss"
]
st.sidebar.markdown("### Select the language to convert into:")

target_language = st.sidebar.selectbox("", languages)
# --- Streamlit UI ---
st.title("🌍 Language Converter GenAI App")

# Text input for user
input_text = st.text_area("Enter English text to convert:", height=150)

# Button to generate translation
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some English text to convert.")
    else:
        # Initialize model
        model = ChatGroq(model=model_name)
        
        # Prompt template (you can customize this further)
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"Translates {input_text} to {target_language} language."),
            ("human", "{input}")
        ])
        
        chain = prompt | model | StrOutputParser()
        
        with st.spinner("Translating..."):
            output = chain.invoke({"input": input_text})
        
        # Display result
        st.success(f"Translation in {target_language}:")
        st.write(output)
