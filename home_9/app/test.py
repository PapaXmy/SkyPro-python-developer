import json

def load_candidates():
    with open('candidates.json', 'r') as file:
        json_candidates = file.read()
        candidates = json.loads(json_candidates)
        return candidates

print(load_candidates()[1]['name'])