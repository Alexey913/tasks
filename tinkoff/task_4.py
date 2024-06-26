# 4 задание
# Ограничение времени
# 3 секунды
# Ограничение памяти
# 4 МБ
# В одной из предыдущих задач требовалось вывести перевернутую матрицу, теперь задача усложняется:

# При этом поворот необходимо осуществлять in−place, т. е. без выделения дополнительной памяти. Для этого вместо результирующей матрицы необходимо вывести последовательность операций. За одну операцию можно обменять местами два элемента матрицы.

# Вам дана матрица ﻿
# �
# ×
# �
# n×n﻿, а так же указано, надо ли повернуть изображение по часовой ﻿
# �
# R﻿ или против часовой ﻿
# �
# L﻿ стрелки. Выведите последовательность операций, чтобы исходная матрица повернулась на ﻿
# 90
# 90﻿ градусов в указанном направлении.

# Заметьте, что необязательно переставлять элементы в том порядке, в котором происходил бы поворот, главное чтобы в результате матрица соответствовала повороту на 90 градусов. Также необязательно, чтобы количество операций было минимальным, нужно только вписаться в ограничения.

# Формат входных данных 

# Первая строка содержит одно натуральное число ﻿
# �
# n﻿ ﻿
# (
# 1
# ≤
# �
# ≤
# 1
# 0
# 3
# )
# (1≤n≤10 
# 3
#  )﻿ и указание направления поворота — символ ﻿
# �
# R﻿ или ﻿
# �
# L﻿. Следующие ﻿
# �
# n﻿ строк содержат описание матрицы, по ﻿
# �
# n﻿ целых неотрицательных чисел, не превосходящих ﻿
# 1
# 0
# 18
# 10 
# 18
#  ﻿.

# Формат выходных данных

# В первой строке выведите число ﻿
# �
# k﻿ — необходимое количество операций, при этом это число не должно превосходить ﻿
# 7
# �
# 2
# 7n 
# 2
#  ﻿. В последующих ﻿
# �
# k﻿ строках выведите по две пары чисел — координаты ﻿
# (
# �
# 1
# ,
# �
# 1
# )
# (x 
# 1
# ​
#  ,y 
# 1
# ​
#  )﻿ и ﻿
# (
# �
# 2
# ,
# �
# 2
# )
# (x 
# 2
# ​
#  ,y 
# 2
# ​
#  )﻿ ячеек, между которыми необходимо обменять элементы матрицы.

# Замечание

# Обратите внимание, что нумерация строк и столбцов матрицы ведётся с ﻿
# 0
# 0﻿, а не с ﻿
# 1
# 1﻿.

# Примеры данных
# Пример 1
# 2 L
# 0 0
# 0 1
# 2 L
# 0 0
# 0 1
# 1
# 1 1 0 1
# 1
# 1 1 0 1
# Пример 2
# 3 R
# 0 1 0
# 1 0 0
# 4 3 0
# 3 R
# 0 1 0
# 1 0 0
# 4 3 0
# 3
# 1 0 1 2
# 0 0 2 0
# 1 0 2 1
# 3
# 1 0 1 2
# 0 0 2 0
# 1 0 2 1
# Пример 3
# 1 L
# 5
# 1 L
# 5
# 0
