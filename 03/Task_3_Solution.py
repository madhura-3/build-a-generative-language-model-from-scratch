import pickle
with open("./deps/deps/word_to_vector_trsf.pkl", "rb") as pk:
    word_to_vector = pickle.load(pk)

def cosine_similarity(vec_a, vec_b):
    numerator = sum([vec_a[i] * vec_b[i] for i in range(len(vec_a))])
    denominator = (sum([vec_a[i] ** 2 for i in range(len(vec_a))]) ** 0.5 * sum([vec_b[i] ** 2 for i in range(len(vec_b))]) ** 0.5)
    return numerator / denominator

def similar_words(word="tree", top_k=10):
    return sorted(
        word_to_vector.keys(), 
        key=lambda x: -cosine_similarity(word_to_vector[x], word_to_vector[word])
    )[:top_k]

result = Answer.similar_words("tree", top_k=10)
