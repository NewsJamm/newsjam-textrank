from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# from src.word_extract_rake import extract_keywords_rake, print_result
from src.word_extract_krwordrank import extract_keywords_krwordrank
from src.word_to_vector import get_weighted_vector, model as w2v_model
from src.model.save_vector import save_vector
from typing import List, Optional

app = FastAPI(title="키워드 추출 및 벡터 저장 API")

# Pydantic 모델 정의
class SaveNewRequest(BaseModel):
    news_title: Optional[str] = ""
    news_content: str
    category: str

class ExtractKeywordReponse(BaseModel):
    word: str
    score: float

class SaveNewsResponse(BaseModel):
    vector_idx: int
    keywords: List[ExtractKeywordReponse]



# 예시 기사
title = "한국 경제 위기설, 진실은?"
content = """
최근 한국 경제가 위기라는 이야기가 곳곳에서 흘러나오고 있다.
그러나 전문가들은 상황이 그리 심각하지 않다는 입장이다.
한국 경제의 펀더멘털은 여전히 견고하다고 평가되고 있으며, 글로벌 시장의 불확실성이 경제에 미치는 영향을 주의깊게 살펴보고 있다.
"""

# 문장 분리 기능 추가하기
sentence_list = ["한국 경제 위기설, 진실은?", "최근 한국 경제가 위기라는 이야기가 곳곳에서 흘러나오고 있다.", "그러나 전문가들은 상황이 그리 심각하지 않다는 입장이다.",
                 "한국 경제의 펀더멘털은 여전히 견고하다고 평가되고 있으며, 글로벌 시장의 불확실성이 경제에 미치는 영향을 주의깊게 살펴보고 있다."]

# if __name__ == "__main__":
#     # 키워드 추출 - rake
#     # keywords_result = extract_keywords(title, content)
#
#     # 키워드 추출 - krwordrank
#     keywords = extract_keywords_krwordrank(title, content)
#
#     sort_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:5]
#
#
#     top_keywords_word = [item[0] for item in sort_keywords]
#
#     # 키워드와 카테고리를 이용하여 벡터화
#     avg_vector = get_weighted_vector("경제", top_keywords_word)
#
#     # vector db에 저장
#     save_vector(avg_vector)


@app.post("/api/news", response_model=SaveNewsResponse)
def save_news(data: SaveNewRequest):
    # 모델이 아직 로드되지 않은 경우
    if w2v_model is None:
        raise HTTPException(status_code=500, detail="모델이 로드되지 않았습니다.")

    keywords = extract_keywords_krwordrank(data.news_title, data.news_content)

    sort_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:5]

    response_keywords = [ExtractKeywordReponse(word = keyword[0], score = keyword[1]) for keyword in sort_keywords]

    top_keywords_word = [item[0] for item in sort_keywords]

    # 키워드와 카테고리를 이용하여 벡터화
    avg_vector = get_weighted_vector(data.category, top_keywords_word)

    # vector db에 저장
    vector_idx = save_vector(avg_vector)


    # 응답 객체 생성
    response = {
        "vector_idx": vector_idx,
        "keywords": response_keywords
    }

    return response






