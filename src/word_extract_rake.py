from rake_nltk import Rake
from konlpy.tag import Okt

# 형태소 분석기 설정
okt = Okt()

# 불용어 목록
stop_words = []

# 토크나이저 함수 정의 (명사만 추출)
def tokenize(text):
    # 명사, 동사, 형용사 등 주요 품사를 추출
    tokens = okt.pos(text, stem=True)  # 형태소 분석 결과 추출 (품사 태그 포함)

    # 품사 필터링 (명사, 동사, 형용사만 사용)
    filtered_tokens = [word for word, pos in tokens if pos in ['Noun']]

    return filtered_tokens


# Rake 객체 생성 (한국어 불용어와 토크나이저 지정)
r = Rake(
    stopwords=stop_words,
    language=None,
    sentence_tokenizer=tokenize
)


def extract_keywords_rake(title, content):
    # Rake를 이용해 키워드 추출
    r.extract_keywords_from_text(content)
    keywords_result = r.get_ranked_phrases_with_scores()
    print_result(keywords_result)
    return keywords_result


def print_result(keywords_result):
    # 결과 출력
    print("추출된 키워드:")
    for score, word in keywords_result:
        print(f"키워드: {word}, 중요도 점수: {score}")