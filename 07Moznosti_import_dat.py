# 1. možnost - zdlouhavý zápis
import data

print(data.my_data)

# 2. možnost - doporučovaná
from data import my_data

print(my_data)

# 3. možnost - moc se nepoužívá, matoucí
from data import *

# 4. možnost - alias (jiný název)
import data as d

print(d.my_data)
