import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { retry, throwError, catchError, Observable, map } from 'rxjs';
import { Pokemon, PokemonDetails } from '../pokemon';

@Injectable({
  providedIn: 'root',
})
export class PokemonService {
  apiUrl = 'https://pokeapi.co/api/v2/pokemon/';

  constructor(private http: HttpClient) {}

  getPokemons(): Observable<Pokemon[]> {
    return this.http.get<{ results: Pokemon[] }>(this.apiUrl).pipe(
      map((data) => data.results),
      retry(3),
      catchError(this.handleError)
    );
  }

  getPokemonByName(name: string): Observable<PokemonDetails> {
    return this.http
      .get<PokemonDetails>(this.apiUrl + name)
      .pipe(retry(3), catchError(this.handleError));
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      console.error('An error occurred:', error.error);
    } else {
      console.error(
        `Backend returned code ${error.status}, body was: `,
        error.error
      );
    }
    return throwError(
      () => new Error('Something bad happened; please try again later.')
    );
  }
}
