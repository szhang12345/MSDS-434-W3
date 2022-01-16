
import main

# Test function


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
    assert '{"greeting":"This is my MSDS434 MVP"}' in r.data.decode('utf-8')
