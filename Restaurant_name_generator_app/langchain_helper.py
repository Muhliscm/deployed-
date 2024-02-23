from langchain.llms import OpenAI
from langchain.chains import SequentialChain, LLMChain
from langchain.prompts import PromptTemplate
from secretkey import open_ai_key
import os
import streamlit as st
import openai

os.environ["OPENAI_API_KEY"] = open_ai_key


def langchain_name_menu_gen(cuisine):

    llm1 = OpenAI(temperature=0.6)

    propmpt_rest_name = PromptTemplate(
        input_variables=[cuisine],
        template="Generate One Best name for {country} restaurant",
    )

    rest_name_chain = LLMChain(
        llm=llm1, prompt=propmpt_rest_name, output_key="restaurant_name"
    )

    prompt_menu_names = PromptTemplate(
        input_variables=["restaurant_name"],
        template="suggest some menu items for {restaurant_name} without description and separated by comma",
    )

    llm2 = OpenAI(temperature=0.6)

    rest_menu_chain = LLMChain(
        llm=llm2, prompt=prompt_menu_names, output_key="menu_items"
    )

    chain = SequentialChain(
        chains=[rest_name_chain, rest_menu_chain],
        input_variables=["country"],
        output_variables=["restaurant_name", "menu_items"],
    )
    return chain({"country": cuisine})


def open_ai_connector(cuisine):
    try:
        return langchain_name_menu_gen(cuisine)
    except openai.RateLimitError:
        st.warning("Api Limit Exceeded")
    except Exception:
        st.error("Exception occurred")


if __name__ == "__main__":
    print(open_ai_connector("Indian"))
