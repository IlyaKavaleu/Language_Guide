from django.shortcuts import render, redirect
from paid_lessons.forms import PaidLessonForm, AddChapterForm
from paid_lessons.models import PaidLesson, PaidСhapter
from programming_guide.settings import AUTH_USER_MODEL
from users.models import User


def add_paid_lesson(request, user_id):
    if request.method != 'POST':
        form = PaidLessonForm()
    else:
        form = PaidLessonForm(data=request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user = User.objects.get(id=user_id)
            user_form.teacher = user
            user_form.save()
            return redirect('paid_lessons:list_paid_lesson', user_id=user_id)
    context = {'form': form}
    return render(request, 'paid_lessons/add_paid_lesson.html', context)


def list_paid_lesson(request, user_id):
    lessons = PaidLesson.objects.filter(teacher=user_id)
    context = {'lessons': lessons}
    return render(request, 'paid_lessons/list_paid_lesson.html', context)


def all_paid_lessons(request):
    paid_lessons = PaidLesson.objects.all()
    context = {'paid_lessons': paid_lessons}
    return render(request, 'paid_lessons/all_paid_lessons.html', context)


def show_lesson(request, lesson_id):
    chapters = PaidСhapter.objects.filter(lesson=lesson_id)
    context = {'chapters': chapters}
    return render(request, 'paid_lessons/paid_lesson.html', context)


def add_chapter(request, lesson_id):
    lesson = PaidLesson.objects.get(id=lesson_id)
    if request.method != 'POST':
        form = AddChapterForm()
    else:
        form = AddChapterForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.lesson = lesson
            form.save()
            return redirect('paid_lessons:show_lesson', lesson.id)
    context = {'lesson': lesson, 'form': form}
    return render(request, 'paid_lessons/add_chapter.html', context)

