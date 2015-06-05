import requests


def get_doi(repo_url, access_token):
    '''Fetch doi from Zenodo, if available.

    Parameters
    ----------
    :param repo_url: string
        Url in from of 'https://github.com/[owner]/[repo] . Don't add 'www'
        in front of 'github.com'.

    :param access_token: string
        Token from zenodo

    Returns
    -------
    :return: tuple
        (doi, link to doi service)
    '''
    zenodo_url = "https://zenodo.org/api/deposit/depositions?access_token="
    response = requests.get(zenodo_url + access_token)

    try:
        response.raise_for_status()
    except requests.exception.RequestException:
        return '', ''

    content = response.json()

    for upload in content:
        try:
            print upload['metadata']['related_identifiers']
            if any(x['identifier'].startswith(repo_url)
                   for x in upload['metadata']['related_identifiers']):
                return upload['doi'], upload['doi_url']
        except KeyError:
            pass

    return '', ''
