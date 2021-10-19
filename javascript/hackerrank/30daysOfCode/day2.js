/**
 * this was my solution : 
 * Day 2: Operators
 */

function solve(meal_cost, tip_percent, tax_percent) {
    // Write your code here
    const tip_result = Math.round(tip_percent/100 * meal_cost)
    const tax_result = Math.round(tax_percent/100 * meal_cost)
    const meal_cost_after_tax = parseInt(meal_cost + tip_result + tax_result)
    console.log(meal_cost_after_tax)
    return meal_cost_after_tax
}