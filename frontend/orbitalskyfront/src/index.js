import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import NewRoute from "../src/NewRoute/NewRoute";
import { BrowserRouter, Switch, Route } from "react-router-dom";

/* Uma outra parada legal do path, é que se passarmos um Route com o path sendo um * após o último route (em nosso caso após o Route do sobre), podemos ter uma rota que representa a página 404 do nosso sistema.
<Route path='*' component={ComponenteDePagina404} /> */

ReactDOM.render(
  <BrowserRouter>
    <Switch>
      <Route path="/" exact={true} component={App} />
      <Route path="/newroute" component={NewRoute} />
    </Switch>
  </BrowserRouter>,
  document.getElementById("root")
);
