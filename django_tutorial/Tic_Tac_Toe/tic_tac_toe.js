let boxes = document.querySelectorAll('td')
let button = document.querySelector('button')
let wining_text = document.querySelector('#wining_text')

console.log(button)

const player_one = 'X'
const player_two = 'O'
const spaces = [null, null, null, null, null, null, null, null, null]

var current_player = player_one;

button.addEventListener('click', function(){
    console.log('clicked')
    for (let i = 0; i < 9; i++){
        boxes[i].textContent = '_'
        boxes[i].style.color = 'black'
        spaces[i] = null
        current_player = player_one
        wining_text.textContent = "Welcome to TIC-TAC-TOE"
    }
})

function updatePlayer(){
    if (current_player === player_one){
        current_player = player_two
    }else {
        current_player = player_one
    }
    return current_player
}

function win_condition(){
    if (spaces[0]===current_player){
        if(spaces[1]===current_player && spaces[2]===current_player){
            console.log(`${current_player} won!!!`)
            return true
        }
        if(spaces[3]===current_player && spaces[6]===current_player){
            console.log(`${current_player} won!!!`)
            return true
        }
        if(spaces[4]===current_player && spaces[7]===current_player){
            console.log(`${current_player} won!!!`)
            return true
        }
    }else if(spaces[8]===current_player){
        if(spaces[5]===current_player && spaces[2]===current_player){
            console.log(`${current_player} won!!!`)
            return true
        }
        if(spaces[7]===current_player && spaces[6]===current_player){
            console.log(`${current_player} won!!!`)
            return true
        }
    }else if(spaces[1] ===current_player){
        if(spaces[4]===current_player && spaces[7]===current_player){
            console.log(`${current_player} won!!!`)
            return true
        }
    }else if(spaces[3] ===current_player) {
        if (spaces[4] === current_player && spaces[5] === current_player) {
            console.log(`${current_player} won!!!`)
            return true
        }
    }else if(spaces[2] ===current_player) {
        if (spaces[4] === current_player && spaces[6] === current_player) {
            console.log(`${current_player} won!!!`)
            return true
        }
    }

}

function get_color(current_player){
    if (current_player === player_one){
        var color = 'red'
    }else {
        var color = 'blue'
    }
    return color
}

function clicks(){
    const id = this.id

    if(!spaces[id]){
        spaces[id] = current_player
        this.textContent = current_player
        this.style.color = get_color(current_player)
        if (win_condition()){
            wining_text.textContent = `_ ${current_player} _ Has WON!`
            return
        }
        current_player = updatePlayer(current_player)
    }
}

for (i = 0; i < boxes.length; i++){
    boxes[i].addEventListener('click', clicks)
}
