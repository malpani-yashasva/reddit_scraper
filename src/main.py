import argparse
import yaml
from reddit_collector import RedditCollector
from llm_client import LLMClient

def load_config(path="config/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():

    parser = argparse.ArgumentParser(description="Extract Reddit user profile and analyze it.")
    parser.add_argument("--url", required=True, help="Reddit profile URL")
    args = parser.parse_args()

    config = load_config()
    reddit_cfg = config["reddit"]
    llm_cfg = config["llm"]

    collector = RedditCollector(
        client_id=reddit_cfg["client_id"],
        client_secret=reddit_cfg["client_secret"],
        user_agent=reddit_cfg["user_agent"],
        username=reddit_cfg["username"],
        password=reddit_cfg["password"]
    )

    llm = LLMClient(
        api_key=llm_cfg["cohere_api_key"],
        model="command-a-03-2025"
    )
    username = collector.extract_username(args.url)
    posts, comments = collector.fetch_user_texts(args.url)

    texts = posts + comments
    texts_enumerated = [f"[{i+1}] {t.strip()}" for i, t in enumerate(texts)]
    print("Writing extracted posts and comments with indexing to " + f"{username}_texts.txt")
    with open(f"{username}_texts.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(texts_enumerated))
    
    result = llm.create_chat(texts_enumerated)
    if result:
        with open(f"{username}_persona.txt", "w", encoding="utf-8") as f:
            f.write(result.message.content[0].text)
        print(f"\nOutput saved to '{username}_persona.txt'")
    else:
        print("LLM failed to generate a response.")

if __name__ == "__main__":
    main()