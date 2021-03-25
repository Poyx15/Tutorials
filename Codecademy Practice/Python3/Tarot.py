tarot = {
    1:	"The Magician",
          2:	"The High Priestess",
          3:	"The Empress",
          4:	"The Emperor",
          5:	"The Hierophant",
          6:	"The Lovers",
          7:	"The Chariot",
          8:	"Strength",
          9:	"The Hermit",
          10:	"Wheel of Fortune",
          11:	"Justice",
          12:	"The Hanged Man",
          13:	"Death",
          14:	"Temperance",
          15:	"The Devil",
          16:	"The Tower",
          17:	"The Star",
          18:	"The Moon",
          19:	"The Sun",
          20:	"Judgement",
          21:	"The World",
          22: "The Fool"
}

spread = {}

spread.update({"past":tarot.get(13)})
tarot.pop(13)

spread.update({"present":tarot.get(22)})
tarot.pop(22)

spread.update({"future":tarot.get(10)})
tarot.pop(10)

for card, meaning in spread.items():
  print("Your "+str(card)+" is the "+meaning+" card.")