// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
    let dayName;
    // Write your code here
    const THE_DATE = new Date(dateString);
    /*
    Read this documentation to understand the conversion into days in the week.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay
    */
    var options = { weekday: 'long' };
    dayName = Intl.DateTimeFormat('en-Us', options).format(THE_DATE);
    return dayName;
}

