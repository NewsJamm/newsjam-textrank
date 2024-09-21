import faiss

# word2vec 모델 dimension 수
dimensions = 200

# L2 거리 기반의 인덱스 생성
index = faiss.IndexFlatL2(dimensions)

def save_vector(avg_vector):
    # 2차원 배열로 변환
    avg_vector= avg_vector.reshape(1, -1)

    index.add(avg_vector)

    return index.ntotal
