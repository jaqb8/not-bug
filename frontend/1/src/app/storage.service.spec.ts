import { TestBed } from '@angular/core/testing';
import { BrowserStorageService } from './storage.service';

describe('StorageService', () => {
  let service: BrowserStorageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BrowserStorageService);
    service.clear();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should return a value', () => {
    service.set('foo', 'bar');
    expect(service.get('foo')).toEqual('bar');
  });

  it('should return null', () => {
    expect(service.get('foo')).toEqual(null);
  });

  it('should remove a value', () => {
    service.set('foo', 'bar');
    service.remove('foo');
    expect(service.get('foo')).toEqual(null);
  });

  it('should clear all values', () => {
    service.set('foo', 'bar');
    service.set('baz', 'qux');
    service.clear();
    expect(service.get('foo')).toEqual(null);
    expect(service.get('baz')).toEqual(null);
  });
});
