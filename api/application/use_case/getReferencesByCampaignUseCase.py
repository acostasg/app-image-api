from injector import inject

from api.application.use_case.getReferencesByCampaignResponse import GetReferencesByCampaignResponse
from api.dominio.repository.referencesRepositoryInterface import ReferencesRepositoryInterface


class GetReferencesByCampaignUseCase:
    @inject
    def __init__(self, references_repository: ReferencesRepositoryInterface):
        self.reference_repository = references_repository

    def execute(self) -> GetReferencesByCampaignResponse:
        references = self.reference_repository.all()
        if not references:
            references = {}
        return GetReferencesByCampaignResponse(references)
