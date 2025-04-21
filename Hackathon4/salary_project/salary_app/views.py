from django.shortcuts import render
import random
 
 
def salary_form(request):
    return render(request, 'salary_form.html')
 
def salary_result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        company = request.POST.get('company')
        gross_salary = float(request.POST.get('gross_salary'))
        tax_percent = float(request.POST.get('tax'))
        bonus_percent = float(request.POST.get('bonus'))
 
        tax_amount = gross_salary * (tax_percent / 100)
        bonus_amount = gross_salary * (bonus_percent / 100)
        net_salary = gross_salary - tax_amount + bonus_amount
 
        context = {
            'name': name,
            'net_salary': round(net_salary, 2)
        }
        return render(request, 'salary_result.html', context)
    return render(request, 'salary_form.html')
 
def jumble_word(request):
    jumbled = None
    original = None
 
    if request.method == 'POST':
        original = request.POST.get('word')
        if original:
            word_list = list(original)
            random.shuffle(word_list)
            jumbled = ''.join(word_list)
 
    return render(request, 'jumble_word.html', {
        'original': original,
        'jumbled': jumbled
    })
