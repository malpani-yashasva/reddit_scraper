import praw


class RedditCollector:
    def __init__(self, client_id, client_secret, user_agent, username, password):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password
        )

    def extract_username(self, url):
        """
        Extracts the Reddit username from a profile URL.
        """
        if "reddit.com/user/" in url:
            return url.split("reddit.com/user/")[1].split('/')[0]
        raise ValueError("Invalid Reddit user URL")

    def fetch_user_texts(self, profile_url, post_limit=20, comment_limit=20):
        """
        Fetches only the text content from a user's posts and comments.
        Returns two lists: posts and comments.
        """


        username = self.extract_username(profile_url)
        redditor = self.reddit.redditor(username)
        if not username:
            raise ValueError(f"Could not extract username from URL: {profile_url}")
        posts = []
        comments = []

        for post in redditor.submissions.new(limit=post_limit):
            if post.selftext:
                posts.append(post.selftext.strip())

        for comment in redditor.comments.new(limit=comment_limit):
            comments.append(comment.body.strip())

        return posts, comments