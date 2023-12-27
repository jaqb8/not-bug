import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterOutlet } from '@angular/router';
import { PokemonComponent } from './pokemon/components/pokemon.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, PokemonComponent, RouterLink],
  templateUrl: './app.component.html',
})
export class AppComponent {
  title = 'Pokemon App';
}
