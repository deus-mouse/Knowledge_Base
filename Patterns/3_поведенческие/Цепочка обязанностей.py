'''
Этот шаблон предлагает удобный способ обработать запрос с использованием нескольких различных методов. Каждый из них может обращаться к определенной части запроса.

Как известно, одним из лучших принципов хорошего кода является принцип единой ответственности. Каждая часть кода должна делать одно, и только одно. Как раз этим и занимается Цепочка обязанностей.

Например, если необходимо отфильтровать некоторый контент, можно создать различные фильтры. Каждый из них реализует один точный и четко определенный тип фильтрации, например, нецензурную лексику или рекламу.
'''

class ContentFilter(object):
    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content

filter = ContentFilter([
                offensive_filter,
                ads_filter,
                porno_video_filter])
filtered_content = filter.filter(content)
