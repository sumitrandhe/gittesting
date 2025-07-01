import pytest
from helper_url_check import *

def test_url():
    web_url = "https://the-internet.herokuapp.com/"
    assert "herokuapp.com" in check_url_title(web_url,current_url = True),"Failed Due to url"

def test_title():
    web_url = "https://the-internet.herokuapp.com/"
    assert "The Internet" == check_url_title(web_url,title=True),"Failed Due to Title"


