import json

def get_words(tweet):
    text = tweet["text"]
    words = text.split()
    return words

def get_hashtags(words):
    hashtags = []
    for word in words:
        if word.startswith("#"):
            hashtags.append(word)
    return hashtags

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def sort_words(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

def normalize_histogram(histogram):
    max_count = histogram[0][1]
    normalized_histogram = []
    for hashtag, count in histogram:
        normalized_count = int(count * 18 / max_count)
        normalized_histogram.append((hashtag, normalized_count))
    return normalized_histogram

def draw_histogram(histogram):
    for hashtag, count in histogram:
        print(f"{hashtag} ({count:3}) {'+' * count}")

def main():
    with open("Exercícios estudo/Exercicios extra 2/twitter.json", "r") as file:
        tweets = json.load(file)

    all_words = []
    for tweet in tweets:
        words = get_words(tweet)
        all_words.extend(words)

    word_count = count_words(all_words)
    sorted_words = sort_words(word_count)

    hashtags = get_hashtags(all_words)
    hashtag_count = count_words(hashtags)
    sorted_hashtags = sort_words(hashtag_count)

    normalized_histogram = normalize_histogram(sorted_hashtags)
    draw_histogram(normalized_histogram[:10])

if __name__ == "__main__":
    main()
