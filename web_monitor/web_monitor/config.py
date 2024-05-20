# Configuration parameters for the web monitoring project
CHECK_INTERVAL = 3600  # Time interval between checks in seconds (e.g., 3600 seconds = 1 hour)

# ChatGPT configuration
CHATGPT_ENGINE = "gpt-3.5-turbo"
CHATGPT_PROMPT_TEMPLATE = "Faites une synthèse des modifications suivantes :\n\n{content}"
CHATGPT_MAX_TOKENS = 500
CHATGPT_TEMPERATURE = 0.5