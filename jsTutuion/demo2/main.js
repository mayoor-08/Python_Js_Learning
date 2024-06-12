


function alertme(e){
    let div = document.getElementById('box')
    const heading = document.createElement("h1")
    heading.innerHTML = "Square of numbers"
    div.appendChild(heading)
for (let i = 1; i <= 10; i++) {
  const node = document.createElement("div");
  const textnode = document.createTextNode(i*i);
  node.appendChild(textnode);
  div.appendChild(node);

}}
document.getElementById("bt").addEventListener('click', alertme)