import base64
import json
import requests
import sys


def get_readme(owner, repo):
    repo_name = owner + '/' + repo
    url = 'https://api.github.com/repos/' + repo_name + '/readme'

    r = requests.get(url)
    try:
        r.raise_for_status()
        j = r.json()
    except requests.exception.RequestException:
        return ""

    return base64.decodestring(j[u'content'])


def get_contact_for_user(owner):
    url = 'https://api.github.com/users/' + owner

    r = requests.get(url)
    try:
        r.raise_for_status()
        j = r.json()
    except requests.exception.RequestException:
        return ""

    return j['email']


def get_contact_for_org(owner, repo_info):

    if not repo_info['has_issues']:
        contact = 'https://github.com/' + owner + '/' + repo + '/issues'
        return contact
    else:
        import re

        EMAIL_REGEX = re.compile('[^@\s]+@[^@\s]+\.[^@\s]+')
        first_email = EMAIL_REGEX.search(get_readme(owner, repo))

        if first_email:
            return first_email.string[first_email.start():first_email.end()]
        else:
            return ""


def get_contact(owner, repo_info):
    user_contact = get_contact_for_user(owner)
    if user_contact:
        return user_contact
    return get_contact_for_org(owner, repo_info)