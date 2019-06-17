

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    var area, perimeter;
    const PI = Math.PI;
    const radius = Number(readLine());

    // Print the area of the circle:
    area = PI * (Math.pow(radius, 2));
    console.log(area);
    // Print the perimeter of the circle:
    perimeter = 2 * PI * radius;
    console.log(perimeter);

}
