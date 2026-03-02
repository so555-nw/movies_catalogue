import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYTE3YzQzZGZiOWQxMmE5NThmZmZjYmExNzdlZWI4MCIsIm5iZiI6MTc2OTczMTI3Mi4wNDQsInN1YiI6IjY5N2JmNGM4ZGQxNjQ5ZDNiN2Q5MDBkNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eZ_V2GH4-4OlNjeZUAMGp6XauTssRlZaNJMHWJNL3ro"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_movies_list(list_name="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    response = requests.get(endpoint, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_movies(how_many=8, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=HEADERS)
    response.raise_for_status()
    return response.json()