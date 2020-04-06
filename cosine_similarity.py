import re, math
from collections import Counter
import numpy as np
import pandas as pd
import operator
import json


class CosineSimilarity:
    def __init__(self):
        print("init")

    @staticmethod
    # Take in two strings text1/2
    def cosine_similarity_calculation(text1, text2):
        # Using Regex, \w matches any word character
        first = re.compile(r"[\w']+").findall(text1)
        second = re.compile(r"[\w']+").findall(text2)
        # Initialize dictionaries with Counter.
        vector1 = Counter(first)
        vector2 = Counter(second)
        # Keys correspond to a word
        common = set(vector1.keys()).intersection(set(vector2.keys()))
        # dot_product computes the dot product multiplication of two vectors
        dot_product = 0.0
        # Finding common words that are in both vector1 and vector2
        for i in common:
            dot_product += vector1[i] * vector2[i]
        #init square sum vectors
        ssv1 = 0.0
        ssv2 = 0.0
        # Calculating cosine similarity
        # Following the formula for cosine similarity calculation
        for i in vector1.keys():
            ssv1 += vector1[i] ** 2

        for i in vector2.keys():
            ssv2 += vector2[i] ** 2

        magnitude = math.sqrt(ssv1)        *math.sqrt(ssv2)

        if not magnitude:
            return 0.0
        else:
            return float(dot_product) / magnitude