import { Routes } from '@angular/router';
import { PokemonComponent } from './pokemon/components/pokemon.component';
import { PokemonDetailsComponent } from './pokemon/components/pokemon-details.component';

export const routes: Routes = [
  {
    path: '',
    component: PokemonComponent,
    title: 'Home Page',
  },
  {
    path: 'pokemon/:name',
    component: PokemonDetailsComponent,
    title: 'Pokemon Details',
  },
];
