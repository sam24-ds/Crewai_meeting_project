import os
from dotenv import load_dotenv
from exa_py import Exa
from langchain.agents import tool

load_dotenv()

class ExaSearchToolset():
    
    @tool
    def search(query: str):
        """Recherche d'une page web sur la base de la requête."""
        return ExaSearchToolset._exa().search(f"{query}", use_autoprompt=True, num_results=3)
    
    @tool
    def find_similar(url: str):
        """Recherche les pages web similaires à une URL donnée.
           L'URL passée doit être une URL renvoyée par `search`.
        """
        return ExaSearchToolset._exa().find_similar(url, num_results=3)
    
    @tool
    def get_contents(ids: str):
        """Obtenir le contenu d'une page web.
           Les identifiants doivent être passés sous forme de liste, une liste d'identifiants renvoyés par `search`.
        """
        ids = eval(ids)
        contents = str(ExaSearchToolset._exa().get_contents(ids))
        print(contents)
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)
    
    def tools():
        return [ExaSearchToolset.search, ExaSearchToolset.find_similar, ExaSearchToolset.get_contents]
    
    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))
    
        