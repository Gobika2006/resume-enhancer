import app

def test_lambda():
    event = {}
    result = app.lambda_handler(event, None)
    assert result["statusCode"] == 200
