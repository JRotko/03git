import postinumerot

TESTIDATA = {
    "00240": "HELSINKI",
    "11223": "TURKU",
    "00100": "HELSINKI",
    "12345": "SIPOO"
}

SMARTPOST = {
    "00700": "SMARTPOST",
    "00800": "SMART POST",
    "00900": "SMART-POST"
}

def test_monta_postinumeroa():
    data = postinumerot.ryhmittele_toimipaikoittain(TESTIDATA)

    assert len(data["HELSINKI"]) == 2


def test_yksi_postinumero():
    data = postinumerot.ryhmittele_toimipaikoittain(TESTIDATA)

    assert len(data["TURKU"]) == 1

def test_yksi_smartpost():
   data = postinumerot.ryhmittele_toimipaikoittain(SMARTPOST)

   assert len(data) == 1 
   assert len(data["SMARTPOST"]) == 3