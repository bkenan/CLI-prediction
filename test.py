from main import final_model

def test_change():
    assert list(final_model("The capital city of the United States is <mask>.")[0].values())[2] == ' Washington'
    
    