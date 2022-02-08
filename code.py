from adafruit_macropad import MacroPad
import time
import board
import busio
import adafruit_htu31d
import usb_cdc
import struct

def switch_color_setting(colors,pix):
    if len(colors) != len(pix):
        pix.fill(colors)
    else:
        for i in range(len(pix)):
            pix[i] = colors[i]

def i3_worskspace(key_event):
    global mp
    if key_event.key_number == 0:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.ONE)
        mp.keyboard.release_all()
    if key_event.key_number == 1:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.TWO)
        mp.keyboard.release_all()
    if key_event.key_number == 2:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.THREE)
        mp.keyboard.release_all()
    if key_event.key_number == 3:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.FOUR)
        mp.keyboard.release_all()
    if key_event.key_number == 4:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.FIVE)
        mp.keyboard.release_all()
    if key_event.key_number == 5:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.SIX)
        mp.keyboard.release_all()
    if key_event.key_number == 6:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.SEVEN)
        mp.keyboard.release_all()
    if key_event.key_number == 7:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.EIGHT)
        mp.keyboard.release_all()
    if key_event.key_number == 8:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.NINE)
        mp.keyboard.release_all()
    if key_event.key_number == 9:
        mp.consumer_control.send(
            mp.ConsumerControlCode.VOLUME_DECREMENT
        )
        print("Vol DOWN")
    if key_event.key_number == 10:
        mp.keyboard.press(mp.Keycode.GUI, mp.Keycode.ZERO)
        mp.keyboard.release_all()
    if key_event.key_number == 11:
        mp.consumer_control.send(
            mp.ConsumerControlCode.VOLUME_INCREMENT
        )
        print("Vol UP")

def youtube_player(key_event):
    global mp
    if key_event.key_number == 0:
        mp.keyboard.press(mp.Keycode.SHIFT, mp.Keycode.COMMA)
        mp.keyboard.release_all()
    if key_event.key_number == 1:
        mp.keyboard.press(mp.Keycode.PERIOD)
        mp.keyboard.release_all()
    if key_event.key_number == 2:
        mp.keyboard.press(mp.Keycode.SHIFT, mp.Keycode.PERIOD)
        mp.keyboard.release_all()
    if key_event.key_number == 3:
        mp.keyboard.press(mp.Keycode.J)
        mp.keyboard.release_all()
    if key_event.key_number == 4:
        mp.keyboard.press(mp.Keycode.F)
        mp.keyboard.release_all()
    if key_event.key_number == 5:
        mp.keyboard.press(mp.Keycode.L)
        mp.keyboard.release_all()
    if key_event.key_number == 6:
        mp.keyboard.press(mp.Keycode.F5)
        mp.keyboard.release_all()
    if key_event.key_number == 7:
        mp.keyboard.press(mp.Keycode.COMMA)
        mp.keyboard.release_all()
    if key_event.key_number == 8:
        mp.keyboard.press(mp.Keycode.CONTROL,mp.Keycode.TAB)
        mp.keyboard.release_all()
    if key_event.key_number == 9:
        mp.consumer_control.send(
            mp.ConsumerControlCode.VOLUME_DECREMENT
        )
        print("Vol DOWN")
    if key_event.key_number == 10:
        mp.keyboard.press(mp.Keycode.SPACEBAR)
        mp.keyboard.release_all()
    if key_event.key_number == 11:
        mp.consumer_control.send(
            mp.ConsumerControlCode.VOLUME_INCREMENT
        )
        print("Vol UP")

def function_keys(key_event):
    global mp
    if key_event.key_number == 0:
        mp.keyboard.press(mp.Keycode.F1)
        mp.keyboard.release_all()
    if key_event.key_number == 1:
        mp.keyboard.press(mp.Keycode.F2)
        mp.keyboard.release_all()
    if key_event.key_number == 2:
        mp.keyboard.press(mp.Keycode.F3)
        mp.keyboard.release_all()
    if key_event.key_number == 3:
        mp.keyboard.press(mp.Keycode.F4)
        mp.keyboard.release_all()
    if key_event.key_number == 4:
        mp.keyboard.press(mp.Keycode.F5)
        mp.keyboard.release_all()
    if key_event.key_number == 5:
        mp.keyboard.press(mp.Keycode.F6)
        mp.keyboard.release_all()
    if key_event.key_number == 6:
        mp.keyboard.press(mp.Keycode.F7)
        mp.keyboard.release_all()
    if key_event.key_number == 7:
        mp.keyboard.press(mp.Keycode.F8)
        mp.keyboard.release_all()
    if key_event.key_number == 8:
        mp.keyboard.press(mp.Keycode.F9)
        mp.keyboard.release_all()
    if key_event.key_number == 9:
        mp.keyboard.press(mp.Keycode.F10)
        mp.keyboard.release_all()
    if key_event.key_number == 10:
        mp.keyboard.press(mp.Keycode.F11)
        mp.keyboard.release_all()
    if key_event.key_number == 11:
        mp.keyboard.press(mp.Keycode.F12)
        mp.keyboard.release_all()

def number_pad(key_event):
    global mp
    if key_event.key_number == 0:
        mp.keyboard.press(mp.Keycode.SEVEN)
        mp.keyboard.release_all()
    if key_event.key_number == 1:
        mp.keyboard.press(mp.Keycode.EIGHT)
        mp.keyboard.release_all()
    if key_event.key_number == 2:
        mp.keyboard.press(mp.Keycode.NINE)
        mp.keyboard.release_all()
    if key_event.key_number == 3:
        mp.keyboard.press(mp.Keycode.FOUR)
        mp.keyboard.release_all()
    if key_event.key_number == 4:
        mp.keyboard.press(mp.Keycode.FIVE)
        mp.keyboard.release_all()
    if key_event.key_number == 5:
        mp.keyboard.press(mp.Keycode.SIX)
        mp.keyboard.release_all()
    if key_event.key_number == 6:
        mp.keyboard.press(mp.Keycode.ONE)
        mp.keyboard.release_all()
    if key_event.key_number == 7:
        mp.keyboard.press(mp.Keycode.TWO)
        mp.keyboard.release_all()
    if key_event.key_number == 8:
        mp.keyboard.press(mp.Keycode.THREE)
        mp.keyboard.release_all()
    if key_event.key_number == 9:
        mp.keyboard.press(mp.Keycode.ESC)
        mp.keyboard.release_all()
    if key_event.key_number == 10:
        mp.keyboard.press(mp.Keycode.ZERO)
        mp.keyboard.release_all()
    if key_event.key_number == 11:
        mp.keyboard.press(mp.Keycode.RETURN)
        mp.keyboard.release_all()

mp      = MacroPad()
i2c     = busio.I2C(board.SCL,board.SDA,frequency=100000)
no_sens = False
try:
    htu     = adafruit_htu31d.HTU31D(i2c)
except:
    no_sens = True
tl      = mp.display_text()
#tl[0].text = "Hallo"
text    = mp.display_text()
tl.show()
pix     = mp.pixels
red     = (3,0,0)
green   = (0,3,0)
i3_colors = [(3  ,0  ,0  ),(3  ,0  ,0  ),(3  ,0  ,0  ),
             (3  ,0  ,0  ),(3  ,0  ,0  ),(3  ,0  ,0  ),
             (3  ,0  ,0  ),(3  ,0  ,0  ),(3  ,0  ,0  ),
             (0  ,0  ,3  ),(3  ,0  ,0  ),(0  ,0  ,3  )
            ]
num_colors = [(3  ,0  ,0  ),(3  ,0  ,0  ),(3  ,0  ,0  ),
              (3  ,0  ,0  ),(3  ,0  ,0  ),(3  ,0  ,0  ),
              (3  ,0  ,0  ),(3  ,0  ,0  ),(3  ,0  ,0  ),
              (0  ,3  ,3  ),(3  ,0  ,0  ),(3  ,0  ,3  )
             ]
yplayer_c = [(3  ,0  ,3  ),(3  ,0  ,0  ),(3  ,0  ,3  ),
             (3  ,0  ,0  ),(0  ,3  ,0  ),(3  ,0  ,0  ),
             (3  ,3  ,0  ),(3  ,0  ,0  ),(3  ,3  ,0  ),
             (0  ,0  ,3  ),(3  ,3  ,3  ),(0  ,0  ,3  )
            ]

switch_color_setting(i3_colors,pix)

last_position   = mp.encoder
display_counter = 0
while True:
    key_event = mp.keys.events.get()

    if last_position != mp.encoder:
        if mp.encoder == 0:
            switch_color_setting(i3_colors,pix)
        elif mp.encoder == 1:
            switch_color_setting(yplayer_c,pix)
        elif mp.encoder == 2:
            switch_color_setting(red,pix)
        elif mp.encoder == 3:
            switch_color_setting(num_colors,pix)
        else:
            display_counter = 0
            switch_color_setting((0,0,0),pix)
        last_position = mp.encoder

    if key_event:
        if key_event.pressed:
            if mp.encoder == 0:
                i3_worskspace(key_event)
            elif mp.encoder == 1:
                youtube_player(key_event)
            elif mp.encoder == 2:
                function_keys(key_event)
            elif mp.encoder == 3:
                number_pad(key_event)
            else:
                display_counter = 0

    if  display_counter >= 0 and \
        (mp.encoder < 0 or mp.encoder > 3) and \
        not(no_sens):
        temperature, relative_humidity = htu.measurements
        text[1].text = "Temperature: {:.2f} C".format(temperature)
        text[2].text = "Humidity:    {:.2f} %".format(relative_humidity)
        text.show()
        display_counter += 1
        #print(temperature,relative_humidity)
        #usb_cdc.data.write(bytearray("{}\r\n".format(time.monotonic())))
        usb_cdc.data.write(bytearray("{},{},{}\r\n".format(time.monotonic(),temperature,relative_humidity)))
        #usb_cdc.data.write(struct.pack("f",time.monotonic()))
        #usb_cdc.data.write(struct.pack("s"," "))
        #usb_cdc.data.write(struct.pack("f",temperature))
        #usb_cdc.data.write(struct.pack("s"," "))
        #usb_cdc.data.write(struct.pack("f",relative_humidity))
        #usb_cdc.data.write(struct.pack("s","\n"))
    else:
        tl.show()

    #time.sleep(0.1)

