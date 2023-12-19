from tkinter import *
import datetime
import time
import winsound
from threading import Thread

main_window = Tk()

# Set Geometry
main_window.geometry("400x200")
main_window.configure(bg='black')  # Set the background color to black

# Threading Usage
def use_thread():
    t1 = Thread(target=set_alarm)
    t1.start()

def set_alarm():
    # Infinite Loop
    while True:
        # Set the Alarm Time
        alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, alarm_time)

        # Check if the set alarm time matches the current time
        if current_time == alarm_time:
            print("Wake Up Time")
            # Play Sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

# Labels, Frame, Buttons, and Option Menus
Label(main_window, text="Alarm Clock", font=("Helvetica", 20, 'bold italic'), fg="red", bg='black').pack(pady=10)
Label(main_window, text="Set Time", font=("Helvetica", 15, 'italic'), bg='black').pack()

frame = Frame(main_window, bg='black')
frame.pack()

hour = StringVar(main_window)
hours = tuple([str(i).zfill(2) for i in range(25)])  # Format the hours
hour.set(hours[0])

hour_menu = OptionMenu(frame, hour, *hours)
hour_menu.pack(side=LEFT)

minute = StringVar(main_window)
minutes = tuple([str(i).zfill(2) for i in range(61)])  # Format the minutes
minute.set(minutes[0])

minute_menu = OptionMenu(frame, minute, *minutes)
minute_menu.pack(side=LEFT)

second = StringVar(main_window)
seconds = tuple([str(i).zfill(2) for i in range(61)])  # Format the seconds
second.set(seconds[0])

second_menu = OptionMenu(frame, second, *seconds)
second_menu.pack(side=LEFT)

Button(main_window, text="Set Alarm", font=("Helvetica", 15, 'bold'), command=use_thread, relief=RIDGE).pack(pady=20)

# Run Tkinter
main_window.mainloop()
