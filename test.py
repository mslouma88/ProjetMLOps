from app import model_pred


new_data = {'clo' : 2,
        'lao' : 10000,
        'tbo' : 1500,
        'income' : 700,
        'ye' : 10,
        'fs' : 580,
            }

def test_predict():
    prediction = model_pred(new_data)
    assert prediction == 1, "incorrect prediction"