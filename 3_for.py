from random import randint as rnt


"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    school_99 = [{'school_class':'1a',
                  'scores': [rnt(1,5),rnt(1,5),rnt(1,5),rnt(1,5),rnt(1,5)]},
                 
                 {'school_class':'1b',
                  'scores': [rnt(1,5),rnt(1,5),rnt(1,5),rnt(1,5),rnt(1,5)]},
                 
                 {'school_class':'1c',
                  'scores': [rnt(1,5),rnt(1,5),rnt(1,5),rnt(1,5),rnt(1,5)]}
                ]
     
    
   
    sum_class_score=0
    sum_school_score=0

    for score in school_99:
        sum_class_score = sum(score['scores']) / len(score['scores'])
        sum_school_score+=sum_class_score
        print(f'Средняя оценка по классу: {sum_class_score}')
        print(f'Средняя оценка по школе: {sum_school_score}')
    
if __name__ == "__main__":
    main()
