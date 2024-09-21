import kss
from krwordrank.word import KRWordRank



# 단어가 최소로 나와야 하는 빈도 수
min_count = 2

# 단어의 최대 길이
max_length = 10

def extract_keywords_krwordrank(title, content):
    full_content = title + " " + content
    sentence_list = kss.split_sentences(full_content)
    print(sentence_list)
    wordrank_extractor = KRWordRank(min_count, max_length)
    keywords, rank, graph = KRWordRank.extract(self=wordrank_extractor, docs=sentence_list)

    # 키워드, 점수 출력
    print_keywords(keywords)
    return keywords


def print_keywords(keywords):
    for word, r in sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:30]:
        print('%8s:\t%.4f' % (word, r))