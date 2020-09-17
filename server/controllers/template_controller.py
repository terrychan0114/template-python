import connexion
import six

from server.models.template_info import TemplateInfo  # noqa: E501
from server import util


def add_info(body):  # noqa: E501
    """Add a new info to the server

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TemplateInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_info():  # noqa: E501
    """Get the information

     # noqa: E501


    :rtype: List[TemplateInfo]
    """
    return 'do some magic!'


def get_num(number):  # noqa: E501
    """Get the information of a number

     # noqa: E501

    :param number: This is the input
    :type number: str

    :rtype: List[TemplateInfo]
    """
    return 'do some magic!'


def update_info(body):  # noqa: E501
    """Update info

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TemplateInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
