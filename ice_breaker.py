from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
Rodrigo Hernández Cascante (born 22 June 1996), known as Rodri or Rodrigo, is a Spanish professional footballer who plays as a defensive midfielder for Premier League club Manchester City and the Spain national team.

After stints with Villarreal and Atlético Madrid in La Liga, Rodri joined Premier League club Manchester City in 2019. He helped the team win three consecutive league titles, in the 2020–21, 2021–22, 2022–23 seasons. Rodri was part of the City team which sealed the club's first continental treble in the 2022–23 season. This treble included a maiden UEFA Champions League triumph, with Rodri scoring the only goal in the final and being named the competition's player of the season.[5]

Rodri is a Spain international and former youth international. He made his debut for the senior national team in 2018 and represented his country at UEFA Euro 2020 and the 2022 FIFA World Cup. 
"""

if __name__ == "__main__":
    summary_template = """
        Given the LinkedIn information {information} about a person from whom I want you to create:
        1. A short summary
        2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(information=information))
