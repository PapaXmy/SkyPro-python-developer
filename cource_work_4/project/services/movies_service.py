from typing import Optional
from project.exceptions import ItemNotFound
from project.models import Movie
from project.dao.main import MoviesDAO


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Фильм с порядковым номером {pk} не существует!')

    def get_all(
            self, page: Optional[int] = None, status: Optional[str] = None
    ) -> list[Movie]:
        return self.dao.get_all(status=status, page=page)
