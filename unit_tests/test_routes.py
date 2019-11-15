def test_home(selenium):
    selenium.get('http://127.0.0.1:5000')
    assert "Luca Melis" in selenium.title
