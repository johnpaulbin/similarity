from sentence_transformers import SentenceTransformer
import numpy as np


class similar:
    def __init__(self, sentences, model="sentence-transformers/paraphrase-albert-small-v2", device="cpu"):
        self.sentenceDict = sentences
        self.model = SentenceTransformer(model, device=device)

    def similar(self, input, max=None):
        compareList = list(self.sentenceDict.keys())
        resultDict = {}
        # append input to the first element in sentences to compare from
        compareList.insert(0, input)
        # generate embeddings
        embeddings = self.model.encode(compareList, batch_size=8)
        # rank embedding arrays based off of ecludian distance
        for i in range(1, len(embeddings)):
            resultDict[i] = np.linalg.norm(embeddings[0] - embeddings[i])
        # sort arrays based off of ecludian distance then return SENTENCE: SIMILARITY
        #return {sentences[i]: resultDict[i] for i in sorted(resultDict, key=resultDict.get)}
        return [self.sentenceDict[compareList[i]] for i in sorted(resultDict, key=resultDict.get)][:max]