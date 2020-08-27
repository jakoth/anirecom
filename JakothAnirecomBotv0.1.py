name = "Jakoth's AniRecom Bot"
print(name + ' v0.1')
user_name = input("Hi! What's your name? ")
print("Welcome to Anirecom, " + user_name + '.')
give = input("What can I do for you? ")
print("Well, I only give Anime recommendations. So that's what we're going to do!")
age = int(input('Inform me of your age so we can proceed. '))
if age < 13:
    print("Gotcha. I have the perfect recommendations for you!")
    print('1. Pokemon '
          '2. Death Note '
          '3. Naruto '
          '4. Doraemon '
          '5. My Hero Academia '
          '6. Shinchan '
          '7. Idaten Jump '
          '8. One Piece '
          '9. Case Closed '
          '10. Dragon Ball Z.')
elif age > 12:
    print('Hmm, Gotcha. I know just the right anime for you!')
    print("Here's my pick: "
          "1. Death Note "
          "2. Steins; Gate "
          "3. One Punch Man "
          "4. Code Geass "
          "5. Monster "
          "6. Full Metal Alchemist: Brotherhood "
          "7. Great Teacher Onizuka "
          "8. My Hero Academia "
          "9. Sword Art Online "
          "10. 91 Days. ")
happy = input('Are you satisfied with the recommendations? ')
print(happy + '? Alright then.')
print(" This bot is still in it's early stages of development. We welcome any positve feedback.")
print("Thank you for using Jakoth's Anirecom bot. ")
