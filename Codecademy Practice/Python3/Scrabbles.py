letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)} #combine the letter and point list
letter_to_points.update({" ": 0}) #blank letters

print(letter_to_points)

def score_word(word):
    point_total = 0
    for i in word:
        point_total = point_total + letter_to_points.get(i)
        print(i + " - " + str(letter_to_points.get(i)))
    return point_total

# word = input("Enter the word: ").upper()
# print(score_word(word))

player1 = "Emmanuel"
player2 = "Poy"
player3 = "Danya"
player4 = "Macmac"


player_to_words = {
    player1: ["BLUE", "TENNIS", "EXIT"],
    player2: ["EARTH", "EYES", "MACHINE"],
    player3: ["ERASER", "BELLY", "HUSKY"],
    player4: ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {

}

for player, points in player_to_words.items():
    player_points = 0
    print(player)
    for word in points:
        each_word = score_word(word)
        player_points = player_points + each_word
        print(word + " - " + str(each_word))

    print("Total Points: "+ str(player_points))
    player_to_points.update({player: player_points})

for x, y in player_to_points.items():
    print(x + " - " + str(y))

