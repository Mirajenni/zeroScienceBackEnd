import React, { Component } from "react";
import "./Login.scss";

export default class Login extends Component {
  render() {
    return (
      <form onSubmit={(e) => e.preventDefault()}>
        <div className={"" + (option === 1 ? "" : option === 2 ? "" : "")}>
          <input
            id="name"
            name="email"
            type="email"
            placeholder="E-Mail"
            required
          />
        </div>
      </form>
    );
  }
}
