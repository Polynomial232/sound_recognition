"""
    docstring
"""

import json

def check_decision(status, provider):
    """
        docstring
    """

    provider = provider.lower()

    with open(f'json/decision.json', 'r', encoding='utf-8') as file:
        decision = json.loads(file.read())

    result = decision.get(status).get(provider)

    if result is None:
        result = decision.get(status).get("other")

    return result.get('tag'), result.get('status')
