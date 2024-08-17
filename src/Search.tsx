import React, { useState } from "react";
import axios from "axios";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import "bootstrap/dist/css/bootstrap.min.css";

interface Policy {
  policy_id: string;
  policy_details: string;
  policy_status: string;
}

interface Customer {
  customer_id: string;
  name: string;
  email: string;
  phone_number: string;
  policies: Policy[];
}

const Search: React.FC = () => {
  const [query, setQuery] = useState<string>("");
  const [searchType, setSearchType] = useState<string>("");
  const [result, setResult] = useState<Customer | null>(null);
  const [error, setError] = useState<string>("");

  const handleSearch = async () => {
    try {
      const response = await axios.get<Customer>(
        `http://localhost:8000/search/?${searchType}=${query}`
      );
      setResult(response.data);
      setError("");
    } catch (err) {
      setError("Customer not found or an error occurred.");
      setResult(null);
    }
    setSearchType("");
    setQuery("");
  };

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <div>
      <h2>Customer Policy Search</h2>
      <div>
        <div className="search-container">
          <Form.Select
            aria-label="Default select example"
            onChange={(e) => setSearchType(e.target.value)}
            value={searchType || ""}
            className="form-control"
          >
            <option value="">Select Search Type</option>
            <option value="phone_number">Phone Number</option>
            <option value="email">Email</option>
            <option value="policy_id">Policy ID</option>
          </Form.Select>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyPress}
            placeholder={`Enter ${searchType.replace("_", " ")}`}
            className="form-control"
            disabled={!searchType}
          />
        </div>
        <button
          onClick={handleSearch}
          disabled={!searchType}
          className="btn btn-primary"
        >
          Search
        </button>
        <hr />
      </div>
      {error && <p>{error}</p>}
      {result && (
        <Container>
          <h2 className="underline">Customer Details</h2>
          <div className="grid-item">
            <Row>
              <Col xs={3}>
                <strong>Name:</strong>
              </Col>
              <Col>{result.name}</Col>
            </Row>
            <Row>
              <Col xs={3}>
                <strong>Email:</strong>
              </Col>
              <Col>{result.email}</Col>
            </Row>
            <Row>
              <Col xs={3}>
                <strong>Phone Number:</strong>
              </Col>
              <Col>{result.phone_number}</Col>
            </Row>
          </div>

          <h4 style={{ textDecoration: "underline" }}>Policies</h4>
          <div className="grid-item">
            {result.policies.map((policy) => (
              <Row key={policy.policy_id} xs={"auto"}>
                <Col>
                  <strong>Policy ID:</strong>
                </Col>
                <Col>{policy.policy_id}</Col>
                <Col>
                  <strong>Details:</strong>
                </Col>
                <Col>{policy.policy_details}</Col>
                <Col>
                  <strong>Status:</strong>
                </Col>
                <Col>{policy.policy_status}</Col>
              </Row>
            ))}
          </div>
        </Container>
      )}
    </div>
  );
};

export default Search;
