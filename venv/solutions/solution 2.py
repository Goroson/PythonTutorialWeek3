import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        try:
            if not brand or not photo_file_name or not carrying:
                raise ValueError
            self.brand = brand
            self.photo_file_name = photo_file_name
            self.carrying = float(carrying)
        except:
            raise

    def get_photo_file_ext(self):
        res = os.path.splitext(self.photo_file_name)
        try:
            return res[1]
        except:
            return ''




class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand,photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except:
            raise

    def __str__(self):
        #print('car with {0} brand, {1} photo file name, {2} carrying weight, {3} passengers'.format(self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count))
        pass

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            if not body_whl or None:
                body_whl = '0x0x0'

            self.body_whl = body_whl.split('x')
            self.body_length = float(self.body_whl[0]) or 0.0
            self.body_width = float(self.body_whl[1]) or 0.0
            self.body_height = float(self.body_whl[2]) or 0.0
            del self.body_whl
        except:
            raise

    def get_body_volume(self):
        return (self.body_length * self.body_height * self.body_width)



class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        if not extra:
            raise ValueError
        self.extra = extra





def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row.__len__() != 7:
                continue
            try:
                if row[0] == 'car':
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
            except:
                continue

            print(row)

    return car_list

cars = get_car_list('/home/goroson/Downloads/csv.csv')


'''
with open('/home/goroson/Downloads/cars.csv', newline='') as f:
        dk = csv.DictReader(f, delimiter=';')
        for row in dk:
            print(row)
            if row['car_type']:
                print('naisu')

'''

