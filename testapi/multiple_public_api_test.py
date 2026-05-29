import requests
import time
import logging

# Configure logging
logging.basicConfig(
    filename="api_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

apis = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://dummyjson.com/products",
    "https://reqres.in/api/users?page=2",

    # Heavy / slower APIs
    "https://pokeapi.co/api/v2/pokemon?limit=1000",
    "https://restcountries.com/v3.1/all",
    "https://api.publicapis.org/entries",
    "https://api.spacexdata.com/v4/launches",
    "https://api.openbrewerydb.org/breweries",
    "https://api.tvmaze.com/shows",
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd",
    "https://rickandmortyapi.com/api/character",
    "https://dog.ceo/api/breeds/list/all"
]

def test_response_time():
    logging.info("API Response Time Testing Started")

    for api in apis:
        print(f"\nTesting: {api}")
        logging.info(f"Testing API: {api}")

        try:
            start = time.time()
            response = requests.get(api, timeout=20)
            end = time.time()

            response_time = (end - start) * 1000

            print("Status Code:", response.status_code)
            print("Response Time:", round(response_time, 2), "ms")

            logging.info(
                f"Status Code: {response.status_code}, "
                f"Response Time: {round(response_time, 2)} ms"
            )

            if response_time > 8000:
                print("🔴 Slow API (>8000ms)")
                logging.warning(f"Slow API detected: {api}")
            else:
                print("🟢 Fast API")
                logging.info(f"Fast API: {api}")

        except Exception as e:
            print("Error:", e)
            logging.error(f"Error testing {api}: {str(e)}")

    logging.info("API Response Time Testing Completed")




test_response_time()