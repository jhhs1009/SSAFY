const products = [
    {name : 'cucumber', type: 'vegetable'},
    {name : 'banana', type:'fruit'},
    {name:'carrot', type:'vegetable'},
    {name:'apple', type:'fruit'},
]

const fruitFilter = function (product) {
    return product.type === 'fruit'
}

const fruits = products.filter(fruitFilter)
console.log(fruits)

//결과
// [ { name: 'banana', type: 'fruit' }, { name: 'apple', type: 'fruit' } ]