import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors


# word2vec-ko 모델 로드
model = KeyedVectors.load_word2vec_format(fname="./src/model/output.tsv", binary=False, encoding="utf-8")


def get_weighted_vector(categorie, keywords, category_weight=1.5):
    # 카테고리 가중치를 적용하여 벡터화
    category_vectors = model[categorie] * category_weight

    keyword_vectors = [model[word[0]] for word in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:3] if word[0] in model]

    combined_vectors = category_vectors + keyword_vectors



    # 벡터가 없을 경우 0으로 반환
    if len(combined_vectors) == 0:
        return np.zeros(model.vector_size)

    avg_vector = np.mean(combined_vectors, axis=0)

    # 벡터 시각화
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(avg_vector)), avg_vector)
    plt.title('Weighted Average Vector (Categories + Keywords with Category Weight = 1.5)')
    plt.xlabel('Vector Dimension')
    plt.ylabel('Value')
    plt.show()

    return avg_vector

