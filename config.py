OPENAI_TOKEN = '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'

STOP_PROMPT = "\n\n###\n\n"
STOP_COMPLETION = "\nEND\n"

TOKEN_LIMIT = 2000

PROMPT_DESC = {
    "v1": "Customizable Serial Dilution for OT-2",
    "v2": "Customizable Serial Dilution for OT-2",
    "v3": "Genric sample plating protocol ",
    "v4":  "Glycerol Stock"
    
 }

PROMPT_LIST = {
    # simple Serail Dilution for OT -2 
    # long prompt
    "v1": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a script that does the following experiment?

a simple serial dilution across a 96-well plate using a single-channel. 

{STOP_PROMPT}
""",
"v2": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a script that does the following experiment?

a simple serial dilution across a 96-well plate using a 8-channel pipette. 

{STOP_PROMPT}
""",
"v3": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a script that does the following experiment?

Plating samples from custom or standard tuberacks to a NEST 96-deepwell plate. 10µl proteinase K and 10µl internal control are then added to each sample. 
Samples are transferred to the plate first down each column, then across each row (A1, B1, C1, …H1, A2, B2, C2, etc.)

{STOP_PROMPT}
""",

"v4": f"""
I want to write a Python script that runs Opentrons machine. This robot can be used to automate laboratory experiment, and is used by many researchers in biology.

Can you write down a script that does the following experiment?

This is a flexible protocol for making glycerol stocks of E. coli cultures for long-term storage in a -80C freezer. The protocol expects that you've grown the strains in liquid culture to an acceptable optical density, and prepared a sterile solution of 50% glycerol, 50% deionized water.

The protocol loads 500ul of liquid culture and 500ul of glycerol into a cryo tube, which you should then cap, label, and store in your -80C freezer. By default, 3 replicates of each strain are made. The number of samples and the number of replicates can be changed and the protocol will 
automatically calculate the number of cryo tubes you need. The protocol will throw an error there are too many samples to fit on the deck.

{STOP_PROMPT}
""",

}
