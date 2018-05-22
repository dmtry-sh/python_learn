class Bag:
    count = 0
    end = 10

    def pack(self, obj):
        self.count += 1
        if self.count > self.end:
            try:
                raise ValueError('Больше не влезет!')
            except ValueError as err:
                print('Ошибка: ', err)

class Packet:
    count = 0
    end = 5

    def pack(self, obj):
        self.count += 1
        if self.count > self.end:
            try:
                raise ValueError('Больше не влезет!')
            except ValueError as err:
                print('Ошибка: ', err)

         
class Thing:
    pass

bag = Bag()
p = Packet()
t1 = Thing()
t2 = Thing()
t3 = Thing()
t4 = Thing()
t5 = Thing()
t6 = Thing()
p.pack(t1)
p.pack(t2)
p.pack(t3)
p.pack(t4)
p.pack(t5)
p.pack(t6)


    
        
