from django.shortcuts import render
from .models import Topic_Interview, TheoryOfTopic

# Добавь функцию отрисовывающую главную страницу категории собеседованния
def home_interview(request):
    return render(request, 'interview/home_interview.html')


# Добавь функцию темы для собеседовании, допустим алгоритмы, SCQ, джанго, pytest и т.д
def topic_interview(request, topic):
    topic_objects = Topic_Interview.objects.filter(slug=topic)
    tesks = topic_objects.select_related('practical_tasks')
    theory_topic = topic_objects.select_related('theory_topic')
    context = {
        'name_topic': topic_objects.name,
        'tesks': tesks,
        'theory': theory_topic,
    }
    return render(request, 'interview/topic_interview.html', context)
