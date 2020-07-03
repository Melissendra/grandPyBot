// function to create dynamically all html tag
function createElement(el, props, container, text){
    const element = document.createElement(el);
    for(let val in props){
        element.setAttribute(val, props[val]);
    }
    element.textContent = text;
    container.appendChild(element);
    return element;
}

