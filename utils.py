import requests


def get_repo_info(owner, repo):
    url = 'https://api.github.com/repos/' + owner + '/' + repo

    r = requests.get(url, headers={'Accept':
                                   'application/vnd.github.drax-preview+json'})
    try:
        r.raise_for_status()
        j = r.json()
    except requests.exceptions.RequestException:
        print r.status_code
        return {}

    return j
