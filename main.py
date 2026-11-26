import tkinter as tk
from tkinter import ttk

#colours
BG = "#FFF0F5"
PANEL = "#FFE0EB"
PINK = "#FF93B9"
DARKPINK = "#CE0555"
TEXT = "#4A3040"
GREEN = "#04FF00"
RED = "#FF0000"
WHITE = "#FFFFFF"

#creating the application window
root = tk.Tk()
root.title("Intelligent Headphones")
root.geometry("850x700")
root.configure(bg=BG)
root.minsize(750,650) #sets the minimum size of the application window

#heading

header = tk.Frame(root, bg=BG)
header.pack(fill="x",padx=30,pady=(25,10))

title = tk.Label(
    header, text="Intelligent Headphones", #get rid of the hearts maybe lol
    font=("Arial", 24, "bold"), fg=DARKPINK,
    bg=BG
)
title.pack(anchor="w") #anchors define where text needs to be positioned relative to a reference point

subtitle = tk.Label(
        header,text="Your audio. Your environment. Your control.",
        font=("Arial", 11), fg=TEXT,bg=BG,
)
subtitle.pack(anchor="w",pady=5)

statusPanel = tk.Frame(root, bg=PANEL)
statusPanel.pack(fill="x",padx=30,pady=10)
statusTitle = tk.Label(statusPanel,text="Headphone Status",
                       font=("Arial",12,"bold"),
                       fg=DARKPINK,bg=PANEL)
statusTitle.pack(anchor="w",padx=20,pady=(15,10))

status = tk.Label(statusPanel,text="● Music is playing",
                  font=("Arial",12,"bold"),fg=GREEN,bg=PANEL)

status.pack(anchor="w",padx=20,pady=5)

modeStatus = tk.Label(statusPanel, text="Noise Cancellation: ON",
                      font=("Arial",11),fg=TEXT,bg=PANEL)
modeStatus.pack(anchor="w",padx=20,pady=5)

controls = tk.Frame(root,bg=BG)
controls.pack(fill="x",padx=30,pady=10)

controlTitle = tk.Label(controls,text="Headphone Controls",font=("Arial",12,"bold"),
                        fg=DARKPINK,bg=BG)
controlTitle.pack(anchor="w",pady=(5,10))

mode = tk.StringVar(value="Noise cancellation")

def changeMode():
        modeStatus.config(text=f"Audio mode: {mode.get()}")

modeMenu = tk.OptionMenu(controls,mode,"Noise Cancellation","Ambient Mode","Off",
                         command=lambda _: changeMode())

modeMenu.config(bg=PINK,fg=TEXT,font=("Arial",11),activebackground=DARKPINK,activeforeground=WHITE,relief="flat")

modeMenu["menu"].config(bg=WHITE,fg=TEXT)
modeMenu.pack(anchor="w",pady=5)

simulator = tk.Frame(root, bg=BG)
simulator.pack(fill="x",padx=30,pady=10)
simTitle = tk.Label(
        simulator,text="ENVIRONMENTAL SOUND SIMULATOR",font=("Arial",12,"bold"),
        fg=DARKPINK,bg=BG)
simTitle.pack(anchor="w",pady=(5,10))

sound = tk.StringVar(value="Conversation")
soundMenu = tk.OptionMenu(simulator,sound,"Conversation","Alarm","Siren",
                          "Dog barking","Door knock") #add new options here too such as Alarm or General Talking

soundMenu.config(bg=PINK,fg=TEXT,font=("Arial",11),activebackground=DARKPINK,activeforeground=WHITE,relief="flat")
soundMenu["menu"].config(bg=WHITE,fg=TEXT)

soundMenu.pack(anchor="w",pady=5)

notificationPanel = tk.Frame(root,bg=WHITE)
notificationPanel.pack(fill="x",padx=30,pady=15)
notificationTitle = tk.Label(notificationPanel,text="SYSTEM NOTIFICATION",font=("Arial",12,"bold"),fg=DARKPINK,bg=WHITE)
notificationTitle.pack(anchor="w",padx=20,pady=(15,10))
notification = tk.Label(notificationPanel,text="No environmental sounds detected.",font=("Arial",11),fg=TEXT,bg=WHITE,wraplength=700,justify="left")
notification.pack(anchor="w",padx=20,pady=5)

def detectSound():
        selectedSound = sound.get()
        responses = {"Conversation": "Music volume reduced", "Alarm": "Ambient mode enabled and alert displayed",
                     "Siren" : "Music reduced and ambient mode enabled", "Dog barking" : "No audio change","Door knock": "Music volume reduced",
                    }
        explanations = {"Conversation": "Nearby voices were detected.", "Alarm" : "A potential alarm was detected.",
                        "Siren": "A siren was detected in your surroundings.", "Dog barking": "A dog barking was detected.",
                        "Dog barking": "A dog barking was detected.", "Door knock": "A knocking sound was detected."}
        response = responses[selectedSound]
        explanation = explanations[selectedSound]
        status.config(
                text=f"● {selectedSound} detected!",
                fg=RED)

        notification.config(
                text=f"Detected: {selectedSound}\n\n"
                     f"Reason: {explanation}\n\n"
                     f"System response: {response}",

                fg=RED
        )

        history.insert(0,f"{selectedSound} - {response}")

        if selectedSound in ["Alarm","Siren"]:
                modeStatus.config(text="Audio mode: Ambient mode")

def resetSystem():

        status.config(text="● Music is playing",fg=GREEN)
        notification.config(text="No environmental sounds detected.",fg=TEXT)
        modeStatus.config(text=f"Audio mode: {mode.get()}")

buttonFrame = tk.Frame(root, bg=BG)
buttonFrame.pack(pady=10)

detectButton = tk.Button(buttonFrame,text="Simulate sound detection",command=detectSound,bg=PINK,fg=TEXT,font=("Arial",11,"bold"),padx=15,pady=10,relief="flat")
detectButton.pack(side="left",padx=10)

resetButton = tk.Button(buttonFrame,text="Reset headphones",command=resetSystem,bg="#" \
"F5C6D8",fg=TEXT,font=("Arial",11),padx=15,pady=10,relief="flat")
resetButton.pack(side="left",padx=10)

historyPanel = tk.Frame(root,bg=PANEL)
historyPanel.pack(fill="both",expand=True,padx=30,pady=15)

historyTitle = tk.Label(historyPanel,text="RECENT DETECTIONS",font=("Arial",12,"bold"),fg=DARKPINK,bg=PANEL)
historyTitle.pack(anchor="w",padx=20,pady=(15,10))

history = tk.Listbox(historyPanel,bg=WHITE,fg=TEXT,font=("Arial",10),relief="flat",height=5)
history.pack(fill="both",expand=True,padx=20,pady=(0,15))


root.mainloop()


