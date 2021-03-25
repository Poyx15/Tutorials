# message = input (">")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "🙁",
#     "8)": "😎",
#     "JOKER": "🤡"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "🙁",
        "8)": "😎",
        "JOKER": "🤡"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input (">")
print(emoji_converter(message))