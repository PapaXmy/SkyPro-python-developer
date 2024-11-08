from typing import Optional
from project.exceptions import ItemNotFound
from project.models import Director
from project.dao.base import BaseDAO


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Режисер с порядковым номером {pk} отсутствует!')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        return self.dao.get_all(page=page)
