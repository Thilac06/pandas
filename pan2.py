import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


login_url = "https://pfm.smartcitylk.org/wp-login.php"
username = "thilacramesh@gmail.com"
password = "TAFpfm#2133"


session = requests.Session()


login_data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
}
login_response = session.post(login_url, data=login_data)


if "Dashboard" in login_response.text:
    print("Login successful")
    target_url = "https://pfm.smartcitylk.org/wp-admin/admin.php?page=actual+"
    target_response = session.get(target_url)
    soup = BeautifulSoup(target_response.text, "html.parser")
    tables = soup.find_all("table")
    
    for i, table in enumerate(tables):
        table_data = []
        for row in table.find_all("tr"):
            cellsc = row.find_all("td")
            row_data = [cell.get_text(strip=True) for cell in cellsc]
            table_data.append(row_data)

        table_headers = table_data[0]
        table_data = table_data[1:] 

        print(f"Table {i + 1}:")
        table_style = "fancy_grid"  
        headers = "keys"  
        numalign = "center"  
        stralign = "left"  
        tablefmt = table_style
        print(tabulate(table_data, headers=table_headers, tablefmt=tablefmt, numalign=numalign, stralign=stralign))
else:
    print("Login failed")


session.close()
