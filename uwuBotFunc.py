# functions for uwuBot

def EngToUwu(string):
    import re as re
    
    """
    Converts a string from english to uwu
    input: string - a string in english
    output: out - the transformed string in uwu
    """
    out = string.casefold()
   
    #replace words first
    out = out.replace("your", "ur")
    out = out.replace("you", "chu") #changed my mind, 'chu' sounds better than 'uwu'
    out = out.replace("to", "two")
    out = out.replace("love", "wuv")
    out = out.replace("this", "dis").replace("there", "dewe")
    out = out.replace(" the ", " teh ")
    out = out.replace("what", "wat")
    out = out.replace("wife", "waifu")
    
    #then replace misc letters
    out = out.replace("r", "w").replace("l", "w")
    out = out.replace("tt","dd")
    out = out.replace("!", " owo!")
    out = out.replace("'", "")
    
    #todo: adjust so ur !-> uw
    out = re.sub(r" uw ", r" ur ", out, flags=re.IGNORECASE)
    #todo: insert w after u if there's another vowel graduated -> graduwated
    out = re.sub(r"u([a|e|i|o|u])", r"uw\1", out, flags=re.IGNORECASE)
    #todo: insert y into na, ne, no, nu but trained !-> trainyed
    out = re.sub(r"\bn([a|e|i|o|u])", r" ny\1", out)

    return out

if __name__ == "__main__":
    test = """What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.

I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.

You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.

Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.

But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it.

You’re fucking dead, kiddo.\n"""
    test2 = """I’ll have you know I graduated top of my class in the Navy Seals...and your IP is being traced right now so you better prepare for the storm,"""
    print(test2)
    print()
    print(EngToUwu("I have been trained at your graduated network in uranium"))