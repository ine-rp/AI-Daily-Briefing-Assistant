from crewai import Crew, Task, LLM
#from langchain_openai import ChatOpenAI
from agents.email_agent import email_agent
from agents.calendar_agent import calendar_agent
from agents.summary_agent import summary_agent
from tasks.analyze_calendar import analyze_calendar
from tasks.compose_briefing import compose_briefing
from tasks.summarize_emails import summarize_emails
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = LLM(model="gemini/gemini-2.0-flash")

crew = Crew(
    agents=[email_agent, calendar_agent, summary_agent],
    tasks=[analyze_calendar,
           summarize_emails,
           compose_briefing
        ],
    process="sequential",
    llm=llm,
    verbose=True
)