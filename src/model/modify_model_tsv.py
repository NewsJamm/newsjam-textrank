import pandas as pd

# 변환할 Word2Vec 모델 tsv 경로
file_path = './ko.tsv'

df = pd.read_csv(file_path, sep='\t', header=None, low_memory=False)


df.head()

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

processed_data = []
current_word = None
current_vector = []
collecting_vector = False

for line in lines:
    parts = line.strip().split('\t')

    if len(parts) > 1 and parts[0].isdigit():
        if current_word is not None:
            processed_data.append(f"{current_word} {' '.join(current_vector)}")

        current_word = parts[1].strip()
        current_vector = []
        vector_part = parts[2].replace('[', '').replace(']', '').strip()
        current_vector.extend(vector_part.split())
        collecting_vector = True
    elif collecting_vector:
        vector_part = line.replace('[', '').replace(']', '').strip()
        current_vector.extend(vector_part.split())
        if ']' in line:
            collecting_vector = False

if current_word is not None:
    processed_data.append(f"{current_word} {' '.join(current_vector)}")

# 에상 벡터 크기
correct_vector_size = 200
error_lines = []

for i, line in enumerate(processed_data):
    parts = line.split()
    word = parts[0]
    vector = parts[1:]

    if len(vector) != correct_vector_size:
        error_lines.append((i + 1, word, len(vector)))  # (줄 번호, 단어, 벡터 길이)

# 예상 벡터 크기가 아닌 경우 오류 출력
if error_lines:
    print("Error: The following vectors do not have the correct dimension (200):")
    for line_num, word, size in error_lines:
        print(f"Line {line_num}: Word '{word}' has {size} dimensions instead of 200.")
else:
    vocab_size = len(processed_data)
    metadata = f"{vocab_size} {correct_vector_size}"

    # 변환된 파일 경로
    output_file = './output.tsv'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(metadata + '\n')
        for line in processed_data:
            f.write(line + '\n')

    print(f"File saved successfully: {output_file}")
