

import json
from pathlib import Path


n, mean, M2 = 0, 0.0, 0
for path in Path('C:\\Users\\User\\IdeaProjects\\BigData\\IMDB.json').glob('**/*'):
    with open(path, 'r') as f:
        info = json.load(f)
        score = float(info['movieIMDbRating'])
        n += 1
        delta = score - mean
        mean += delta / n
        M2 += delta * (score - mean)

    if n != 0:
        print(mean, (M2 / n) ** (1/2))
    else:
        print("Нет данных для вычисления среднего и стандартного отклонения.")


def mapper(file_path):
    with open('C:\\Users\\User\\IdeaProjects\\BigData\\IMDB.json', 'r') as file:
        content = file.read()
        if content:  # Проверяем, что файл не пустой
            info = json.load(content)
            score = float(info['movieIMDbRating'])
            return score, 1

def reducer(mapper_results):
    scores, counts = zip(*mapper_results)
    n = sum(counts)
    mean = sum(scores * counts) / n
    M2 = sum((x - mean) ** 2 for x in scores) * counts
    return mean, M2

def print_results(n, mean, M2):
    if M2 == 0:
        print("Нет данных для вычисления стандартного отклонения.")
    else:
        std_dev = (M2 / (n - 1)) ** 0.5
        print(mean, std_dev)

n, mean, M2 = 0, 0.0, 0
for path in Path('C:\\Users\\User\\IdeaProjects\\BigData\\IMDB.json').glob('**/*'):
        mapper_result = mapper(path)
        if mapper_result:  # Проверяем, что mapper вернул результат
            n += 1
            mean += mapper_result[0] / n
            M2 += (mapper_result[0] - mean) ** 2 * 1

if n != 0:
    print_results(n, mean, M2)
else:
    print("Нет данных для вычисления среднего и стандартного отклонения.")