import PySimpleGUI as sg

PAT = "PAT"

layout = [
    [sg.Text("Vaše meno:")],
    [sg.Input(key="name")],

    [sg.Text("Váš vek:")],
    [sg.Input(key="age")],

    [sg.Text("Zadajte 15 slov (oddelené medzerou):")],
    [sg.Input(key="words")],

    [sg.Button("Vyhľadať"), sg.Button("Zrušiť")],

    [sg.Text("Výsledok:")],
    [sg.Multiline(size=(50, 12), key="output", autoscroll=True)]
]

window = sg.Window("PAT Finder", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Zrušiť"):
        break

    if event == "Vyhľadať":

        name = values["name"]
        age = values["age"]
        text = values["words"]

        # Kontrola mena a veku
        if not name or not age:
            window["output"].update("Prosím zadajte meno a vek!")
            continue

        if not age.isdigit():
            window["output"].update("Vek musí byť číslo!")
            continue

        words = text.split()

        if len(words) != 15:
            window["output"].update("Musíte zadať presne 15 slov!")
            continue

        # Lowercase porovnanie (ignoruje veľkosť písmen)
        found = [w for w in words if PAT.lower() in w.lower()]

        # Výsledok
        if found:
            result = (
                f"Výsledky hľadania pre používateľa {name}, vek {age}:\n"
                f"Hľadaný reťazec (bez ohľadu na veľkosť písmen): {PAT}\n"
                f"Počet nájdených slov: {len(found)}\n\n"
                "Slová obsahujúce PAT:\n" + "\n".join(found)
            )
        else:
            result = (
                f"Používateľ {name}, vek {age}:\n"
                f"Žiadne zadané slová neobsahujú PAT."
            )

        window["output"].update(result)

window.close()