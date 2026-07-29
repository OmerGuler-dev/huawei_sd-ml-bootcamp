"""
scope (local ve global)
    -bir değişken nerede erişilebilir olduğunu ifade eder
    -değişken nerede tanimliysa orada geçerlidir
"""

#local , fonksiyonların içinde tanımlı olduğunda
#global, fonksiyon dışında tanımlanan değişken


x = 9 
def test():
    global x 
    x = 5 #lokal > global ,artık global x 5 oldu

test()
print(x)