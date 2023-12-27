import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AddCarFormComponent, CarListComponent } from '../../cars/components';
import { CarService } from '../../cars/services/car.service';
import { Car } from '../../cars/models/car.model';
import { AddCarDto } from '../../cars/dto/add-car.dto';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, AddCarFormComponent, CarListComponent],
  templateUrl: './home.component.html',
  providers: [CarService],
})
export class HomeComponent {
  cars: Car[] = [];

  constructor(private carService: CarService) {}

  ngOnInit() {
    this.cars = this.carService.getCars();
  }

  addCar(car: AddCarDto) {
    this.carService.addCar(car);
    this.cars = this.carService.getCars();
  }
}
