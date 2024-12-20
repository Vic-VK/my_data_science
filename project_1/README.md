# Проект 1. Анализ резюме из HeadHunter

## Оглавление
[1. Описание проекта](#Описание-проекта)  
[2. Какой кейс решаем?](#Какой-кейс-решаем)  
[3. Краткая информация о данных](#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](#Этапы-работы-над-проектом)  
[5. Результат](#Результат)  
[6. Выводы](#Выводы)  

### Описание проекта
Некоторые соискатели работы на HeadHunter не указывает желаемую заработную плату, когда составляет своё резюме. Это обстоятельство является помехой для рекомендательной системы HeadHunter, которая подбирает соискателям список наиболее подходящих вакансий, а работодателям — список наиболее подходящих специалистов. Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе.

Целью данного проекта является предварительные преобразования данных из резюме, их очистка и исследование на предмет выявления признаков, от которых зависит ожидаемая заработная плата сотрудников.

:arrow_up:[к оглавлению](#Оглавление)

### Какой кейс решаем?
Необходимо провести предобработку данных из базы резюме, выгруженной с сайта поиска вакансий hh.ru.

**Условия соревнования**
- Каждая часть состоит из блока практических заданий, которые необходимо оформлять только в Jupyter Notebook.
- Ноутбук необходимо оформить на основе предоставленного шаблона и требований.
- Отправить свой код ментору для code-ревью.

**Метрика качества**
 Результаты оцениваются на основании выполнения требований к оформлению ноутбука:
 - Решение оформляется только в Jupyter Notebook.
 - Решение оформляется в соответствии с ноутбуком-шаблоном.
 - Каждое задание выполняется в отдельной ячейке, выделенной под задание (в шаблоне они помечены как ваш код здесь).
 - Код для каждого задания оформляется в одной-двух jupyter-ячейках (не стоит создавать множество ячеек для решения задачи, это усложняет проверку).
 - Решение должно использовать только пройденный материал: переменные, основные структуры данных (списки, словари, множества), циклы, функции, библиотеки numpy, pandas, matplotlib, seaborn, plotly. Если вы думаете, что для решения необходимо воспользоваться сторонними библиотеками или инструментами (например Excel), другими языками программирования или неизученными конструкциями, вы ошибаетесь :) Все задания решаются с помощью уже знакомых методов.
 - Код должен быть читаемым и понятным: имена переменных и функций отражают их сущность, важно избегать многострочных конструкций и условий.
 - Пользуйтесь руководством PEP 8.
 - Графики оформляются в соответствии с теми правилами, которые мы приводили в модуле по визуализации данных.
 - Обязательное требование: графики должны содержать название, отражающее их суть, и подписи осей.
 - Выводы к графикам оформляются в формате Markdown под самим графиком в отдельной ячейке (в шаблоне они помечены как ваши выводы здесь). Выводы должны быть представлены в виде небольших связанных предложений на русском языке.

**Что практикуем**
+ проведение обработки, анализа данных и оформление отчетов с помощью средств python.

:arrow_up:[к оглавлению](#Оглавление)

### Краткая информация о данных
Исходные данные из базы компании HeadHunter находятся в файле по данной [ссылке.](#https://drive.google.com/file/d/1Kb78mAWYKcYlellTGhIjPI-bCcKbGuTn/view)

:arrow_up:[к оглавлению](#Оглавление)

 ### Этапы работы над проектом
1. Базовый анализ структуры данных.

2. Преобразование данных.

3. Разведывательный анализ.

4. Очистка данных.

:arrow_up:[к оглавлению](#Оглавление)

 ### Результат
Для создания требуемой модели для компания HeadHunter были подготовлены необходимые данные.

:arrow_up:[к оглавлению](#Оглавление)

### Выводы
Ход работы и ее результаты оформлены в виде [Jupyther Notebook.](Project-1.ipynb)
Диаграммы, которые были построенные в ходе выполнения проекта и сохраненные в папке [diagrams.](diagrams) Нумерация диаграмм соответствует их нумерации в ноутбуке.

:arrow_up:[к оглавлению](#Оглавление)