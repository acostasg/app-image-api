from api.dominio.repository.referencesRepositoryInterface import ReferencesRepositoryInterface
from api.infrastucture.repository.referencesRespository import ReferencesRepository
from api.application.use_case.getReferencesByCampaignUseCase import GetReferencesByCampaignUseCase


def configure(binder):
    binder.bind(ReferencesRepositoryInterface, to=ReferencesRepository)
    binder.bind(GetReferencesByCampaignUseCase, to=GetReferencesByCampaignUseCase)
