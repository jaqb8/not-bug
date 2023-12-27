import { TestBed } from '@angular/core/testing';
import { CarService } from './car.service';

describe('CarService', () => {
  let service: CarService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CarService);
    service.deleteAllCars();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should return cars', () => {
    expect(service.getCars()).toEqual([]);
  });

  it('should add a car', () => {
    const car = service.addCar({
      brand: 'Ford',
      model: 'Focus',
      year: '2019',
    });
    expect(service.getCars().length).toEqual(1);
  });

  it('should return a car', () => {
    const car = service.addCar({
      brand: 'Ford',
      model: 'Focus',
      year: '2019',
    });
    expect(service.getCar(car.id)).toEqual(car);
  });

  it('should update a car', () => {
    const car = service.addCar({
      brand: 'Ford',
      model: 'Focus',
      year: '2019',
    });
    const updatedCar = service.updateCar(car.id, {
      ...car,
      brand: 'Toyota',
    });
    expect(updatedCar?.brand).toEqual('Toyota');
  });

  it('should delete a car', () => {
    const car = service.addCar({
      brand: 'Ford',
      model: 'Focus',
      year: '2019',
    });
    service.deleteCar(car.id);
    expect(service.getCars()).toEqual([]);
  });

  it('should delete all cars', () => {
    service.addCar({
      brand: 'Ford',
      model: 'Focus',
      year: '2019',
    });
    service.addCar({
      brand: 'Toyota',
      model: 'Corolla',
      year: '2019',
    });
    service.deleteAllCars();
    expect(service.getCars()).toEqual([]);
  });
});
