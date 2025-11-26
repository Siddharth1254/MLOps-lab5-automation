from hello_world import generate_html, greet, app


def test_greet_returns_expected_message():
    """greet() should return the fixed welcome message."""
    expected = "Welcome to CI/CD 101 using GitHub Actions!"
    assert greet() == expected


def test_generate_html_includes_message():
    """generate_html(message) should place the message inside the HTML."""
    message = "Hello from tests"
    html = generate_html(message)

    # basic sanity checks
    assert "<html" in html.lower()
    assert message in html


def test_greeting_route_returns_200_and_contains_greeting():
    """The /greeting route should respond with 200 and contain the greeting text."""
    client = app.test_client()
    response = client.get("/greeting")

    assert response.status_code == 200

    body = response.data.decode("utf-8")
    assert greet() in body