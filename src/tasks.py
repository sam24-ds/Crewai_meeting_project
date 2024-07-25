from textwrap import dedent
from crewai import Task


class MeetingPrepTask():
    def research_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
            Effectuez des recherches approfondies sur chacune des personnes et des 
            entreprises impliquées dans la réunion à venir.
            Recueillez des informations sur les actualités récentes, les réalisations, les antécédents professionnels et toute activité 
            commerciale pertinente.
            
            Participants: {meeting_participants}
            Meeting Context: {meeting_context}"""),
            expected_output=dedent(f"""\
               Un rapport détaillé résumant les principales conclusions concernant chaque participant et chaque entreprise, en mettant en évidence 
               les informations susceptibles d'être utiles pour la réunion."""),
            async_execution=True,
            agent=agent
        )
        
    def industry_analysis_task(self, agent, meeting_participants, meeting_context):
        return Task(
            description=dedent(f"""\
            Analyser les tendances, les défis et les opportunités actuels du secteur dans le contexte de la réunion. Prendre en compte les rapports de marché, les développements récents et les avis d'experts 
            pour fournir une vue d'ensemble du paysage industriel.
            
            Participants: {meeting_participants}
            Meeting Context: {meeting_context}"""),
            expected_output=dedent(f"""\
               Une analyse perspicace qui identifie les principales tendances, les défis potentiels 
               et les opportunités stratégiques."""),
            async_execution=True,
            agent=agent
        ) 
        
    def meeting_strategy_task(self, agent, meeting_context, meeting_objectives):
        return Task(
            description=dedent(f"""\
            Élaborez des points de discussion stratégiques, des questions et des angles de discussion pour la réunion sur la base de la recherche 
            et de l'analyse sectorielle effectuées.
            
            Meeting_objectives: {meeting_objectives}
            Meeting Context: {meeting_context}"""),
            expected_output=dedent(f"""\
                Rapport complet avec une liste de points de discussion clés, de questions stratégiques à poser 
                pour aider à atteindre l'objectif de la réunion pendant la réunion."""),
            agent=agent
        )
        
    def summary_and_briefing_task(self, agent, meeting_context, meeting_objectives):
        return Task(
            description=dedent(f"""\
                Compilez tous les résultats de la recherche, l'analyse du secteur et les points de discussion stratégiques dans un document d'information concis et complet pour la réunion. 
                Veillez à ce que le briefing soit facile à assimiler et à ce que les participants à la réunion disposent de toutes les informations et stratégies nécessaires.
                
                Meeting_objectives: {meeting_objectives}
                Meeting Context: {meeting_context}"""),
            
            expected_output=dedent(f"""\
                Un document d'information bien structuré comprenant 
                des sections pour les biographies des participants, une vue d'ensemble de l'industrie, des points de discussion et des recommandations stratégiques."""),
            agent=agent
        )