class movieCatalog:
    def __init__(self)-> None:
        self.catalog: dict[str, list[str]] ={}

    def add_movie(self, director_name: str, movies: list[str])->None:
        if director_name not in self.catalog:
            self.catalog[director_name] = movies
        else:
            for movie in movies:
                if movie not in self.catalog[director_name]:
                    self.catalog[director_name].append(movie)




    
    def remove_movie(self, director_name:str, movie_name:str):
        if director_name in  self.catalog and movie_name in self.catalog:
            self.catalog[director_name].remove(movie_name)
            if not self.catalog[director_name]:
                del self.catalog[director_name]



    def list_directors(self)->list[str]:
        return list(self.catalog.keys())

    def get_movie_by_directors(self, directers_name: str) -> list[str]:
        if directers_name in self.catalog:
            return self.catalog[directers_name]
        else:
            return "Il regista non ce."
 

    def serch_movies_by_title(self, title:str):
        result: dict[str, list[str]] ={}

        for director, movies in self.catalog.items():
            matching_movies:list[str] = []
            for movie in movies:
                if movie.lower() == title.lower():
                    matching_movies.append(movie)

                if matching_movies:
                    result[director] = matching_movies
        if result:
            return result
        else:
            return "Nessun film trovato"

