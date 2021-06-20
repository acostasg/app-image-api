from api.dominio.repository.referencesRepositoryInterface import ReferencesRepositoryInterface
from api.dominio.entity.reference import Reference


class ReferencesRepository(ReferencesRepositoryInterface):
    def all(self) -> list:
        return Reference.query.all()
