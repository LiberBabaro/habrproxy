import regex

words_regex = regex.compile('(<[^>]+?>)([^<]+)', regex.IGNORECASE)
words_6_regex = regex.compile(r'([^\p{Cyrillic}a-z_]|\A)([\p{Cyrillic}a-z]{6})([^\p{Cyrillic}a-z_]|\Z)',
                              regex.IGNORECASE)
links_regex = regex.compile(r'(href=")https?://(habrahabr.ru|habr.com/ru)([^"]*)', regex.IGNORECASE)


def replace_content(content):
    return _replace_words(_replace_links(content))


def _replace_6_char_words(data):
    return data[1] + words_6_regex.sub(r'\g<1>\g<2>™\g<3>', data[2])


def _replace_words(content):
    return words_regex.sub(_replace_6_char_words, content)


def _replace_links(content):
    return links_regex.sub(r'\g<1>http://127.0.0.1:8080\g<3>', content)
