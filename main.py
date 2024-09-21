# from src.word_extract_rake import extract_keywords_rake, print_result
from src.word_extract_krwordrank import extract_keywords_krwordrank
from src.word_to_vector import get_weighted_vector
from src.model.save_vector import save_vector

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

if __name__ == "__main__":
    # 키워드 추출 - rake
    # keywords_result = extract_keywords(title, content)

    # 키워드 추출 - krwordrank
    keywords = extract_keywords_krwordrank(sentence_list)

    sort_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:5]

    top_keywords_word = [item[0] for item in sort_keywords]

    # 키워드와 카테고리를 이용하여 벡터화
    avg_vector = get_weighted_vector("경제", top_keywords_word)

    # vector db에 저장
    save_vector(avg_vector)



