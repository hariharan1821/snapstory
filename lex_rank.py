import PlaintextParser
import Tokenizer
import LexRankSummarizer


def sumy_method(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    #Summarize the document with 2 sentences
    summary = summarizer(parser.document, 2)
    dp = []
    for i in summary:
        lp = str(i)
        dp.append(lp)
    final_sentence = ' '.join(dp)

    return final_sentence