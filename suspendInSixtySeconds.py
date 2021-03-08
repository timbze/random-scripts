import os
import threading

import PySimpleGUI as sg

sg.theme('DarkAmber')  # Add a touch of color
window_initialized = False
cancelled = False
seconds = [60]


def f(f_stops: threading.Event):
    if cancelled:
        return
    elif seconds[0] > 0:
        seconds[0] = (seconds[0]-1)

        threading.Timer(1, f, [f_stops]).start()
        if window_initialized:
            window['suspendMessage'].update(get_suspend_message())
    else:
        suspend_now()


def suspend_now():
    os.system('systemctl suspend')
    window.write_event_value('Cancel', '')


f_stop = threading.Event()
f(f_stop)


def get_suspend_message():
    return f'System will suspend in {seconds[0]} seconds'


layout = [[sg.Text('')],
          [sg.Text(get_suspend_message(), key='suspendMessage')],
          [sg.Text('')],
          [sg.Text('Press cancel if you don''t want to suspend')],
          [sg.Text('')],
          [sg.Button('Cancel')]]

window = sg.Window('Suspend Timer', layout)
window_initialized = True

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	 # if user closes window or clicks cancel
        cancelled = True
        seconds[0] = 0
        break

window.close()
