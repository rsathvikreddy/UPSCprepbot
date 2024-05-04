import requests

# Set your API key
API_KEY = 'b9e6238b16bc4feab12e09586b4b6eeb'

# Define the endpoint URL
url = 'https://newsapi.org/v2/top-headlines'

# Define query parameters
parameters = {
    'country': 'in',  # Country code for India
    'apiKey': API_KEY  # Your API key
}

# Make the request
response = requests.get(url, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    # Convert response to JSON
    data = response.json()
    
    # Extract and print headlines
    articles = data['articles']
    for article in articles:
        title = article['title']
        description = article['description']
        print(f'Title: {title}\nDescription: {description}\n')
else:
    print('Error fetching news:', response.status_code)
