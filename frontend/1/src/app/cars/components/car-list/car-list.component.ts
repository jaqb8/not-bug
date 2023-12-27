import { Component, Input } from '@angular/core';
import { Car } from '../../models/car.model';
import { NgFor } from '@angular/common';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-car-list',
  standalone: true,
  templateUrl: './car-list.component.html',
  imports: [NgFor, RouterLink, RouterOutlet],
})
export class CarListComponent {
  @Input() cars!: Car[];
}
