from dotenv import load_dotenv
from crewai import Crew
from tasks import MeetingPrepTask
from agents import MeetingPrepAgents

load_dotenv()

tasks = MeetingPrepTask()
agents = MeetingPrepAgents()

print("## Bienvenue à l'équipe de préparation des réunions")
print('-------------------------------')
participants = input("Quels sont les courriels des participants (autres que vous) à la réunion ?\n")
context = input("Quel est le contexte de la réunion ?\n")
objective = input("Quel est l'objectif de cette réunion ?\n")


# Create Agents
researcher_agent = agents.research_agent()
industry_analyst_agent = agents.industry_analysis_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()


# Create Tasks
research = tasks.research_task(researcher_agent, participants, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, context)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

meeting_strategy.context = [research, industry_analysis]
summary_and_briefing.context = [research, industry_analysis, meeting_strategy]



# Create Crew responsible for Copy
crew = Crew(
	agents=[
		researcher_agent,
		industry_analyst_agent,
		meeting_strategy_agent,
		summary_and_briefing_agent
	],
	tasks=[
		research,
		industry_analysis,
		meeting_strategy,
		summary_and_briefing
	]
)

game = crew.kickoff()
