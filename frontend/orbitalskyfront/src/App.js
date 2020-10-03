import React from "react";
// import { Link } from "react-router-dom";
import Stars from "./Stars/Stars";
import "./App.scss";

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Link to="/NewRoute">Ir para Nova Rota</Link>
        </a>
      </header> */}
      <Stars />
    </div>
  );
}

export default App;
