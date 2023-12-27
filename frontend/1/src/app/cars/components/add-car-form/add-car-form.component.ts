import { Component, EventEmitter, Output } from '@angular/core';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { AddCarDto } from '../../dto/add-car.dto';

@Component({
  selector: 'app-add-car-form',
  standalone: true,
  templateUrl: './add-car-form.component.html',
  imports: [ReactiveFormsModule],
})
export class AddCarFormComponent {
  @Output() carAdded = new EventEmitter<AddCarDto>();

  addCarForm = new FormGroup({
    brand: new FormControl('', {
      validators: [Validators.required],
      nonNullable: true,
    }),
    model: new FormControl('', {
      validators: [Validators.required],
      nonNullable: true,
    }),
    year: new FormControl('', {
      validators: [Validators.required],
      nonNullable: true,
    }),
  });

  onSubmit() {
    if (this.addCarForm.invalid) {
      return;
    }
    this.carAdded.emit(this.addCarForm.getRawValue());
  }
}
