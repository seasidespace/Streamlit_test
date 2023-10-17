from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
import streamlit as st
import os
import openai
from snowflake.snowpark import Session
import re


#db = SQLDatabase.from_uri("sqlite:///Chinook.db")

@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets["connections.snowpark"]).create()

session = create_session()
st.success("Connected to Snowflake!")

# Initialize the chat messages history
openai.api_key = st.secrets.OPENAI_API_KEY

llm = OpenAI(temperature=0, verbose=True)

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0)),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run(
    "List the total sales per country. Which country's customers spent the most?"
)

