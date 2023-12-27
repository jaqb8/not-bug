import { Observable, from, of } from "rxjs";
import { map, filter, mergeMap, toArray } from "rxjs/operators";

let persons = [
  { id: 1, name: "Jan Kowalski" },
  { id: 2, name: "John Doe" },
  { id: 3, name: "Jarek Kaczka" },
];

let ages = [
  { person: 1, age: 18 },
  { person: 2, age: 24 },
  { person: 3, age: 666 },
];

let locations = [
  { person: 1, country: "Poland" },
  { person: 3, country: "Poland" },
  { person: 1, country: "USA" },
];

const locations$ = of(...locations);

const polishLocations$ = locations$.pipe(
  filter((location) => location.country === "Poland")
);

const ages$ = of(...ages);

const polishAges$ = polishLocations$.pipe(
  mergeMap((location) =>
    ages$.pipe(
      filter((age) => age.person === location.person),
      map((age) => age.age)
    )
  )
);

const polishAgesArray$ = polishAges$.pipe(toArray());

const averageAge$ = polishAgesArray$.pipe(
  map((ages) => ages.reduce((acc, age) => acc + age, 0) / ages.length)
);

averageAge$.subscribe((averageAge) => {
  console.log(`Average age of persons living in Poland: ${averageAge}`);
});
