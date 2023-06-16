import newspaper
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from textstat import syllable_count

# List of URLs to process
urls = ['https://www.ndtv.com/india-news/move-to-rename-jawaharlal-nehru-museum-new-flashpoint-between-bjp-congress-4126816'
    ]
encoded_urls = [url.encode('utf-8') for url in urls]

# Start URL ID
url_id = 37

for url in urls:
    # Create a newspaper Article object
    article = newspaper.Article(url)
    article.download()
    article.parse()


    article_heading = article.title
    article_text = article.text

    sentences = nltk.sent_tokenize(article_text)
    words = nltk.word_tokenize(article_text)

    # Calculate the required metrics and scores
    total_sentence_length = sum(len(sentence.split()) for sentence in sentences)
    avg_sentence_length = total_sentence_length / len(sentences)

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    complex_words = [word for word in words if syllable_count(word) >= 3]
    percentage_complex_words = (len(complex_words) / len(words)) * 100

    word_count = len(words)
    sentence_count = len(sentences)
    complex_word_count = len(complex_words)
    fog_index = 0.4 * ((word_count / sentence_count) + (100 * (complex_word_count / word_count)))

    avg_words_per_sentence = len(words) / len(sentences)

    personal_pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'you', 'him', 'her', 'us', 'them']
    personal_pronoun_count = sum(1 for word in words if word.lower() in personal_pronouns)

    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / len(words)

    total_syllables = sum(syllable_count(word) for word in words)
    avg_syllables_per_word = total_syllables / len(words)


    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(article_text)
    positive_score = sentiment_scores['pos']
    negative_score = sentiment_scores['neg']
    polarity_score = sentiment_scores['compound']
    subjectivity_score = 1 - abs(polarity_score)

    # Construct the file name based on the URL ID
    file_name = str(url_id) + '.txt'
    url_id += 1

    # Save the results to a text file
    with open(file_name, 'w') as file:
        file.write(f"Article Heading: {article_heading}\n\n")
        file.write(article_text)
        file.write(f"\n\nPositive Score: {positive_score}")
        file.write(f"\nNegative Score: {negative_score}")
        file.write(f"\nPolarity Score: {polarity_score}")
        file.write(f"\nSubjectivity Score: {subjectivity_score}")
        file.write(f"\nAvg Sentence Length: {avg_sentence_length}\n")
        file.write(f"Percentage of Complex Words: {percentage_complex_words:.2f}%\n")
        file.write(f"FOG Index: {fog_index:.2f}\n")
        file.write(f"Avg Words per Sentence: {avg_words_per_sentence:.2f}\n")
        file.write(f"Complex Word Count: {complex_word_count}\n")
        file.write(f"Word Count: {word_count}\n")
        file.write(f"Avg Syllables per Word: {avg_syllables_per_word:.2f}\n")
        file.write(f"Personal Pronoun Count: {personal_pronoun_count}\n")
        file.write(f"Avg Word Length: {avg_word_length:.2f}\n")
