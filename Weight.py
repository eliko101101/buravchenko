class Weight:
    def __init__(self, m):
        self.m_c = m
        draft = round(m % 1, 2)
        self.m_c -= m % 1
        self.m_kg = draft * 100

    def __str__(self):
        return '{c} centners and {kg} kilos'.format(c=self.m_c, kg=self.m_kg)

    def __add__(self, other):
        if isinstance(other, str):
            raise TypeError
        self.m_c = self.m_c + other.m_c
        self.m_kg = self.m_kg + other.m_kg
        if self.m_kg >= 100:
            k = self.m_kg // 100
            self.m_kg -= k * 100
            self.m_c += k
        print('centners = {c}, kilos={kg}'.format(c=self.m_c, kg=self.m_kg))
        return self.m_c, self.m_kg

    def __sub__(self, other):
        self.m_c = self.m_c - other.m_c
        self.m_kg = self.m_kg - other.m_kg
        if self.m_kg >= 100:
            k = self.m_kg // 100
            self.m_kg -= k * 100
            self.m_c += k
        print('centners = {c}, kilos={kg}'.format(c=self.m_c, kg=self.m_kg))
        return self.m_c, self.m_kg

    def __mul__(self, other):
        self.m_c = self.m_c * other.m_c
        self.m_kg = self.m_kg * other.m_kg
        if self.m_kg >= 100:
            k = self.m_kg // 100
            self.m_kg -= k * 100
            self.m_c += k
        print('centners = {c}, kilos={kg}'.format(c=self.m_c, kg=self.m_kg))
        return self.m_c, self.m_kg


m1 = Weight(25.25)
m2 = Weight(75.74)
print(m1)
print(m2)
m1+m2
m1 - m2
m1*m2