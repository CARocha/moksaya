/*
 * This is a JavaScript Scratchpad.
 *
 * Enter some JavaScript, then Right Click or choose from the Execute Menu:
 * 1. Run to evaluate the selected text (Ctrl+R),
 * 2. Inspect to bring up an Object Inspector on the result (Ctrl+I), or,
 * 3. Display to insert the result in a comment after the selection. (Ctrl+L)
 */

//Accessing and Enumertating Properites on Objects

//var school = {schoolName:"MIT",schoolAccredited: true, schoolLocation:"Massachusetts"};


function HigherLearning() {
    this.educationLevel = "University";
    }
    
var school = new HigherLearning();

school.schoolName = "MIT";
school.schoolAccredited = true;
school.schoolLocation = "Massachusetts";
    
console.log(school.hasOwnProperty("educationLevel")); 

for (var eachItem in school){
    console.log(eachItem + "::" 
    + school[eachItem]);
    }
    
var christmasList = {mike:"Book",jason:"sweater" , chelsea:"iPAd"}
//JSON.stringify(christmasList);


//delete christmasList.mike;
console.log(JSON.stringify (christmasList,null, 4));

var christmasListStr = '{"mike":"Book","jason":"sweater","chelsea":"iPAd"}';

var christmasObject = JSON.parse(christmasListStr);


for (var people in christmasObject){
    console.log(christmasObject[people]);
    }
    


console.log(christmasObject.mike); 

//console.log(school.schoolName);
/*
undefined
*/