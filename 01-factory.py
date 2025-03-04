import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.region_spec} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.region_spec} Spec): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


def main():
    # Використання
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Ducati", "Panigale")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()