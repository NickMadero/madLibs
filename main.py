from random import randint
import copy

story = (
        "On a random day my {} and i decided to go to the beach and was a {} kind of day\n" +
        "we got to the beach and we saw {} waves\n" +
        "after spending some time in the water we got out and ate {} and drank {} it was a good day\n"
)

word_dict = {
    'person': ['dog', 'girlfriend', 'friend'],
    'adjective': ['hot', 'gloomy', 'dark', 'bright'],
    'adjective2': ['huge', 'massive', 'large', 'small'],
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
    return story.format(
        grab_word('person',local_dict),
        grab_word('adjective',local_dict),
        grab_word('adjective2',local_dict),
        grab_word('food',local_dict),
        grab_word('drink',local_dict)

    )
print("madlibs! ")
print(story_function())
