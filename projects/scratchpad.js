/*
 * This is a JavaScript Scratchpad.
 *
 * Enter some JavaScript, then Right Click or choose from the Execute Menu:
 * 1. Run to evaluate the selected text (Ctrl+R),
 * 2. Inspect to bring up an Object Inspector on the result (Ctrl+I), or,
 * 3. Display to insert the result in a comment after the selection. (Ctrl+L)
 */

//var myBooks = {};

/*

var mango = {
color: "yellow",
shape: "round",
sweetness:8,
fruitName:"Mango",
nativeToLand:["INDIA","South America","Central America"],
showName: function(){
console.log("This is " + this.fruitName);
},
nativeto: function(){
 nativeToLand.forEach(function(eachCountry) {
    console.log("Grown in :" + eachCountry);
    });
    }

}
*/

/*

function Fruit (theColor, theSweetness, theFruitName, theNativeToLand)
{   
    this.color = theColor;
    this.sweetness = theSweetness;
    this.fruitName = theFruitName;
    this.nativeToLand = theNativeToLand;
    
    this.showName = function(){
        console.log("this is a " + this.fruitName);
        }
        
    this.nativeTo = function() {
    this.nativeToLand.forEach(function(eachCountry) {
        console.log("GRoWs in : " +eachCountry);
        });
        }
        
}


var MangoFruit = new Fruit("Yellow",8,"Mango",["INDIA","SOUTH AMERICa","Centeral America"]);

MangoFruit.showName();
MangoFruit.nativeTo();


var Orange = new Fruit("ORANGE",5,'ORANGE',["NAGPUR","JAMMU AND KASHMIR","KOSH"]);
Orange.showName();
Orange.nativeTo();

var aMango = new Fruit();

aMango.mangoOrigin = "VNS" ; //City Code

aMango.printStuff = function() { return  aMango.showName() }//"Mango is from  " + aMango.mangoOrigin; }

console.log(aMango.printStuff());
*/
// LETS prototype with JS

function Fruit() { }

Fruit.prototype.color = "Yellow";
Fruit.prototype.sweetness = 8;
Fruit.prototype.fruitName = "Generic Fruit Name";
Fruit.prototype.nativeToLand = "USA";
Fruit.prototype.showName = function(){
        console.log("this is a " + this.fruitName);
        }

Fruit.prototype.nativeTo = function() {
        console.log("GRoWs in : " + this.nativeToLand);
         }


var mangoFruit = new Fruit ();
console.log(mangoFruit.sweetness , mangoFruit.color);
mangoFruit.showName(); //
mangoFruit.nativeTo();

for (var eachItem in mangoFruit) {
console.log(eachItem);
}

























    



/*
Exception: mangoFruit is not defined
@Scratchpad/1:55
*/
/*
Exception: Ornage is not defined
@Scratchpad/1:62
*/
/*
Exception: Ornage is not defined
@Scratchpad/1:62
*/