#!/bin/python

# i'm not going to comment this crap out of this b/c i don't have time, but
# here's a not-so-basic implementation you might learn from:

# {vars} are fancy string formatting - you'll see
madlib = """
the {noun_1} and the {noun_2}

- Hans Christian Anderson
ONCE upon a time there was a prince who wanted to marry a {noun_1}; but she would have to be a real {noun_1}. He {past_tense_verb} all over the world to find one, but nowhere could he get what he wanted. There were {noun_1}es enough, but it was difficult to find out whether they were real ones. There was always something about them that was not as it should be. So he came home again and was sad, for he would have liked very much to have a real {noun_1}.

One evening a terrible storm came on; there was thunder and lightning, and the rain poured down in torrents. Suddenly a knocking was heard at the city gate, and the old king went to open it.

It was a {noun_1} standing out there in front of the gate. But, good gracious! what a sight the rain and the wind had made {third_person_posessive} look. The water ran down from {third_person_posessive} hair and clothes; it ran down into the toes of {third_person_posessive} shoes and out again at the heels. And yet she said that she was a real {noun_1}.

"Well, we'll soon find that out," thought the old queen. But she said nothing, went into the bed-room, took all the bedding off the bedstead, and laid a {noun_2} on the bottom; then she took twenty mattresses and laid them on the {noun_2}, and then twenty eider-down beds on top of the mattresses.

On this the {noun_1} had to lie all night. In the morning she was asked how she had slept.

"Oh, very badly!" said she. "I have scarcely closed my eyes all night. Heaven only knows what was in the bed, but I was lying on something hard, so that I am black and blue all over my body. It's horrible!"

Now they knew that she was a real {noun_1} because she had felt the {noun_2} right through the twenty mattresses and the twenty eider-down beds.

Nobody but a real {noun_1} could be as sensitive as that.

So the prince took {third_person_posessive} for his {title}, for now he knew that he had a real {noun_1}; and the {noun_2} was put in the museum, where it may still be seen, if no one has stolen it.

There, that is a true story.

"""

def prompt_string(kind):
    return "Please give me a %s:\n" % kind

data = [
    { 'kind': 'noun', 'keyname': 'noun_1' },
    { 'kind': 'noun', 'keyname': 'noun_2' },
    { 'kind': 'past tense verb', 'keyname': 'past_tense_verb' },
    { 'kind': 'third person posessive', 'keyname': 'third_person_posessive' },
    { 'kind': 'title', 'keyname': 'title' },
]

collected_data = {}

for field in data:
    collected_data[field['keyname']] = raw_input(prompt_string(field['kind']))

print collected_data

print madlib.format(**collected_data)


