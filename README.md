# algorithms_lab_05
An algorithm for a lab task

## Електрики
Ваша компанія проводить електро-мережу в село Вільшанка. Умовою тендеру було
залучення місцевих майстрів, і Вам довелось на це погодитись. Майстри ці своєрідні, і
в результаті вам поставили/закопали N стовпів/електроопор, які знаходяться на
відстані w одна від одної. Проблема у тому, що точна висота кожної опори невідома -
ви тільки знаєте, що висота опори i знаходиться у межах [1, heights[i]], і приєднати
дріт ви можете тільки до вершини опори (там вже встановлене необхідне обладнання).
Електро-дріт для з’єднання стовпів ви замовляєте з Китаю, і він буде дооовго
їхати/пливти. Ви не знаєте, скільки саме дроту потрібно (це залежить від конкретних
висот опор), тому хочете замовити рівно стільки, скільки треба буде для найгіршої
ситуації.
(Іншими словами - потрібно знайти таку послідовність висот опор, що дріт, який з’єднує
їхні вершини, буде найдовшим)

## Вхідні дані:
Перший рядок містить w - відстань між опорами. Другий рядок містить N чисел,
що опиисують максимальну можливу висоту для кожної опори (тобто це масив
heights).

## Вихідні дані:
Максимально можлива необхідна довжина дроту з точністю до 2 знаків після
коми.

## Обмеження:
w, heights[i] - цілі числа у діапазоні 1 … 100
N &lt; 50
Звісно, ви повинні ігнорувати різні фізичні обмеження аля просідання дроту чи
витрати дроту на з’єднання
