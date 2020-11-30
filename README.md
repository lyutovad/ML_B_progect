## Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy API: flask 

Данные: <https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009>

### Задача: предсказать по химическому составу, является вино качественным или нет (поле quality). Бинарная классификация

Используемые признаки:

- sulphates - [0.33, 2]
- free sulfur dioxide - [1, 72]
- total sulfur dioxide - [6, 289]
- pH - [2.74, 4.01]

Модель: XGBoost


### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/lyutovad/ml_b_project
$ cd ml_b_project
$ docker build -t lyutovad/ml_b_project .
```

### Запускаем контейнер

```
$ docker run -d -p 8180:8180 -p 8181:8181 lyutovad/ml_b_project
```

### Переходим на localhost:8181
