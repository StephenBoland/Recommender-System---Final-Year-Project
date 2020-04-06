import numpy as np
import pandas as pd
from RecommenderScripts.cosine_similarity import CosineSimilarity
import operator
import json

class RecommenderEngine:
    def __init__(self):
        print("init")
    def get_recommendations(keywords):

            df = pd.read_csv('clearedDesc.csv')

            score_dict = {}

            for index, row in df.iterrows():
                score_dict[index] = CosineSimilarity.cosine_similarity_calculation(row['description'], keywords)
            #sorted descriptions of beers by score and index.
            sorted_scores = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)
            # print (sorted_scores) [testing]
            # print(keywords) [testing]

            counter = 0
            #The results dataframe will hold the returning values.
            resultDF = pd.DataFrame(columns=('id','name', 'description', 'type','score',))
            #Looping for 5 beers and then breaking.
            for i in sorted_scores:

                #using pandas iloc for integer positioning
                resultDF = resultDF.append({'id': df.iloc[i[0]]['id'],'name': df.iloc[i[0]]['name'],
                                            'description': df.iloc[i[0]]['description'],
                                            'type': df.iloc[i[0]]['type'],'score': i[1]},ignore_index=True)
                counter += 1
                print(resultDF)
                if counter >= 4:
                    break;

            json_result = json.dumps(resultDF.to_dict('records'))
            return json_result