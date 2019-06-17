/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    let my_count = 0;
    /* this is another way to do !
    objects.forEach(function (value) {
        if (value.x == value.y) {
            my_count++;
        }
    });
    return my_count;
    */
    objects.forEach((value) => {
        if (value.x == value.y) {
            my_count++;
        }
    });
    return my_count++;
}