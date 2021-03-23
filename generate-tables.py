import pandas as pd 

df = pd.read_excel("/Users/rithvikrao/Desktop/list.xlsx")

# date = "3/26/2021"
# time = "10:30 AM to 12:15 PM ET"
# sessions = ["Special 1"]

# date = "3/26/2021"
# time = "2:15 PM to 4:00 PM ET"
# sessions = ["Special 2"]

# date = "3/27/2021"
# time = "10:30 AM to 12:20 PM ET"
# sessions = ["IO 1", "Network Formation", "Network Games 1"]

# date = "3/27/2021"
# time = "2:40 PM to 4:00 PM ET"
# sessions = ["Financial Networks 1", "Peer Effects", "Technology Applications"]

# date = "3/28/2021"
# time = "10:30 AM to 11:50 AM ET"
# sessions = ["Development", "Econometrics: Theory", "Learning 1"]

# date = "3/28/2021"
# time = "12:30 PM to 1:50 PM ET"
# sessions = ["Econometrics: Applied", "IO 2", "Network Games 2"]

date = "3/28/2021"
time = "2:40 PM to 4:00 PM ET"
sessions = ["Financial Networks 2", "Learning 2", "Production Networks"]

mapping = {0: "Nashville", 1: "Bloomington", 2: "Stanford"}

selection = df[(df['Date'] == date) & (df['Time'] == time)]

for i, session in enumerate(sessions):
    print(f"""<td style="width:27%;"valign="top">""")
    if len(sessions) == 3:
        print(f"""  <u><strong>{session} ({mapping[i]})</strong></u><ul>""")
    else:
        print(f"""  <u><strong>{session}</strong></u><ul>""")
    selec_sess = selection[selection['Session'] == session].sort_values(by=['Paper Order'])
    for index, row in selec_sess.iterrows():
        authors = row['Author Names and Affiliations']
        title = row['Title']
        paper_link = row['Paper Link']
        additional_link = row['Additional Links']
        abstract = row['Abstract']
        print(f"""  <li><strong>{title}</strong> <br><i>{authors}</i></li>""")
        if paper_link == paper_link:
            if additional_link == additional_link: 
                print(f"""  <a href="{paper_link}">Paper Link</a> | <a href="{additional_link}">Additional Link</a>""")
            else:
                print(f"""  <a href="{paper_link}">Paper Link</a>""")
        print(f"""  <button type="button" class="collapsible">Abstract</button>""")
        print(f"""  <div class="content2" style="font-size:12px">""")
        print(f"""    {abstract}""")
        print(f"""  </div>""")
    print(f"""</ul></td>""")

