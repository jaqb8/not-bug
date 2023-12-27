export interface Pokemon {
  name: string;
  url: string;
}

export interface PokemonDetails {
  id: number;
  name: string;
  abilities: {
    ability: Record<string, string>;
    is_hidden: boolean;
    slot: number;
  }[];
  stats: {
    base_stat: number;
    effort: number;
    stat: Record<string, string>;
  }[];
  height: number;
  weight: number;
  base_experience: number;
  forms: Record<string, string>[];
  game_indices: Record<string, string>[];
  held_items: Record<string, string>[];
  is_default: boolean;
  location_area_encounters: string;
  moves: Record<string, string>[];
}
