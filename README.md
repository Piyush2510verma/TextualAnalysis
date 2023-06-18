# TextualAnalysis
This project is a Python program that reads articles from the internet and performs analysis on them to extract various metrics and sentiment scores. The program utilizes the Natural Language Toolkit (NLTK) library and the Textstat library to process and analyze the text.

Installation

1.Clone the repository to your local machine:
git clone https://github.com/your-username/news-article-analysis.git

2.Install the required dependencies. You can use pip to install the necessary packages:
pip install newspaper3k nltk textstat

NLTK also requires additional resources to be downloaded. You can download them by running the following Python code:
import nltk
nltk.download('punkt')
nltk.download('stopwords')

#Usage 
1.Open the Python file 'TextAnalysis.py' in a code editor.
2.Modify the 'urls' list to include the URLs of the news articles you want to analyze.
3.Run the program:
python TextAnalysis.py
4.The program will process each article, calculate metrics, and perform sentiment analysis.
5.The results will be saved to separate text files. Each file contains the article heading, the article text, and various metrics and scores.

#Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

#Acknowledgments

The program uses the newspaper3k library for article extraction.
It also utilizes the NLTK library for text processing and sentiment analysis.
The Textstat library is used for calculating text metrics.
Feel free to customize this README file based on your specific project needs and provide additional information as necessary.
