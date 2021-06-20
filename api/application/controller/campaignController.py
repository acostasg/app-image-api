from api.application.use_case.getReferencesByCampaignUseCase import GetReferencesByCampaignUseCase
from flask import jsonify, Blueprint
from injector import inject

campaign = Blueprint('campaignController', __name__)


@campaign.route('/references')
@inject
def references(use_case: GetReferencesByCampaignUseCase):
    response = use_case.execute()
    return json_encoder(response.get_references())


def json_encoder(items):
    dic = []
    for item in items:
        dic.append(item.dictionary())

    return jsonify(dic)
