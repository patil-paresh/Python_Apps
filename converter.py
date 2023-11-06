import PySimpleGUI as sg

layout = [[sg.Input(key="input"), sg.Spin(['km to miles', 'kg to pound', "sec to min"], key="units"), sg.Button("Convert", key="convert")],
          [sg.Text("Output", key="output")]]
window = sg.Window("Converter", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "convert":
        input_value = values['input']

        # Validate input as a float
        try:
            input_value = float(input_value)
        except ValueError:
            window['output'].update("Please enter a valid number")
            continue

        match values["units"]:
            case 'km to miles':
                output = round(input_value * 0.6214, 2)
                output_str = f"{input_value} km are {output} miles"
            case 'kg to pound':
                output = round(input_value * 2.20462, 2)
                output_str = f"{input_value} kg is {output} pounds"
            case 'sec to min':
                output = round(input_value / 60, 2)
                output_str = f"{input_value} seconds are {output} minutes"
        window['output'].update(output_str)

window.close()
