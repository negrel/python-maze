def menu():
    # Menu
    menu = Page("menu")
    menu.appendElement(image)

    menu.appendElement(
        Button(*CENTER,
               BTN_WIDTH,
               BTN_HEIGHT,
               "Jouer",
               lambda event: app.push_page(play),
               background=WHITE,
               color=BLACK))
    menu.appendElement(
        Button(CENTER[0],
               CENTER[1] + 92,
               BTN_WIDTH,
               BTN_HEIGHT,
               "Résoudre",
               lambda event: print("Résoudre"),
               background=WHITE,
               color=BLACK))

    # Bouton pour quitter l'application
    btn_quitter = Button(CENTER[0] + (BTN_WIDTH + 10),
                         (window_height - window_height / 10),
                         BTN_WIDTH,
                         BTN_HEIGHT,
                         "Quitter",
                         lambda event: app.quit(),
                         background=BLACK)
    menu.appendElement(btn_quitter)

    btn_retour = Button(CENTER[0] - (BTN_WIDTH + 10),
                        (window_height - window_height / 10),
                        BTN_WIDTH,
                        BTN_HEIGHT,
                        "Retour",
                        lambda event: app.pop_page(),
                        background=BLACK)
    menu.appendElement(btn_retour)
