from tools.CustomSerpAPIWrapper import CustomSerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for a LinkedIn Profile Page"""
    search = CustomSerpAPIWrapper()
    result = search.run(f"{text}")
    return result
