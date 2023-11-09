import requests
from bs4 import BeautifulSoup
import openpyxl

sn = str(input("Enter the file name: "))
bn = str(input("Enter the sheet name: "))

login_url = "https://pfm.smartcitylk.org/wp-admin/admin.php?page=actual+"
username = "thilacramesh@gmail.com"
password = "TAFpfm#2133"

session = requests.Session()

login_data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
}

try:
    login_response = session.post(login_url, data=login_data)
    login_response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"An error occurred during login: {e}")
    exit(1)

if "wp-admin" in login_response.url:
    url = "https://pfm.smartcitylk.org/wp-admin/admin.php?page=annualBudget"
    response = session.get(url)

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        exit(1)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        workbook = openpyxl.Workbook()
        sheet = workbook.create_sheet(bn)

        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all(['th', 'td'])
                data = [column.get_text(strip=True) for column in columns]
                sheet.append(data)

        workbook.save(sn + ".xlsx")
        print("Success! Tables extracted and saved.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
else:
    print("Login failed. Check your credentials or the login process on the website.")
