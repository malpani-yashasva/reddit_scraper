import cohere


class LLMClient:
    def __init__(self, api_key, model="command-a-03-2025"):
        self.co = cohere.ClientV2(api_key=api_key)
        self.model = model
    
    def generate_system_message(self):
        system_message = """You are given a numbered list of a user's Reddit posts and comments.

Extract up to five points each for:
- Personality traits including introversion, extrroversion or ambiversion. Also include age if mentioned or predict the age.
- Likes
- Dislikes
- Goals or ambitions

After each point, include the ID(s) input(s) that heavily support that conclusion. Format it like this:

- Likes:
  1. Enjoys hiking [1]
  2. Likes AI and climate science [3]

- Dislikes:
  1. Dislikes long queues [2]

Be concise and avoid repetition."""
        return system_message

    def create_chat(self, input_texts):
        if isinstance(input_texts, list):
            if not all(isinstance(t, str) for t in input_texts):
                raise ValueError("All elements in input_texts list must be strings.")
            user_prompt = "\n".join(input_texts)
        elif isinstance(input_texts, str):
            user_prompt = input_texts
        else:
            raise TypeError("input_texts must be a string or a list of strings.")

        system_message = self.generate_system_message()

        res = self.co.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt},
            ],
        )
        return res