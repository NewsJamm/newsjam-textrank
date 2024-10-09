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

def find_recommand_news_vectors(faiss_index, recommend_count):
    # 입력받은 FAISS 인덱스에 해당하는 벡터 가져오기
    input_vector = index.reconstruct(faiss_index).reshape(1, -1)

    # 입력된 벡터와 가까운 이웃을 검색 (k개의 가장 가까운 벡터)
    distances, indices = index.search(input_vector, recommend_count)

    # 가까운 이웃의 인덱스와 거리 반환
    return indices[0], distances[0]
