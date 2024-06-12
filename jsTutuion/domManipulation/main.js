
let fruits = ["apple", "banana", "orange", "mango"]

const ul = document.getElementById("fruit-list");
   

function addFruits(){
    
    if (!ul.hasChildNodes()){
        for(i = 0; i < fruits.length; i++){
            let li = document.createElement("li");
            li.innerHTML = fruits[i]
            ul.appendChild(li)
        }
    }
}


function rmFruits(ul){
    ul.innerHTML = ""
}

function addBgColor(ul){
    ul.style.backgroundColor = "yellow";
}

function rmBgColor(ul){
 ul.style.backgroundColor = "white";
}

let btn = document.getElementById("add-fruit")
let btnRm = document.getElementById("rm-fruit")

let btnColor = document.getElementById("add-color")
let btnRmColor = document.getElementById("remove-color")

btn.addEventListener("click", addFruits)
btnRm.addEventListener("click", ()=>rmFruits(ul))

btnColor.addEventListener("click", ()=>addBgColor(ul))
btnRmColor.addEventListener("click", ()=>rmBgColor(ul))

