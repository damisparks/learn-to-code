// the item we are looking for its discount
const itemToFind = 'iphone'

// a function that return an item
function showPrice(findItem) {

    const collectedItems = []
    function pingoDoce(findItem) {
        
        // an array of items that pingo has.
        const pingeItems = [
            {name : 'iphone',price: 1200},
            {name : 'iphone10',price: 1500},
        ]
        
        let foundItem = {}
        // loop over the {pingeItems} to compare against {findItem}
        pingeItems.forEach(item => {
            // check if findItem is present in pingeItems
            if (findItem === item.name) {    
                // console.log(item)
                foundItem = item 
                collectedItems.push(item)
            } 
        });
        console.log(collectedItems)
        return foundItem
    }
    
    // a function that return an item
    function continente(findItem) {
        
        let foundItem = {}
        // an array of items that pingo has.
        const pingeItems = [
            {name : 'iphone',price: 1800},
            {name : 'iphone10',price: 1500},
        ]
    
        // loop over the {pingeItems} to compare against {findItem}
        pingeItems.forEach(item => {
            // check if findItem is present in pingeItems
            if (findItem === item.name) {    
                // console.log(item)
                foundItem = item
                collectedItems.push(item) 
            } 
        });
        return foundItem
    }
    
    const pingoValaue = pingoDoce(itemToFind)
    console.log(pingoValaue)

    const continenteValaue = continente(itemToFind)
    console.log(continenteValaue)
}


showPrice(itemToFind)


