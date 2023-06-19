from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from output_parsers import person_intel_parser
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
import json
from agents.linkedin_lookup_agent import linkedin_lookup_agent
from agents.twitter_lookup_agent import twitter_lookup_agent


def ice_break(name: str) -> str:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    with open("./third_parties/linkedin_data.json", "r") as f:
        linkedin_data = json.load(f)
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_lookup_agent(name=name)
    with open("./third_parties/twitter_data.json", "r") as f:
        twitter_data = json.load(f)
    # twitter_data = scrape_user_tweets(username=twitter_username)

    summary_template = """
        Given the LinkedIn information {linkedin_info} and Twitter information {twitter_info} about a person from whom 
        I want you to create:
        1. A short summary
        2. Two interesting facts about them
        3. A topic that may interest them
        4. 2 creative ice breakers to open a conversation with them
        
        \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_info", "twitter_info"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    return chain.run(linkedin_info=linkedin_data, twitter_info=twitter_data)


if __name__ == "__main__":
    name = "Barack Obama"
    output = ice_break(name)
    print(output)
