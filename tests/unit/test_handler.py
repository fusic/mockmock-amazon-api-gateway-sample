import json
import pytest

from app import app

@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "pathParameters": {
          "auth_key": "v2olQkcZGh7giUqWLVVCFXgNcrrzqpiS"
        }
    }


def test_auth(apigw_event, mocker):

    ret = app.auth(apigw_event, "")

    assert ret["statusCode"] == 200
    assert ret["body"] == "v2olQkcZGh7giUqWLVVCFXgNcrrzqpiS"
