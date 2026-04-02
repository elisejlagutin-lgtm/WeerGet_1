from django.db import models


# Тут модель теории о теме для подготовки к собеседования
class TheoryOfTopic(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


# Тут модель задачи для подготовки к собеседованию
class TaskInterviews(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    answer_problem = models.TextField(max_length=20)
    problem_solving = models.TextField()


# Тут модель темы для собеседования
class Topic_Interview(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.CharField(max_length=15)
    practical_tasks = models.ForeignKey(
        TaskInterviews,
        on_delete=models.CASCADE,
        null=True
    )
    theory_topic = models.ForeignKey(
        TheoryOfTopic,
        on_delete=models.CASCADE,
        null=True
    )
