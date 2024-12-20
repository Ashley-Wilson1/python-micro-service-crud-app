import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import Products from "./admin/Products";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Main from "./main/Main";

function App() {
	return (
		<div className="App">
			<Nav />

			<div className="container-fluid">
				<div className="row">
					<Menu />

					<main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
						<BrowserRouter>
							<Routes>
								<Route path="/admin/products" Component={Products} />
								<Route path="/" Component={Main} />
							</Routes>
						</BrowserRouter>
					</main>
				</div>
			</div>
		</div>
	);
}

export default App;
