import { Injectable } from '@angular/core';
import { Car } from '../models/car.model';
import { BrowserStorageService } from '../../storage.service';
import { v4 as uuidv4 } from 'uuid';
import { AddCarDto } from '../dto/add-car.dto';

const CARS_KEY = 'cars';

@Injectable({
  providedIn: 'root',
})
export class CarService {
  private cars: Car[] = [];

  constructor(private storageService: BrowserStorageService) {
    const storedCars = this.storageService.get(CARS_KEY);
    if (storedCars) {
      this.cars = JSON.parse(storedCars);
    }
  }

  getCars(): Car[] {
    return this.cars;
  }

  getCar(id: string): Car | undefined {
    return this.cars.find((c) => c.id === id);
  }

  addCar(addCarDto: AddCarDto): Car {
    const id = uuidv4();
    const { brand, model, year } = addCarDto;
    const newCar: Car = { id, brand, model, year, services: [] };
    this.cars.push(newCar);
    this.saveCarsToLocalStorage();
    return newCar;
  }

  updateCar(carId: string, car: Car): Car | undefined {
    const index = this.cars.findIndex((c) => c.id === carId);
    if (index === -1) {
      return;
    }
    this.cars[index] = car;
    this.saveCarsToLocalStorage();
    return this.cars[index];
  }

  deleteCar(id: string): void {
    const index = this.cars.findIndex((c) => c.id === id);
    if (index !== -1) {
      this.cars.splice(index, 1);
      this.saveCarsToLocalStorage();
    }
  }

  deleteAllCars(): void {
    this.cars = [];
    this.clearCarsFromLocalStorage();
  }

  private saveCarsToLocalStorage(): void {
    this.storageService.set(CARS_KEY, JSON.stringify(this.cars));
  }

  private clearCarsFromLocalStorage(): void {
    this.storageService.remove(CARS_KEY);
  }
}
