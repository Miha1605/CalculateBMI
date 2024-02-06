import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # переводим в метры
        age = int(age_spinbox.get())
        gender = gender_var.get()

        # Рассчитываем BMI
        bmi = weight / (height * height)

        # Определяем категорию BMI
        if age < 18:
            category = 'Недостаточная масса тела'
        elif gender == 'male':
            if bmi < 18.5:
                category = 'Недостаточная масса тела'
            elif 18.5 <= bmi < 24.9:
                category = 'Нормальная масса тела'
            elif 25 <= bmi < 29.9:
                category = 'Избыточная масса тела (предожирение)'
            else:
                category = 'Ожирение'
        else:
            if bmi < 17.5:
                category = 'Недостаточная масса тела'
            elif 17.5 <= bmi < 24.9:
                category = 'Нормальная масса тела'
            elif 25 <= bmi < 29.9:
                category = 'Избыточная масса тела (предожирение)'
            else:
                category = 'Ожирение'

        # Определяем обозначение
        if bmi < 16:
            notation = 'Выраженный дефицит массы тела'
        elif 16 <= bmi < 17:
            notation = 'Дефицит массы тела'
        elif 17 <= bmi < 18.5:
            notation = 'Недостаточная масса тела'
        elif 18.5 <= bmi < 24.9:
            notation = 'Нормальная масса тела'
        elif 25 <= bmi < 29.9:
            notation = 'Избыточная масса тела (предожирение)'
        elif 30 <= bmi < 34.9:
            notation = 'Ожирение 1 степени'
        elif 35 <= bmi < 39.9:
            notation = 'Ожирение 2 степени'
        else:
            notation = 'Ожирение 3 степени'

        # Выводим результат на метку
        result_text = f'BMI: {bmi:.2f}\nКатегория: {category}\nОбозначение: {notation}'

        # Добавляем рекомендации
        if category == 'Недостаточная масса тела':
            result_text += '\nРекомендация: Обратитесь к врачу для консультации и разработки плана питания.'
        elif category == 'Нормальная масса тела':
            result_text += '\nРекомендация: Продолжайте поддерживать здоровый образ жизни.'
        elif category == 'Избыточная масса тела (предожирение)':
            result_text += '\nРекомендация: Постарайтесь улучшить свой образ жизни, включая более активную физическую активность и здоровое питание.'
        elif category == 'Ожирение':
            result_text += '\nРекомендация: Обратитесь к врачу для получения консультации и поддержки в управлении весом.'

        result.set(result_text)

    except ValueError:
        result.set('Введите корректные значения веса, роста и возраста')

# Создаем основное окно
root = tk.Tk()
root.title('Калькулятор BMI')

# Переменные для хранения значений веса, роста, пола, возраста и результата
weight_var = tk.StringVar()
height_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
result = tk.StringVar()

# Создаем виджеты
weight_label = ttk.Label(root, text='Вес (кг):')
weight_entry = ttk.Entry(root, textvariable=weight_var)

height_label = ttk.Label(root, text='Рост (см):')
height_entry = ttk.Entry(root, textvariable=height_var)

age_label = ttk.Label(root, text='Возраст:')
age_spinbox = ttk.Spinbox(root, from_=1, to=150, textvariable=age_var, width=5)

gender_label = ttk.Label(root, text='Пол:')
male_radiobutton = ttk.Radiobutton(root, text='Мужской', variable=gender_var, value='male')
female_radiobutton = ttk.Radiobutton(root, text='Женский', variable=gender_var, value='female')

calculate_button = ttk.Button(root, text='Рассчитать BMI', command=calculate_bmi)

result_label = ttk.Label(root, textvariable=result, wraplength=300, justify='left')

# Размещаем виджеты на экране
weight_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
height_entry.grid(row=1, column=1, padx=10, pady=10)

age_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
age_spinbox.grid(row=2, column=1, padx=10, pady=10)

gender_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
male_radiobutton.grid(row=3, column=1, padx=10, pady=5, sticky='w')
female_radiobutton.grid(row=3, column=1, padx=10, pady=5, sticky='e')

calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Запускаем основной цикл программы
root.mainloop()
