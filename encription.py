def encription(user_variable):
    encription_txt={"a":"b",
        "b":"c",
        "c":"d",
        "e":"f",
        "f":"g",
        "g":"h",
        "i":"j",
        "j"
        "g":"k",
        "k":"l",
        "l":"m",
        "m":"n",
        "n":"o",
        "o":"p",
        "p":"q",
        "q":"r",
        "r":"s",
        "s":"t",
        "t":"u",
        "u":"v",
        "v":"w",
        "w":"x",
        "x":"y",
        "y":"z",
        "z":"0"}
    string=""
    for i in user_variable:
        if encription_txt.get(i)!=None:
            string+=encription_txt.get(i)    
    return string
string="sanjeev"

print(encription(string))
