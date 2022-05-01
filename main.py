# poz_[x] explanations available here http://www.wskazniki.gofin.pl/9,223,2373,2,przykladowe-obliczenie-wynagrodzenia-netto.html
class Worker:
    def __init__(self, name, brutto_salary):
        self._name = name
        self._poz_a = float(brutto_salary)
        self._poz_c = round(round(self._poz_a * 0.0976, 2) + round(self._poz_a * 0.015, 2) + round(self._poz_a * 0.0245, 2), 2)
        self._poz_d = self._poz_a - self._poz_c
        self._poz_e = round(self._poz_d * 0.09, 2)
        self._poz_f = round(self._poz_d * 0.0775, 2)
        self._poz_g = 111.25
        self._poz_h = int(self._poz_a - self._poz_g - self._poz_c)
        self._poz_i = round((self._poz_h * 0.18) - 46.33, 2)
        self._poz_j = int(self._poz_i - self._poz_f)
        self._poz_k = round(self._poz_a - self._poz_c - self._poz_e - self._poz_j, 2)
        self._poz_l = round(self._poz_a * 0.0976, 2) + round(self._poz_a * 0.065, 2) + round(self._poz_a * 0.0193, 2) + round(self._poz_a * 0.0245, 2) + round(self._poz_a * 0.001, 2)
        self._poz_ł = round(self._poz_a + self._poz_l, 2)

    def print_output(self):
        print(self._name, "%.2f"%self._poz_k, "%.2f"%self._poz_l, "%.2f"%self._poz_ł)

    def get_total_employer_cost(self):
        return self._poz_ł

workers_count = int( input() )

workers = []

for index in range(0, workers_count):
    worker_data = input().replace('\r', '').replace('\n', '').split(" ")

    worker = Worker(worker_data[0], worker_data[1])

    workers.append(worker)

total_cost = 0

for index in range(0, workers_count):
    worker = workers[index]

    total_cost += worker.get_total_employer_cost()

    worker.print_output()

print("%.2f"%total_cost)
