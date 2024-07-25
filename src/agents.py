from textwrap import dedent
import os
from dotenv import load_dotenv
from crewai import Agent
from tools import ExaSearchToolset
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()
"""
##call the gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.environ.get('GOOGLE_API_KEY')
)
"""

##call the llama3 models
llm=ChatGroq(temperature=0.5,
             model_name="llama-3.1-70b-versatile",
             api_key=os.environ.get('YOUR_GROQ_API_KEY')
)

class MeetingPrepAgents():
    def research_agent(self):
        return Agent(
            role="Research Specialist",
            goal="Effectuer des recherches approfondies sur les personnes et les entreprises impliquées dans la réunion",
            tools=ExaSearchToolset.tools(),
            backstory=dedent(f"""\
                En tant que spécialiste de la recherche, votre mission consiste à découvrir des informations détaillées sur les personnes et les entités participant à la réunion. 
                Vos informations jetteront les bases d'une préparation stratégique de la réunion."""),
            verbose=True,
            llm=llm
        )
        
    def industry_analysis_agent(self):
        return Agent(
          role='Industry Analyst',
                goal='Analyser les tendances, les défis et les opportunités actuels du secteur',
                tools=ExaSearchToolset.tools(),
                backstory=dedent("""\
                        En tant qu'analyste du secteur, vous identifierez les principales tendances, les défis auxquels le secteur est confronté et 
                        les opportunités potentielles qui pourraient être exploitées au cours de la réunion pour en tirer un avantage stratégique."""),
                verbose=True,
                llm=llm
		)
        
    def meeting_strategy_agent(self):
        return Agent(
          role='Meeting Strategy Advisor',
                goal='Élaborer des points de discussion, des questions et des angles stratégiques pour la réunion',
                tools=[],
                backstory=dedent("""\
                        En tant que conseiller stratégique, votre expertise vous permettra d'élaborer des sujets de discussion, des questions perspicaces 
                        et des angles stratégiques afin de garantir la réalisation des objectifs de la réunion."""),
                verbose=True,
                llm=llm
        )
    
    def summary_and_briefing_agent(self):
        return Agent(
            role='Briefing Coordinator',
                goal="Compiler toutes les informations recueillies dans un document d'information concis et instructif.",
                tools=[],
                backstory=dedent("""\
                        En tant que coordinateur des briefings, votre rôle est de consolider la recherche, l'analyse et les idées stratégiques."""),
                verbose=True,
                llm=llm
            )

    
        
        
    
      
   

	
    