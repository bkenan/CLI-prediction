from main import final_model

def test_us():
    assert list(final_model("The capital city of the United States is <mask>.")[0].values())[2] == ' Washington'

def test_uk():
    assert list(final_model("The capital city of the United Kingdom is <mask>.")[0].values())[2] == ' London'
    
    