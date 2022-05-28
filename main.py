from random import randint
import copy

story = (
        "On a random day my " + {} + " and i decided to go to the beach and was a " + {} + " kind of day " +
        "we got to the beach and we saw " + {} + " waves" +
        "after spending some time in the water we got out and ate " + {} + " and drank " + {} + " it was a good day"
)

word_dict = {
    'person': ['dog', 'girlfriend', 'friend'],
    'adjective': ['hot', 'gloomy', 'dark', 'burning'],
    'adjective': ['huge', 'massive', 'large', 'small'],
    'food': ['hotdogs', 'burgers', 'fries'],
    'drink': ['soda', 'water', 'juice']

}

def grab_word(type,local_dict):
    words = local_dict[type]
    count = len(words)-1
    index = randint(0,count)
    return local_dict[type].pop(index)

def story_function():
    local_dict = copy.deepcopy(word_dict)
    return story.format()