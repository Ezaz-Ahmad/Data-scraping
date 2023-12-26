import requests
from bs4 import BeautifulSoup

def find_apple_us_subsidiaries(link):
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
              "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
              "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
              "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
              "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
              "Wisconsin", "Wyoming"]

    state_counts = {state: 0 for state in states}

    headers = {
        'User-Agent': 'Mozilla/5.0 ...',
    }
    session = requests.Session()
    session.headers.update(headers)

    try:
        response = session.get(link)
        if response.status_code != 200:
            return f"Failed to retrieve the webpage, Status code: {response.status_code}"
        soup = BeautifulSoup(response.content, 'html.parser')


        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) > 1:
                    location = cols[1].get_text(strip=True)
                    for state in states:
                        if state.lower() in location.lower():
                            state_counts[state] += 1
                            break

        return state_counts

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

link = input("Vai Link Den : ")
us_apple_subsidiaries = find_apple_us_subsidiaries(link)

for state, count in us_apple_subsidiaries.items():
    if count > 0:
        print(f"{state}: {count}")