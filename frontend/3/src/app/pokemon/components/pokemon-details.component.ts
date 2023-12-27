import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PokemonService } from '../services/pokemon.service';
import { Pokemon, PokemonDetails } from '../pokemon';
import { JsonPipe, NgIf, UpperCasePipe } from '@angular/common';

@Component({
  selector: 'app-pokemon-details',
  standalone: true,
  imports: [JsonPipe, UpperCasePipe, NgIf],
  templateUrl: './pokemon-details.component.html',
})
export class PokemonDetailsComponent {
  pokemon: PokemonDetails | undefined;
  isLoading = false;

  constructor(
    private activatedRoute: ActivatedRoute,
    private pokemonService: PokemonService
  ) {}

  ngOnInit() {
    this.isLoading = true;
    const name = this.activatedRoute.snapshot.params['name'];
    this.pokemonService.getPokemonByName(name).subscribe((pokemon) => {
      this.pokemon = pokemon;
      this.isLoading = false;
    });
  }

  get abilities() {
    return this.pokemon?.abilities.map((a) => a.ability['name']).join(', ');
  }

  get stats() {
    return this.pokemon?.stats
      .map((s) => `${s.stat['name']}: ${s.base_stat}`)
      .join(', ');
  }
}
