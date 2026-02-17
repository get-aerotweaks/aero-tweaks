from customtkinter import * 
from hPyT import * 
from PIL import Image 
import os
import webbrowser
import subprocess
import sys
import ctypes


# Fix paths for dev and PyInstaller
if getattr(sys, 'frozen', False):
    # PyInstaller bundle
    base_path = sys._MEIPASS
else:
    # Normal dev
    base_path = os.path.dirname(os.path.abspath(__file__))

# Change current working directory
os.chdir(base_path)

def load_image(path, size=None):
    full_path = os.path.join(base_path, path)
    return CTkImage(light_image=Image.open(full_path), size=size)

version = "2.1.1"

font_path = os.path.join(base_path, "fonts", "ReadexPro-Regular.ttf")
ctypes.windll.gdi32.AddFontResourceExW(font_path, 0x10, 0)

os.chdir(base_path)


app = CTk()
app.iconbitmap("images/transparent.ico")
app.geometry("720x420")
app.title(f"Aero Tweaks - {version}")


set_default_color_theme("aerotheme.json")
app.resizable(False, False)


# --- hPyT Code Start ---

maximize_minimize_button.hide(app)
title_bar_color.set(app, color="#0B0B21")
corner_radius.set(app, style="round")

# maximize_minimize_button.unhide(window)
# --- hPyT Code End --

## FUNCTIONS ##

def restart_pc():
    os.system("shutdown /r /t 1")

def switch_btns(switch_to):

    if switch_to == 'performance':
        button_2.configure(fg_color='#0B0B21', text_color="#A0A0A0")
        button_1.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_4.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_3.configure(fg_color='#0B0B21', text_color="#FFFFFF")

        for widgets in main_frame.winfo_children():
            widgets.destroy()

        performance_page()
    
    elif switch_to == 'system':
        button_1.configure(fg_color='#0B0B21', text_color="#A0A0A0")
        button_2.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_4.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_3.configure(fg_color='#0B0B21', text_color="#FFFFFF")

        for widgets in main_frame.winfo_children():
            widgets.destroy()

        system_page()

    elif switch_to == 'cleaning':
        button_3.configure(fg_color='#0B0B21', text_color="#A0A0A0")
        button_2.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_4.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_1.configure(fg_color='#0B0B21', text_color="#FFFFFF")

        for widgets in main_frame.winfo_children():
            widgets.destroy()

        cleaning_page()

    elif switch_to == 'privacy':
        button_4.configure(fg_color='#0B0B21', text_color="#A0A0A0")
        button_2.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_3.configure(fg_color='#0B0B21', text_color="#FFFFFF")
        button_1.configure(fg_color='#0B0B21', text_color="#FFFFFF")

        for widgets in main_frame.winfo_children():
            widgets.destroy()

        privacy_page()

def social_media(socialmedia_btns_switch):
    if socialmedia_btns_switch == 'youtube':
        webbrowser.open("https://www.youtube.com/@AeroTweaks")

    elif socialmedia_btns_switch == 'github':
        webbrowser.open("https://github.com/get-aerotweaks")

    elif socialmedia_btns_switch == 'discord':
        webbrowser.open("https://discord.com/invite/mdZ9uJHaX2")

###################

## BATCH OPENINGS ##

def script_path(script_file):
        subprocess.Popen(
             f'powershell -Command "Start-Process cmd -ArgumentList \'/c {script_file}  \' -Verb RunAs"',
            shell=True
        )


## START NAV BAR ##
navbar = CTkFrame(app,
                  height=420,
                  width=150,
                  fg_color="#0B0B21",
                  corner_radius=0)

navbar.grid_propagate(False)
navbar.grid( row=0, column=0, padx=0, pady=0)

## START NAV BAR ITEMS ##

ico_image = CTkImage(light_image=Image.open("images/White_Logo.png"), size=(100, 100))

ico_img_label = CTkLabel(app, text="", image=ico_image, fg_color="#0B0B21")
ico_img_label.place(x=25, y=5)

#Github Btn
git_image = CTkImage(light_image=Image.open("images/github.png"), size=(20, 20))

git_img_label = CTkLabel(app, text="",
                        image=git_image,
                        bg_color="#0B0B21",
                        cursor='hand2',
                        
                        )
git_img_label.place(x=35, y=95)

git_img_label.bind("<Button 1>", lambda e: social_media('github'))
##############


#Youtube Btn
yt_image = CTkImage(light_image=Image.open("images/youtube.png"), size=(22, 14))

yt_img_label = CTkLabel(app, text="",
                        image=yt_image,
                        bg_color="#0B0B21",
                        cursor='hand2',
                        )
yt_img_label.place(x=95, y=95)

yt_img_label.bind("<Button 1>", lambda e: social_media('youtube'))
##############

#Discord Btn
dc_image = CTkImage(light_image=Image.open("images/discord.png"), size=(25, 25))

dc_img_label = CTkLabel(app, text="",
                        image=dc_image,
                        bg_color="#0B0B21",
                        cursor='hand2',
                        )
dc_img_label.place(x=63, y=95)

dc_img_label.bind("<Button 1>", lambda e: social_media('discord'))
##############

#Button 1
button_1 = CTkButton(navbar,
                     text='System',
                     fg_color="transparent",
                     hover_color="#18183A",
                     cursor='hand2',
                     font=("Readex Pro", 19),
                     command=lambda: switch_btns(switch_to='system'),
                    )

button_1.place(x=5, y=140)


#Button 2
button_2 = CTkButton(navbar,
                     text='Performance',
                     hover_color="#18183A",
                     cursor='hand2',
                     fg_color="transparent",
                     font=("Readex Pro", 19),
                     command=lambda: switch_btns(switch_to='performance')
                    )

button_2.place(x=5, y=180)

#Button 3
button_3 = CTkButton(navbar,
                     text='Cleaning',
                     hover_color="#18183A",
                     cursor='hand2',
                     fg_color="transparent",
                     font=("Readex Pro", 19),
                     command=lambda: switch_btns(switch_to='cleaning')
                    )

button_3.place(x=5, y=220)

#Button 4
button_4 = CTkButton(navbar,
                     text='Privacy',
                     hover_color="#18183A",
                     cursor='hand2',
                     fg_color="transparent",
                     font=("Readex Pro", 19),
                     command=lambda: switch_btns(switch_to='privacy')
                    )

button_4.place(x=5, y=260)

#Restart Button 
restart_button = CTkButton(navbar,
                     text='Restart',
                     hover_color="#18183A",
                     fg_color="#C9008D",
                     cursor='hand2',
                     font=("Readex Pro", 19),
                     command=restart_pc
                    )

restart_button.place(x=5, y=375)

##END NAVBAR ##

## START MAIN FRAME ##
main_frame = CTkFrame(master=app, width=570, height=420, corner_radius=0, fg_color="#0E0E27")
main_frame.place(x=150, y=0)

## START PRIVACY PAGE ##
def privacy_page():
    heading_lb = CTkLabel(master=main_frame, text='Privacy',
                          font=('Readex Pro', 30))
    heading_lb.place(x=20, y=10)

    disabletelemetry_btn = CTkButton(master=main_frame,
                    text='Disable Telemetry',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/privacy/disable_telemetry_extreme.ps1"),
                    )

    disabletelemetry_btn.place(x=20, y=80)

    disablerecall_btn = CTkButton(master=main_frame,
                    text='Disable Recall',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/privacy/recall.ps1"),
                    )

    disablerecall_btn.place(x=210, y=80)

## END PRIVACY PAGE ##

## START CLEANING PAGE ##
def cleaning_page():
    heading_lb = CTkLabel(
                    master=main_frame,
                    text='Cleaning',
                    font=('Readex Pro', 30))
    
    heading_lb.place(x=20, y=10)

    tempfiles_btn = CTkButton(
                    master=main_frame,
                    text='Clean Temporary Files',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/cleaning/clear_temp_files.ps1")
                    )

    tempfiles_btn.place(x=230, y=80)

    prefetch_btn = CTkButton(
                    master=main_frame,
                    text='Clear Prefetch Files',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/cleaning/clear_prefetch.ps1")
                    )

    prefetch_btn.place(x=20, y=80)
 
    ## DEBLOAT ##

    heading_lb = CTkLabel(
                    master=main_frame,
                    text='Debloat (Remove)',
                    font=('Readex Pro', 30))
    
    heading_lb.place(x=20, y=140)

    my_frame = CTkScrollableFrame(main_frame,
    orientation="vertical",
	width=490,
	height=20,
	border_width=0,
	fg_color="#131341",
	corner_radius = 20,

	)

    my_frame.place(x=20, y=190)
    my_frame._scrollbar.configure(height=160)


    paint_btn = CTkButton(
                    master=my_frame,
                    text='Paint',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/paint.ps1"),

                    )

    paint_btn.grid(row=0, column=0, padx=10, pady=10)

    notepad_btn = CTkButton(
                    master=my_frame,
                    text='Notepad',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/notepad.ps1"),

                    )

    notepad_btn.grid(row=0, column=1, padx=10, pady=10)

    alarmsclock_btn = CTkButton(
                    master=my_frame,
                    text='Alarms & clock',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/alarmsclock.ps1"),

                    )

    alarmsclock_btn.grid(row=0, column=2, padx=10, pady=10)

    calculator_btn = CTkButton(
                    master=my_frame,
                    text='Calculator',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/calculator.ps1"),

                    )

    calculator_btn.grid(row=2, column=0, padx=10, pady=10)

    camera_btn = CTkButton(
                    master=my_frame,
                    text='Camera',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/camera.ps1"),
                    )

    camera_btn.grid(row=2, column=1, padx=10, pady=10)

    copilot_btn = CTkButton(
                    master=my_frame,
                    text='Copilot',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/copilot.ps1"),

                    )

    copilot_btn.grid(row=2, column=2, padx=10, pady=10)

    feedback_btn = CTkButton(
                    master=my_frame,
                    text='Feedback',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/feedback.ps1"),

                    )

    feedback_btn.grid(row=3, column=0, padx=10, pady=10)

    gethelp_btn = CTkButton(
                    master=my_frame,
                    text='Get Help',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/gethelp.ps1"),

                    )

    gethelp_btn.grid(row=3, column=1, padx=10, pady=10)

    microsoftstore_btn = CTkButton(
                    master=my_frame,
                    text='Microsoft Store',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/microsoftstore.ps1"),

                    )

    microsoftstore_btn.grid(row=3, column=2, padx=10, pady=10)

    moviestv_btn = CTkButton(
                    master=my_frame,
                    text='Movies & Tv',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/moviesTV.ps1"),

                    )

    moviestv_btn.grid(row=4, column=0, padx=10, pady=10)

    onenote_btn = CTkButton(
                    master=my_frame,
                    text='Onenote',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/onenote.ps1"),

                    )

    onenote_btn.grid(row=4, column=1, padx=10, pady=10)

    yourphone_btn = CTkButton(
                    master=my_frame,
                    text='Your phone',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/yourphone.ps1"),

                    )

    yourphone_btn.grid(row=4, column=2, padx=10, pady=10)


    photos_btn = CTkButton(
                    master=my_frame,
                    text='Photos',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/photos.ps1"),
                    )

    photos_btn.grid(row=5, column=0, padx=10, pady=10)

    snippingtool_btn = CTkButton(
                    master=my_frame,
                    text='Snipping Tool',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/SnippingTool.ps1"),

                    )

    snippingtool_btn.grid(row=5, column=1, padx=10, pady=10)

    xbox_btn = CTkButton(
                    master=my_frame,
                    text='Xbox (ALL)',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/xbox.ps1"),

                    )

    xbox_btn.grid(row=5, column=2, padx=10, pady=10)
 

## END CLEANING PAGE ##

## START SYSTEM PAGE ##
def system_page():
    heading_lb = CTkLabel(master=main_frame, text='System',
                          font=('Readex Pro', 30))
    heading_lb.place(x=20, y=10)

    restoredefaultsettings_btn = CTkButton(master=main_frame,
                    text='Restore default settings',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/system/restore_defaults.ps1"),
                    )

    restoredefaultsettings_btn.place(x=20, y=80)

    disablestartupapps_btn = CTkButton(master=main_frame,
                    text='Disable Startup Apps',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/disable_startup_apps.ps1"),
                    )

    disablestartupapps_btn.place(x=270, y=80)

    flushdns_btn = CTkButton(master=main_frame,
                    text='Flush Dns',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/flush_dns.ps1"),
                    )

    flushdns_btn.place(x=20, y=140)

    hibernation_btn = CTkButton(master=main_frame,
                    text='Hibernation',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/hibernation.ps1"),
                    )

    hibernation_btn.place(x=175, y=140)

    createrestorepoint_btn = CTkButton(master=main_frame,
                    text='Create restore Point',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/debloat/create_restore_point.ps1"),
                    )

    createrestorepoint_btn.place(x=20, y=200)


## END SYSTEM PAGE ##


## START PERFORMANCE PAGE ##
def performance_page():
    heading_lb = CTkLabel(master=main_frame, text='Performance',
                          font=('Readex Pro', 30))
    heading_lb.place(x=20, y=10)

    ###BTNS PERFORMANCE MODE ##
    performancemode_btn = CTkButton(master=main_frame,
                    text='Enable performance mode',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/performance/performance_mode_extreme.ps1"),
                    )

    performancemode_btn.place(x=20, y=80)

    performanceoptions_btn = CTkButton(master=main_frame,
                    text='Open Performance Options',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path(r"C:\Windows\System32\SystemPropertiesPerformance.exe")

                    )

    performanceoptions_btn.place(x=290, y=80)


    disablesysmain_btn = CTkButton(master=main_frame,
                    text='Disable SysMain (Recommend HDDs)',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/performance/disable_sysmain.ps1"),
                    )

    disablesysmain_btn.place(x=20, y=140)

    disablevisualeffects_btn = CTkButton(master=main_frame,
                    text='Disable Visual Effects',
                    hover_color="#18183A",
                    cursor='hand2',
                    fg_color="#222272",
                    font=("Readex Pro", 19),
                    command=lambda: script_path("scripts/performance/disable_visual_effects.ps1"),
                    )

    disablevisualeffects_btn.place(x=20, y=200)



## END PERFORMANCE PAGE ##

def welcome_page():
    heading_lb = CTkLabel(master=main_frame, text='WELCOME TO AERO, ENJOY!',font=('Readex Pro', 30))
    heading_lb.place(x=70, y=180)

    label = CTkLabel(master=main_frame, text="Disclaimer: The developers are not responsible for any damage or data loss. Use at your own risk. ", font=('Readex Pro', 11))
    label.place(x=23, y=385)
    label = CTkLabel(master=main_frame, text=f"Version: {version}. ", font=('Readex Pro', 17))
    label.place(x=200, y=220)

welcome_page()

## END MAIN FRAME ##

app.mainloop()
