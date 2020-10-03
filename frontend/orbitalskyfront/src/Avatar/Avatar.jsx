import React, { Component } from "react";
import "./Avatar.scss";

export default class Avatar extends Component {
  constructor() {
    super();
  }

  componentDidMount() {
    window.addEventListener("load", this.valueSlider);
  }

  valueSlider() {
    let slider = document.getElementById("myRange");
    let output = document.getElementById("demo");
    output.innerHTML = slider.value;

    slider.oninput = function () {
      output.innerHTML = this.value;
    };
  }

  render() {
    return (
      <React.Fragment>
        <div class="slidecontainer">
          <input
            type="range"
            min="1"
            max="100"
            value="50"
            class="slider"
            id="myRange"
          />
          <p>
            Value: <span id="demo"></span>
          </p>
        </div>
      </React.Fragment>
    );
  }
}
