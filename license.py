def get_license(owner, repo):

    licenses = {
      "agpl-3.0": {
        "name": "GNU Affero GPL v3.0",
        "url": "https://api.github.com/licenses/agpl-3.0"
      },
      "apache-2.0": {
        "name": "Apache License 2.0",
        "url": "https://api.github.com/licenses/apache-2.0"
      },
      "artistic-2.0": {
        "name": "Artistic License 2.0",
        "url": "https://api.github.com/licenses/artistic-2.0"
      },
      "bsd-2-clause": {
        "name": "Simplified BSD",
        "url": "https://api.github.com/licenses/bsd-2-clause"
      },
      "bsd-3-clause": {
        "name": "New BSD",
        "url": "https://api.github.com/licenses/bsd-3-clause"
      },
      "cc0": {
        "name": "CC0 1.0 Universal",
        "url": "https://api.github.com/licenses/cc0"
      },
      "epl-1.0": {
        "name": "Eclipse Public License v1.0",
        "url": "https://api.github.com/licenses/epl-1.0"
      },
      "gpl-2.0": {
        "name": "GNU GPL v2.0",
        "url": "https://api.github.com/licenses/gpl-2.0"
      },
      "gpl-3.0": {
        "name": "GNU GPL v3.0",
        "url": "https://api.github.com/licenses/gpl-3.0"
      },
      "isc": {
        "name": "ISC license",
        "url": "https://api.github.com/licenses/isc"
      },
      "lgpl-2.1": {
        "name": "GNU LGPL v2.1",
        "url": "https://api.github.com/licenses/lgpl-2.1"
      },
      "lgpl-3.0": {
        "name": "GNU LGPL v3.0",
        "url": "https://api.github.com/licenses/lgpl-3.0"
      },
      "mit": {
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit"
      },
      "mpl-2.0": {
        "name": "Mozilla Public License 2.0",
        "url": "https://api.github.com/licenses/mpl-2.0"
      },
      "unlicense": {
        "name": "Public Domain (Unlicense)",
        "url": "https://api.github.com/licenses/unlicense"
      }
    }

    # A line for request

    try:
        license = licenses[response['license']['key']]
        return license['name'], license['url']
    except KeyError:
        return '', ''
