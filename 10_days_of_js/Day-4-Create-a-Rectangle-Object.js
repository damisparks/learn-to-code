/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    this.length = a;
    this.width = b; 
    this.area = rec_area(a, b); 
    this.perimeter = rec_perimeter(a, b);

    function rec_area(a, b) {
        return (a * b);
    }

    function rec_perimeter(a, b) {
        return (2 * (a + b));
    }
}