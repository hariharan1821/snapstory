import LuhnSummarizer


def lunh_method(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer_luhn = LuhnSummarizer()
    summary_1 = summarizer_luhn(parser.document, 2)
    dp = []


    for i in summary_1:
        lp = str(i)
    dp.append(lp)
    final_sentence = ' '.join(dp)
    return final_sentence