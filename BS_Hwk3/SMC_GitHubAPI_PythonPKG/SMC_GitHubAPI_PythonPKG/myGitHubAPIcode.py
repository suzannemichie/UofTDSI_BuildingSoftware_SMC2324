import requests
from pprint import pprint
from google.colab import userdata

def get_repo_data() -> dict:
    """ Get the repository data object from GitHub.

    Connect to the GitHub API and retrieve the repository data as Python dictionary.
    The token is retrieved from the colab userdata system.

    Returns
    -------
    repository retrieved from GitHub

    Examples
    --------
    repo_data = get_repo_data()
    pprint(repo_data)
    """

    # initialize request parameters
    first_api = 'https://abcdefghijklmnopqrstuvwxyz.com'
    second_api = 'https://api.github.com/search/repositories?q=stars:>10000&fork:>100&sort=stars&per_page=1'

    # Get token after initializing API URLs
    token = userdata.get('ghtoken')

    # Validate the token (example: check if it's not empty)
    if not token:
        print('Error: Invalid token. Please provide a valid GitHub token.')
        return

    headers = {'Authorization': 'Bearer ' + token}

    try:
        # get response from first API
        response = requests.get(url=first_api + '/user', headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        print('Success from first API')
    except requests.exceptions.RequestException as e:
        print(f'Error with 1st API: {e}')
        # connection error to first API, let's try backup
        try:
            response = requests.get(url=second_api + '/user', headers=headers)
            response.raise_for_status()  # Check for HTTP errors
            print('Success from 2nd API')
        except requests.exceptions.RequestException as e:
            print(f'Error with 2nd API: {e}')
            # Handle the error or raise it again if needed

    # parse json
    return response.json()

# Example usage
try:
    repo_data = get_repo_data()
    pprint(repo_data)
except Exception as e:
    print(f'An error occurred: {e}')