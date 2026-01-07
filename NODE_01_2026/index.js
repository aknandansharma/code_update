console.log("This is JavaScript Revision.");

// This is Object in js.

// This is Type 1: U
let object = {
    name: "AKnandan Sharma",
    age: 24,
    class: "BCA",
    College: "GAYA College, Gaya"
}

let obj1 = new Object();
obj1.name = "Akash Sharma";
obj1.age =  "25th";
obj1.address = "Gaya, BIHAR"

function objectDetaiils(name, age) {
    this.name = name;
    this.age = age;
}

// let fak = new objectDetaiils("aknandan", 27);
// // console.table(fak)

// function Person () {};


const anu = {
    name: "Aknandan Sharma",
    walk() {
        console.log("Walking");
    }
}

const dog = Object.create(anu);

dog.bark = function() {
    console.log("Barking");
}

console.log(dog.name);
dog.walk();
dog.bark();
