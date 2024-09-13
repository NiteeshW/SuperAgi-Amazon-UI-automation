import re

import products as products
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://www.amazon.in")


search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("LG soundbar")
search_box.submit()


wait = WebDriverWait(driver, 10)
assert driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span').is_displayed()


products = [
    {"name": "LG Sound Bar S65Tr, 5.1Ch, 600W Dolby Digital Soundbar for Tv with Wireless Woofer and Wireless Rear Speaker, Hdmi Optical Connectivity,Black", "price": 29999},
    {"name": "LG Sound Bar Sc9S, 3.1.3 Ch, 400W (Bluetooth, HDMI, Optical connectivity) Perfect Matching for OLED C2/C3 Tv with Imax Enhanced, Dolby Atmos Soundbar, Black", "price": 33239},
    {"name": "Samsung Soundbar (HW-C45E/XL) 2.1 Channel, 300W, Dolby Digital, 3 Speakers, Wireless Subwoofer, Bluetooth Enabled and DTS Virtual X Experience Sound (Black)", "price": 10999},
    {"name": "LG New Launch Soundbar SQ70TY, 400W, 3.1.1Ch, Dolby Atmos & DTS: X, Hi-Res Audio, Center Up-Firing Speaker, AI Sound Pro, Wow Synergy, Wireless Subwoofer, QNED Matching Bracket Inside (2024 QNED TV)", "price": 31990},
    {"name": "LG New Launch Sq75Tr,600W,5.1.1Ch,Dolby Atmos,Center Up-Firing Speaker,Ai Sound Pro,Wow Synergy,Wireless Subwoofer,Rear Speaker Inbuilt Receiver,Qned Matching Bracket Inside(2024 Qned Tv),Black", "price": 44790},
    {"name": "LG Sound Bar with Surround Speakers S95Qr-9.1.5 Channel,810 Watts Output,Home Theater Audio with Dolby Atmos,DTS:X,&Imax Enhanced,Wi-Fi,Multi", "price": 69490},
    {"name": "JBL Cinema SB241, Dolby Digital Soundbar with Wired Subwoofer for Extra Deep Bass, 2.1 Channel Home Theatre with Remote, HDMI ARC, Bluetooth & Optical Connectivity (110W)", "price": 8498},
    {"name": "Mivi Fort Q500 Soundbar with 500W Surround Sound, 5.1 Channel with External subwoofer & 2 Satellite Speakers, Multiple EQ & Input Modes, Remote, BT v5.3, Made in India Sound bar for TV", "price": 9999},
    {"name": "VW Hunter Bar | 160W Soundbar | 2.1 Channel Home Theatre | Deep Bass from 6.5\" Subwoofer | Multiple Connectivity | 4 EQ Modes | Sleek Remote & LED Light (Black)", "price": 5499},
    {"name": "LG Electronics SPK8-S 2.0 Channel Sound Bar Wireless Rear Speaker Kit compatibel with SN10YG, SN9YG, SN8YG, GX, SN7Y, SN6Y, SN5Y, SP9YA, SP8YA, G1, SPD7Y, SP7Y (Black)", "price": 12990},
    {"name": "LG New Launch Soundbar S77TY, 400W, 3.1.3Ch, Dolby Atmos & DTS: X, Tripple Up-Firing Speaker, AI Sound Pro, WOW Synergy, Triple Level Spatial Sound, Smart Up-Mixer, VRR/ALLM /120Hz, Wireless Subwoofer", "price": 38009},
    {"name": "Samsung Soundbar (HW-B67E/XL) 5.1 Channel, Wireless Subwoofer, 1x Wireless Rear Speaker, 1x Center Speaker and Energy Star, Dolby 5.1ch & DTS Virtual X Experience Sound (Black)", "price": 21899},
    {"name": "(Refurbished) LG Soundbar SP2, 100W 2.1Ch Home Theatre System, Built-in Subwoofer for Powerful Bass in Eco-Friendly Fabric Wrapped Design, AI Sound Pro, Bluetooth, HDMI", "price": 10999},
    {"name": "boAt Aavante Bar 4100DA Bluetooth Soundbar with Dolby Atmos 3D Cinematic Sound,300W RMS Signature Sound,3.1.2 Channel, BT v5.3,Multi-Connectivity&EQ Modes &Remote Control(Premium Black)", "price": 12999},
    {"name": "JBL CINEMA SB190 Deep Bass, Dolby Atmos Soundbar with Wireless Subwoofer for Extra Deep Bass, 2.1 Channel with Remote, Sound Mode for Voice Clarity, HDMI eARC, Bluetooth & Optical Connectivity (380W)", "price": 19999},
    {"name": "GOVO GoSurround 990 Dolby Digital | 525W Sound bar, 5.1 Channel Home Theatre, 6.5\" Wireless subwoofer and Satellite Speakers, HDMI, Opt, AUX, USB & Bluetooth, 3 Equalizer Modes, LED Display (Black)", "price": 11999},
    {"name": "ZEBRONICS Juke BAR 100A Compact Soundbar with Subwoofer, 60W RMS Output, Powerful Bass, Glossy Design, HDMI ARC, Coaxial, Bluetooth 5.0, AUX, LED Indicator and Remote Control", "price": 3499},
    {"name": "Samsung Soundbar (HW-C45E/XL) 2.1 Channel, 300W, Dolby Digital, 3 Speakers, Wireless Subwoofer, Bluetooth Enabled and DTS Virtual X Experience Sound (Black)", "price": 10999},
    {"name": "GOVO GoSurround 990 Dolby Digital | 525W Sound bar, 5.1 Channel Home Theatre, 6.5\" Wireless subwoofer and Satellite Speakers, HDMI, Opt, AUX, USB & Bluetooth, 3 Equalizer Modes, LED Display (Black)", "price": 11999}
]


product_dict = {}
for product in products:
    product_dict[product["name"]] = product["price"]

# Sort the dictionary by values (prices)
sorted_products = dict(sorted(product_dict.items(), key=lambda item: item[1]))



sorted_products = sorted(products, key=lambda product: product["price"])


for product in sorted_products:
    price = product["price"]
    name = product["name"]
    wattage = ""
    if "Watt" in name:
        wattage = " ".join(re.findall(r'\d+Watt', name))
    print(f"{price} {name.split(',')[0]} {wattage}")