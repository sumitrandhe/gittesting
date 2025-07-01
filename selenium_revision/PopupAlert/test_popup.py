from check_popup import check_alert,check_popup_alert

def test_popup_alert():
    assert check_alert("alert", result_text="You successfully clicked an alert"),"Failed due to error"


def test_popup_confirm_ok():
    assert check_popup_alert("confirm", accept=True,dismiss=None,result_text="You clicked: Ok"),"Failed due to error"

def test_popup_confirm_cancel():
    assert check_popup_alert("confirm", accept=None,dismiss=True,result_text="You clicked: Cancel"),"Failed due to error"
