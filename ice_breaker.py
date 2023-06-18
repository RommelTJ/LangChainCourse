from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
import json
from agents.linkedin_lookup_agent import lookup


name = "Rommel Rico San Diego"
if __name__ == "__main__":
    linkedin_profile_url = lookup(name=name)
    print(linkedin_profile_url)
    with open("./third_parties/linkedin_data.json", "r") as f:
        data = json.load(f)
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    linkedin_data = data

    tweets = scrape_user_tweets(username=name)

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

    print(chain.run(information=linkedin_data))
