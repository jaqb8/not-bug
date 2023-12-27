"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const rxjs_1 = require("rxjs");
const operators_1 = require("rxjs/operators");
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
const locations$ = (0, rxjs_1.of)(...locations);
const polishLocations$ = locations$.pipe((0, operators_1.filter)((location) => location.country === "Poland"));
const ages$ = (0, rxjs_1.of)(...ages);
const polishAges$ = polishLocations$.pipe((0, operators_1.mergeMap)((location) => ages$.pipe((0, operators_1.filter)((age) => age.person === location.person), (0, operators_1.map)((age) => age.age))));
const polishAgesArray$ = polishAges$.pipe((0, operators_1.toArray)());
const averageAge$ = polishAgesArray$.pipe((0, operators_1.map)((ages) => ages.reduce((acc, age) => acc + age, 0) / ages.length));
averageAge$.subscribe((averageAge) => {
    console.log(`Average age of persons living in Poland: ${averageAge}`);
});
