
print("Top 6 of the best free games in 2024!: ")
print("")
print("")
for games in["(1) Enlisted", "(2) THE FINALS", "(3) Farlight84", "(4) Once Human", "(5) War Thunder", "(6) Krunker.io"]:
    print(games)

plyrask = input("Which is your favorite game which is not listed above? (Can be buy-able): ")

inputtetgame = {
    'game' : plyrask
}
print("")
print("")
print(f"Nice! I think I heard of {inputtetgame['game']} before!")
print("")
for list in ["(1) The Price", "(2) The Long Story/Gameplay", "(3) The Graphics"]:
    print(list)
fdbck = int(input("And what exactly is so great about it? Type in one Number from above: "))

if fdbck == 1:
    price = input("Nice! How much is it?: ")
    price1 = {
        'price': price
    }
    print(f"Wow! {price1['price']} is a very good price.. if you got money xD")
    print("Anyways, thanks for using my program!")
elif fdbck == 2:
    print("Very nice! Hope you keep enjoy your game!")
    print("Have a nice day bro and thanks for using my program ;D ")
elif fdbck == 3:
    print("Very nice! Hope you keep enjoy your game!")
    print("Have a nice day bro and thanks for using my program ;D ")

input("Press any key to leave...")









