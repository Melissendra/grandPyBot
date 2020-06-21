class CreateElement{
    constructor(el, props, container, text) {
        this.el = el;
        this.props = props;
        this.container = container;
        this.text= text; 
    }

    createElement(){
        const element = document.createElement(this.el);
        for(let val in this.props){
            element.setAttribute(val, this.props[val]);
        }
        element.textContent = this.text;
        this.container.appendChild(element);
        return element;
    }

    newElement(){
        return this.createElement();
    }
}