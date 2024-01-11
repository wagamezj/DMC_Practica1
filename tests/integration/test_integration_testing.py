import pytest
from text_processing.text_preprocessor import  TextPreprocessor 

    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])

def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = TextPreprocessor().remove_numbers(TextPreprocessor().remove_users(input_text))
    assert processed_text == expected_output

######################## Codigo para practica 1 test de integracion ###################################################################
    

@pytest.mark.parametrize("text, expected", [
(["was", "happier", "understanding"], 'wa happier understand' ),
(["beautiful", "quickly", "management"], 'beauti quickli manag'),
(["written", "children", "gonna"], 'written child gonna'),
(["dogs", "playing", "run"], 'dog play run'),])
   
def test_integration_lem_stem(text, expected):
    processed_text = TextPreprocessor().lemmatization_activate(text) 
    processed_text2 = TextPreprocessor().stemming_activate(processed_text.split())
    assert processed_text2 == expected


