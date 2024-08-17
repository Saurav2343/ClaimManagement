import React from "react";
import Search from "./Search";
import "./App.css";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";

const App: React.FC = () => {
  return (
    <>
      <div>
        <Navbar
          expand="lg"
          className="bg-body-primary"
          style={{ backgroundColor: " #ef1017" }}
        >
          <Container>
            <Navbar.Brand
              // href=" http://192.168.1.37:5173/"
              href="http://localhost:5173/"
              style={{ textDecoration: "underline" }}
            >
              HDFC-ERGO Claim Management
            </Navbar.Brand>
            <Navbar.Brand
              href="https://www.hdfcergo.com/"
              style={{ textDecoration: "underline" }}
            >
              HDFC-ERGO ACTUAL SITE
            </Navbar.Brand>
          </Container>
        </Navbar>
      </div>
      <div>
        <header style={{ fontFamily: "sans-serif", verticalAlign: "center" }}>
          <h1>HDFC ERGO CLAIM MANAGEMENT APP</h1>
        </header>
        <hr />
        <img
          src="https://i.ytimg.com/vi/n0p_BaTl3rY/maxresdefault.jpg"
          alt="HDFC LOGO"
          height={"50%"}
          width={"100%"}
        />
      </div>

      <main>
        <div>
          <Search />
        </div>
      </main>

      <footer>
        <div>
          {" "}
          <h2>Policies if any can be searched here.</h2>
        </div>
      </footer>
    </>
  );
};

export default App;
