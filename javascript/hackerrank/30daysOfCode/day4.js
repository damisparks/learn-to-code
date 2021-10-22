/**
 * this was my solution : 
 * Day 4: Class vs. Instance
 */

function Person(initialAge){
    
    const maxAge = 30
    const young = 13
    const teenager = 18
    
    this.age
    
    if (initialAge > 0) {
        this.age = initialAge
    }
    else {
        this.age = 0;
        console.log("Age is not valid, setting age to 0.");
    }
      
  this.amIOld=function(){
   // Do some computations in here and print out the correct statement to the console
   
   if(this.age < young){
       console.log('You are young.')
   }
   
   else if(this.age < teenager){
       console.log('You are a teenager.')
   } 
   else {
       console.log('You are old.')
   }

  };
   this.yearPasses=function(){
          // Increment the age of the person in here
          this.age ++
   };
}