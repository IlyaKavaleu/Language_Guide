from django.shortcuts import render, redirect
from paid_card.models import PaidCard
from paid_lessons.models import PaidLesson


def add_to_paid_card(request, paid_lesson_id):
    paid_lesson = PaidLesson.objects.get(id=paid_lesson_id)
    cart = PaidCard.objects.create(user=request.user, paid_lesson=paid_lesson)
    cart.save()
    return redirect('paid_lessons:all_paid_lessons')


def delete_paid_card(request, paid_card_id):
    paid_lesson = PaidCard.objects.get(id=paid_card_id)
    paid_lesson.delete()
    return redirect('users:paid_card_and_free_basket')
