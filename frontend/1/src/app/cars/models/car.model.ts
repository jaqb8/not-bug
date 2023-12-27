import { ServiceRecord } from './service-record.model';

export interface Car {
  id: string;
  brand: string;
  model: string;
  year: string;
  services: ServiceRecord[];
}
