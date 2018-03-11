import os
import csv

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        try:
            self.car_type = car_type
            self.brand = brand
            self.photo_file_name = photo_file_name
            self.carrying = float(carrying)
            if not brand or not photo_file_name or not carrying or not self.get_photo_file_ext():
                raise ValueError
        except:
            raise

    def get_photo_file_ext(self):
        res = os.path.splitext(self.photo_file_name)
        return res[1]





class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand,photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except:
            raise

    def __str__(self):
        return('{4} with {0} brand, {1} photo file name, {2} carrying weight, {3} passengers'.format(self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count, self.car_type))

class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        try:
            body_whl = body_whl.split('x')
            if body_whl.__len__() != 3:
                body_whl = [0, 0, 0]
            self.body_length = float(body_whl[0])
            self.body_width = float(body_whl[1])
            self.body_height = float(body_whl[2])
        except:
            raise

    def get_body_volume(self):
        return (self.body_length * self.body_height * self.body_width)

    def __str__(self):
        return('{4} with {0} brand, {1} photo file name, {2} carrying weight, {3} volume'.format(self.brand, self.photo_file_name, self.carrying, self.get_body_volume(), self.car_type))


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        if not extra:
            raise ValueError
        self.extra = extra

    def __str__(self):
        return ('{4} with {0} brand, {1} photo file name, {2} carrying weight, {3}'.format(self.brand, self.photo_file_name, self.carrying, self.extra, self.car_type))





def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        #next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row.__len__() != 7:
                    continue
                if row[0] == 'car':
                    car_list.append(Car(row[0], row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(Truck(row[0], row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[0], row[1], row[3], row[5], row[6]))
            except:
                continue
    return car_list

cars = get_car_list('/home/goroson/Downloads/cars2.csv')
for car in cars:
    print(car.__str__())