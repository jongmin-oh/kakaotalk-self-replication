from kiwipiepy import Kiwi

kiwi = Kiwi()


def remove_after_last_punctuation(text: str):
    last_punc_index = max(text.rfind("."), text.rfind("?"), text.rfind("!"))
    if last_punc_index != -1:
        text = text[: last_punc_index + 1]
    return text


def remove_incomplete_sentence(text: str):
    split_sentence = kiwi.split_into_sents(text)
    split_sentence = [str(i) for i in split_sentence]
    if len(split_sentence) == 1:
        return split_sentence[0]
    else:
        return " ".join(split_sentence[:-1])
