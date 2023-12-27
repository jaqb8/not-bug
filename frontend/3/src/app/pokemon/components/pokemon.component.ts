import { Component } from '@angular/core';
import { PokemonService } from '../services/pokemon.service';
import { Pokemon } from '../pokemon';
import { NgFor } from '@angular/common';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-pokemon',
  standalone: true,
  imports: [NgFor, RouterLink, RouterOutlet],
  templateUrl: './pokemon.component.html',
  providers: [PokemonService],
})
export class PokemonComponent {
  pokemons: Pokemon[] = [];

  constructor(private pokemonService: PokemonService) {}

  ngOnInit() {
    this.pokemonService.getPokemons().subscribe((pokemons) => {
      this.pokemons = pokemons;
    });
  }
}
