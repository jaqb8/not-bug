import { Routes } from '@angular/router';
import { CarDetailsComponent } from './cars/components/car-details/car-details.component';
import { HomeComponent } from './home/components/home.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    title: 'Home Page',
  },
  {
    path: 'car/:id',
    component: CarDetailsComponent,
    title: 'Car Details',
  },
];
