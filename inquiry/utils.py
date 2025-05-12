from inquiry.models import Product


def populate_products():
    _text_list = """
Peace Naturals 33/1 GC GMO Cookies
Ostara GC Gas Cake
CNBS CPJ 31/1 Cap Junky
Remexian 30/1 HCC BMS Black Mountain Side
CNBS VV 30/1 Varnish Vapor
Pedanios 31/1 COS-CA Cosmic Cream
Canify Cannabis flos 30/1 POR Ku. Chapel of Love
Demecan CRAFT FCF 31:01 First Class Funk
TYSON 2.0 30/1 Tiger Milk
420 Evolution 30/1 CA ICC Ice Cream Cake
Therismos 30/1 ATG Atlantic Glue GG4
Remexian 30/1 CHK Chemical Kush
Remexian 30/1 LPP Lemon Pepper Punch
420 Compound 30/1 GAP Gastro Pop
MC Epic Drop 30/1 Hawaiian Rain X Permanent Marker
Materia 8BK 30/1 8 Ball Kush
Top Shelf Medical S1E2 30/1 Oasis OG
Remexian 30/1 NXN SPZ Spritzer
Remexian 30/1 HCC Grape Gasoline
Remexian 30/1 HCC Blue Pave
Green Karat FS 30/1 Fiji Sunset
Top Shelf Medical S1E3 Wes' Coast Kush
Bathera 28/1 FA Facetz
avaay 29/1 SCG Super Citra G
Cannamedical Indica Ultra Crazy Rntz
avaay Signature 28/1 WB Waffle Bites
Green Karat SD PT Supreme Diesel
Cannamedical CM 28/1 Koko Cookies
LOT 420 LEM PT Lemonatti
Mother 28 B8 CAN Beta 808
avaay 28/1 GNC Grapes and Cream
Cannamedical CM 30/1 Koko Cookies
Green Karat PV Pavé S1
Remexian 27/1 GRG Grape Galena
Barongo 27/1 Mac 3
Remexian 27/1 Eco MYZ Munyunz
ADREX Mother 28 GF CAN Garlic Funk
LOT 420 AB Apple & Bananas
Remexian 27/1 FFG Franco's Fullgas
Wellford Aquaponic 26/1 QSG Queen SanG
ADREX Mother 26 GF CAN Garlic Funk
Patagonia Plus TN The New
All Nations LT 25/1 Lemon Tartz
Cantourage MAC 1+
420 Evolution 25/1 CA TGP Tiger Paw
IMC THC25 T04 Strawberry OG
enua 25/1 SBD CA Strawberry Diesel
Demecan Craft T4N-G 25:01 Banjo
Oceanic BC 25/1 Black Cookies

Origine Nature CHEM 25/1 Chemdawg OG
Grünhorn SCK 25/1 Scotti´s Cake
Demecan Craft Sky 25:01 Sky Pie
enua 25/1 SJ CA Splitter Gelato
NICE KW 24/1 Kirkwood White
KEjF. SPZ 25/1 Spritzer
CNBS Gelo 25/1 Gelonade
enua 25/1 AFSC CA Animal Face Sherb Crasher
All Nations FG 25/1 Frosted Gelato
Vasco PR PT Pave Runtz
Roxton Air FC Frosted Cookies
Green Karat MG PT Modified Gas
Khiron GK 24/1 Green Knight
Cannamedical Sativa forte NM Wedding Tree
Remexian 24/1 GRG Grape Galena
Cannamedical CM 24/1 PG Platinum Grapes
Ceres No. 4 Top 5
Barongo 24/1 Banjo
avaay 24/1 BPM Baby Pam
Big Dreams 24/1 PSF BAA Baked Animal
Medicus 24/1 EVS Godfather Biscotti
Ceres NO. 5 25/1 Super Boof
avaay 23/1 RG Royal Gorilla
avaay 21/1 BKR Black Krush
Sibanax MCF 23/1 Mac Fem
avaay Signature 23/1 MC Mandarin Cookies
Wellford Aquaponic 23/1 PIK Pink Kush
Khiron CK 23/1 Cinderella Kush
All Nations LT 21/1 Lemon Tartz
Tilray THC 25 Spotlight Porto Pink Kush
Navcora THC 22 Spotlight Porto Headband
420 Evolution 22/1 CA MAC
enua 22/1 JFG CA Jet Fuel Gelato
Navcora THC 22 Spotlight Porto Galaxy Walker
enua 22/1 CRO CA Crescendo Cookies
420 Evolution 22/1 CA PLD Plum Driver
BOTANICS Tonic Fuel 22/1 Gary Payton
Canopy Bakerstreet 22/1 Hindu Kush
Huala 22/1 CA ALM Alien Mints
Cannamedical Sativa classic NM Gelato Dream
Cannamedical Hybrid Classic NM Gorilla Zkittlez
Cannamedical Indica Classic NM 22/1 Kerosene Krash
Tweed Glitter Bomb 20/1
madrecan 21/1 Granddaddy OG
Cannamedical Indica classic ZAF Black Cherry Punch
Huala 22/1 CA DOG Chemdog
Blackbird Strong Sativa Euforia
Cannamedical Sativa classic AU Tangie Chem
Cannamedical CM 20/1 LLY Legendary Larry
enua 20/1 ABG CA Sweets

Cannamedical Sativa Classic NM Wedding Tree
Tilray THC 18 Indica Sirius No. 4
AMP Classic 18/1 White Widow
Tilray THC18 Spotlight Porto Jean Guy
madrecan 18/1 RCH Remo Chemo
Beacon BT T18 Black Triangle
Tilray THC 18 Spotlight Porto Jack Herer
NICE 18/1 CC Cookies & Cream
Cannamedical Hybrid light NM Casey Jones
"""

    _text_list = _text_list.strip()
    _text_list = _text_list.split("\n")
    for _product in _text_list:
        _product = _product.strip()
        Product.objects.update_or_create(name=_product)
