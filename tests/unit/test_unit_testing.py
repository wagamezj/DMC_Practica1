import pytest
from text_processing.text_preprocessor import TextPreprocessor





@pytest.mark.parametrize("text, expected", [
    ("Hi How are you!$%&/()", "Hi How are you"),
    ("This is an example/()=?", "This is an example"),
    ("Christmas is !""#the best time of the year%&/()==)()", "Christmas is the best time of the year"),
    
])

def test_remove_characters(text, expected):
    assert TextPreprocessor().remove_characters(text) == expected

@pytest.mark.parametrize("text, expected", [
    (['I','like','playing','computer','games'], ' '.join([ 'like', 'playing', 'computer', 'games'])),
    (['hate', 'fast', 'food', 'restaurants'], ' '.join(['hate', 'fast', 'food', 'restaurants'])),
    (['The','best','book','of','all','times','is','from','kafka'], ' '.join(['best', 'book', 'times', 'kafka']))
    
])
def test_remove_stopwords(text, expected):
    assert TextPreprocessor().remove_stopwords(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("THIS IS A TEST", "this is a test"),
    ("I LIKE READING COMICS", "i like reading comics"),
    ("THE APPLE PIE IS MY FAVOURITE", "the apple pie is my favourite")
    
])
def test_convert_to_lowercase(text, expected):
    assert TextPreprocessor().convert_to_lowercase(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("🌟Just finished an amazing workout session! Feeling so energized and ready to conquer the day!💪", "Just finished an amazing workout session! Feeling so energized and ready to conquer the day!"),
    ("😞Stuck in traffic again... why does this always happen during rush hour?", "Stuck in traffic again... why does this always happen during rush hour?"),
    ("📉Disappointed with the latest company decision. Feels like a step backward instead of forward.", "Disappointed with the latest company decision. Feels like a step backward instead of forward."),
   
])
def test_remove_emojis(text, expected):
    assert TextPreprocessor().remove_emojis(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Stuck in traffic  again...  why  does  this", "Stuck in traffic again... why does this"),
    ("Just  finished  an  amazing workout  session", "Just finished an amazing workout session"),
    ("There's  nothing  like a  peaceful morning", "There's nothing like a peaceful morning"),
])
def test_remove_extra_spaces(text, expected):
    assert TextPreprocessor().remove_extra_spaces(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("123abc456def789", "abcdef"),
    ("Stuck in traffic again 123abc456def789", "Stuck in traffic again abcdef"),
    ("Disappointed with the latest company decision. Feels 12343", "Disappointed with the latest company decision. Feels "),
    # Add more test cases here for remove_numbers
])
def test_remove_numbers(text, expected):
    assert TextPreprocessor().remove_numbers(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Just had an amazing brainstorming session with @TechInnovator21! Their innovative ideas are always inspiring. 💡🚀 #Collaboration #Innovation","Just had an amazing brainstorming session with  Their innovative ideas are always inspiring. 💡🚀 #Collaboration #Innovation"),
    ("Attended a seminar by @MarketingGuru45 today! Their insights on social media strategies were incredibly enlightening. 📱✨ #MarketingTips #LearnFromTheBest","Attended a seminar by  today! Their insights on social media strategies were incredibly enlightening. 📱✨ #MarketingTips #LearnFromTheBest"),
    ("Had a fantastic interview with @MusicMaestro88! Their passion for music truly shines through. 🎶🎤 #MusicalGenius #InterviewInsights","Had a fantastic interview with  Their passion for music truly shines through. 🎶🎤 #MusicalGenius #InterviewInsights")
])
def test_remove_users(text, expected):
    assert TextPreprocessor().remove_users(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("Exploring new heights 🏞️ #AdventureTime #PeakViews", "Exploring new heights 🏞️  "),
    ("Baking bliss 🥖🍰 #HomeBakerJoys #OvenMagic", "Baking bliss 🥖🍰  "),
    ("Fitness journey begins! 💪🏋️ #NewGoals #HealthyHabits","Fitness journey begins! 💪🏋️  "),

])
def test_remove_hastags(text, expected):
    assert TextPreprocessor().remove_hastags(text) == expected

@pytest.mark.parametrize("text, expected", [
    ("This is a link: https://example.com", "This is a link: "),
    ("Learn how to master coding basics in no time! 💻🚀 Link: https://codinglessons.com/basics #CodingSkills #TechEducation", "Learn how to master coding basics in no time! 💻🚀 Link:  #CodingSkills #TechEducation"),
    # Add more test cases here for remove_links

])
def test_remove_links(text, expected):
    assert TextPreprocessor().remove_links(text) == expected


###################################CODIGO DE PRACTICA 1 #########################################################################

@pytest.mark.parametrize("text, expected", [
    (["dogs", "playing", "run"], ' '.join(["dog", "play", "run"])),
    (["beautiful", "quickly", "management"], ' '.join(["beauti", "quickli", "manag"])),
    
])



def test_stemming(text, expected):    
    assert TextPreprocessor().stemming_activate(text) == expected

@pytest.mark.parametrize("text, expected", [
    (["was", "happier", "understanding"], ' '.join(["wa", "happier", "understanding"])),    
    (["written", "children", "gonna"], ' '.join(["written", "child", "gonna"])),    
    
])


def test_lemmatization(text, expected):    
    assert TextPreprocessor().lemmatization_activate(text) == expected

    
    

if __name__ == "__main__":
    pytest.main()
