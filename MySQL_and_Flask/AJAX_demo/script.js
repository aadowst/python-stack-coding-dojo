// fetch(`https://pokeapi.co/api/v2/pokemon/ditto`)
// .then(resp => resp.json())
// .then (data => {
//     // console.log(data.sprites.front_default)
//     var pokiHeading = document.querySelector('.pokiHeading')
//     var pokiImg = document.querySelector('.pokiImg')

//     pokiHeading.textContent = data.name
//     pokiImg.innerHTML = `
//     <img src="${data.sprites.front_default}" alt="">
//     `
//     // using back ticks to do multiple lines
    
// })
// .catch(err => console.log(err))

// var pokiForm = document.querySelector('.pokiForm')

// pokiForm.addEventListener('submit', function(e){
//     e.preventDefault()
//     // to see what gets entered, use either method below
//     console.log(pokiForm.children[1].value);
//     let pokiName = document.querySelector('#pokiName').value

// })



var pokiForm = document.querySelector('.pokiForm')

pokiForm.addEventListener('submit', function(e){
    e.preventDefault()
    console.log("test")
    // to see what gets entered, use either method below
    // console.log(pokiForm.children[1].value);
    let pokiName = document.querySelector('#pokiName').value
    console.log(pokiName)
    let url = `https://pokeapi.co/api/v2/pokemon/${pokiName}`
    console.log(url)
    fetch(url)
    .then(resp => resp.json())
    .then (data => {
        // console.log(data.sprites.front_default)
        var pokiHeading = document.querySelector('.pokiHeading')
        var pokiImg = document.querySelector('.pokiImg')

    pokiHeading.textContent = data.name
    pokiImg.innerHTML = `
    <img src="${data.sprites.front_default}" alt="">
    `
    // using back ticks to do multiple lines
    
})
.catch(err => console.log(err))
})