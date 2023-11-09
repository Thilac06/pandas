import requests
from bs4 import BeautifulSoup

# Define the URL, username, and password
login_url = "https://pfm.smartcitylk.org/wp-login.php"
username = "thilacramesh@gmail.com"
password = "TAFpfm#2133"

# Create a session to handle cookies and login
with requests.Session() as session:
    # Send a GET request to the login page to get the required cookies
    login_page = session.get(login_url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(login_page.text, "html.parser")

    # Find the form data required for login
    form = soup.find("form", {"id": "loginform"})
    data = {}
    for input_tag in form.find_all("input"):
        name = input_tag.get("name")
        value = input_tag.get("value")
        data[name] = value

    # Update the form data with the username and password
    data["log"] = username
    data["pwd"] = password

    # Send a POST request to login to the website
    response = session.post(login_url, data=data)

    # Check if the login was successful (you may need to adjust this check)
    if "Dashboard" in response.text:
        # If the login was successful, you can now access pages that require authentication
        # For example, let's scrape the HTML of the dashboard page
        dashboard_url = "https://pfm.smartcitylk.org/dashboard"
        dashboard_page = session.get(dashboard_url)
        dashboard_soup = BeautifulSoup(dashboard_page.text, "html.parser")

        # Print the HTML content of the dashboard page
        print(dashboard_soup.prettify())
    else:
        print("Login failed")

# Make sure to adjust the login success check to match the actual website's behavior
