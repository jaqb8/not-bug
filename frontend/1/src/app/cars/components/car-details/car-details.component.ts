import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CarService } from '../../services/car.service';
import { Car } from '../../models/car.model';
import { NgIf, NgFor, DatePipe } from '@angular/common';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { v4 as uuidv4 } from 'uuid';

@Component({
  selector: 'app-car-details',
  standalone: true,
  imports: [NgIf, NgFor, ReactiveFormsModule, DatePipe],
  templateUrl: './car-details.component.html',
})
export class CarDetailsComponent {
  car: Car;

  constructor(
    private activatedRoute: ActivatedRoute,
    private carService: CarService,
    private router: Router
  ) {
    const carId = this.activatedRoute.snapshot.params['id'];
    const foundCar = this.carService.getCar(carId);

    if (!foundCar) {
      this.router.navigate(['/']);
    }

    this.car = foundCar as Car;
  }

  get carFullName() {
    return `${this.car?.brand} ${this.car?.model}`;
  }

  addServiceForm = new FormGroup({
    parts: new FormControl('', {
      validators: [Validators.required],
      nonNullable: true,
    }),
    cost: new FormControl('', {
      validators: [Validators.required],
      nonNullable: true,
    }),
  });

  onSubmit() {
    if (this.addServiceForm.invalid) {
      return;
    }

    const service = this.addServiceForm.getRawValue();

    const updatedCar = this.carService.updateCar(this.car.id, {
      ...this.car,
      services: [
        ...this.car.services,
        {
          id: uuidv4(),
          parts: service.parts,
          cost: service.cost,
          date: new Date(),
        },
      ],
    });

    if (updatedCar) {
      this.car = updatedCar;
    }
  }
}
