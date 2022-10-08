print('''
     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777
''')
print('Welcome back bond! We have been waiting for you.')
ready_to_start = input(
    ("Are you ready for your first mission? y or n?")).lower() == "y"

if ready_to_start:
    print("""
     ______________________________    . \  | / .
     /                            / \     \ \ / /
    |                            | ==========  - -
     \____________________________\_/     / / \ \\
    """)
    print("""
                  _.-^^---....,,---_
           _--                  --_
          <          BOOM!         >)
           \._                   _./
              ```--. . , ; .--'''
                    | |   |
                 .-=||  | |=-.
                 `-=#$%&%$#=-'
                    | ;  :|
           _____.,-#%&$@%#&#~,._____
    """)

    is_fighting = input(
        "Men entering the front door👮🏼, should you run or fight? run or fight? ").lower() == "run"

    if is_fighting:
        print("Good work, all villains are down")
        print("Hurry, more are coming!")

        jump_from_window = input(
            "Should you jump from the window or roof? ").lower() == "window"
        if jump_from_window:
            print("You landed in water🌊!")
            print("You'll live! Swim")
        else:
            print("Oh no, Helicopter above with the a machine gun")
            shoot_pilot = input(
                "Shoot the pilot or the rifle men? 🔫 ").lower() == "pilot"
            if shoot_pilot:
                print("Jump~")
                print("Well done! You live")
            else:
                print("The pilot crashed the plane on your head😐")
    else:
        print("Boom, you died!")

else:
    print("Good to see you")
