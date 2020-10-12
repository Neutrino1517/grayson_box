#!/usr/bin/python3

from gpiozero import LED, Button
#from signal import pause
import simpleaudio as sa
import time

btn_green = LED(25)
button = Button(23)
rot_light = LED(24)
wave_obj = [
#    sa.WaveObject.from_wave_file("/home/pi/starwars.wav"), \
#    sa.WaveObject.from_wave_file("/home/pi/imperial_march.wav"), \
#    sa.WaveObject.from_wave_file("/home/pi/light-saber-battle.wav"), \
#    sa.WaveObject.from_wave_file("/home/pi/ewokpara.wav"), \
#    sa.WaveObject.from_wave_file("/home/pi/continamusic.wav"), \
#    sa.WaveObject.from_wave_file("/home/pi/chewy_roar.wav")
    # sa.WaveObject.from_wave_file("/home/pi/tie_fighter_fire_3.wav"), \
    # sa.WaveObject.from_wave_file("/home/pi/battle_alarm.wav"), \
    # sa.WaveObject.from_wave_file("/home/pi/tie_fighter_flyby_3.wav")
    sa.WaveObject.from_wave_file("/home/pi/tire_squealing.wav"), \
    sa.WaveObject.from_wave_file("/home/pi/harley.wav"), \
    sa.WaveObject.from_wave_file("/home/pi/motorcycle_gang.wav")
    
    
    ]

siren_state = 2
wav_obj_idx = 0

def toggle_siren():
    global siren_state
    if siren_state == 1:
        siren_state = 0
    else:
        siren_state = 1

def next_wav_obj():
    global wav_obj_idx
    
    wav_obj_idx = wav_obj_idx + 1

    if wav_obj_idx >= len(wave_obj):
        wav_obj_idx = 0

    return wave_obj[wav_obj_idx]


button.when_pressed = toggle_siren

print("Beginning loop")


try:
    while True:
        if siren_state == 1:
            btn_green.on()
            rot_light.off()

            try:
                if not play_obj.is_playing():
                    play_obj = next_wav_obj().play()

            except:
                play_obj = next_wav_obj().play()

        elif siren_state == 0:
            btn_green.off()
            rot_light.on()

            try:
                if play_obj.is_playing():
                    play_obj.stop()

            except:
                pass

        else:
            btn_green.on()
            rot_light.on()

        time.sleep(.5)

except KeyboardInterrupt:
    print("Exiting")
