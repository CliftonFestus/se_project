import re
import long_responses as long


def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1
    # calculate the percentage of recognized words from the user message

    percentage = float(message_certainty)/float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False

            break

    if has_required_words or single_response:
        return int(percentage*100)

    else:
        return 0


def check_all_messages(message):
    highes_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highes_prob_list
        highes_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    # responses-------------------------------------------------------------------------------------------------
    response('Hey man', ['Hi', 'Whats upp', 'sup',
             'Hello', 'Hows it going', 'hey'], single_response=True)

    response('I am doing fine, sup with ya?', [
             'How', 'Are', 'you', 'doing', 'keeping', 'well', 'feeling'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

    response('Yes I like Naruto, the guy has infinite energy!', [
             'do', 'you', 'like', 'naruto'], single_response=True, required_words=['like', 'naruto'])

    best_match = max(highes_prob_list, key=highes_prob_list.get)
    # print(highes_prob_list)

    return best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print("Naruto: " + get_response(input('You: ')))
