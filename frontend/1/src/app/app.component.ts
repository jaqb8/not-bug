import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterOutlet } from '@angular/router';
import { CarListComponent, AddCarFormComponent } from './cars/components';
import { CarService } from './cars/services/car.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    RouterOutlet,
    RouterLink,
    AddCarFormComponent,
    CarListComponent,
  ],
  templateUrl: './app.component.html',
  providers: [CarService],
})
export class AppComponent {
  title = 'Car App';
}
