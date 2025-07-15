# Reddit Persona Extractor

This project extracts Reddit user posts and comments, then generates a personality summary using an LLM (Cohere API). The extracted texts and generated persona are saved to files.

---

## 🚀 Getting Started

### 1. Clone the Repository
bash commands - 
git clone <repo_url>
cd <repo_folder>

### 2. Create a virtual environment in the base directory
python3 -m venv venv (MacOS, Linux)
python -m venc venv (windows)

### 3. Activate the virtual environment
source venv/bin/activate (MacOS, Linux)
venv\Scripts\activate.bat (Windows CMD)
venv\Scripts\Activate.ps1 (Windows powershell)

### 4. Install dependencies for the Cohere LLM as well as extracting data from reddit page
pip install -r requirements.txt

### 5. Create a reddit app for credentials (https://www.reddit.com/prefs/apps) and create a free tier API_KEY for using the Cohere LLMs ("https://dashboard.cohere.com/welcome/login")

### 6. Create config files
Create a folder named config in the base directory. Inside this create a config.yaml file to store the environment variables.
the format for the yaml file is- (All the credentials are found in the created reddit app)

reddit:
  client_id: "<CLIENT_ID>"
  client_secret: "<CLIENT_SECRET>"
  user_agent: "scraper by /u/<USERNAME>"
  username: "<YOUR_USERNAME>"
  password: "<YOUR_PASSWORD>"

llm:
  cohere_api_key: "<COHERE_API_KEY>"

  

### 7. Run the main script
python src/main.py --url <reddit_profile_url>
(replace <reddit_profile_url> with the required URL)

The output for each user will be found in text files in the base directory
"USERNAME_texts.txt" and "USERNAME_persona.txt"
