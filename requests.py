import json
from RecommenderScripts.recommender_engine import RecommenderEngine

#Pass in keywords which will be used as comparison
def get_recommendations(keywords):
    result = RecommenderEngine.get_recommendations(keywords)
    return result
# Get the beer names
def get_top_5_beer_names(json_string):
    list = json.loads(json_string)
    result = []
    max = len(list)
    i = 0
    while i < max:
        result.append(list[i]['name'])
        i += 1

    return result

