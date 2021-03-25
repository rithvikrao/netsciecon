import pandas as pd 

df = pd.read_excel("/Users/rithvikrao/Desktop/list.xlsx")

# date = "3/26/2021"
# sessions = ["Applied and Experimental Misc", "Beliefs", "Methodology and Statistics", "Production and Financial Networks"]

date = "3/27/2021"
sessions = ["Applied Micro", "Econometrics", "Network Formation", "Peer Effects"]

selection = df[(df['Date'] == date) & (df['Poster or Open'] == "Poster")]

for i, session in enumerate(sessions):
    print(f"""  <u style="font-size:16px"><strong>{session}</strong></u><ul>""")
    selec_sess = selection[selection['Session'] == session].sort_values(by=['Paper Order'])
    for index, row in selec_sess.iterrows():
        authors = row['Author Names and Affiliations']
        title = row['Title']
        paper_link = row['Paper Link']
        additional_link = row['Additional Links']
        abstract = row['Abstract']
        print(f"""  <li style="font-size:16px"><strong>{title}</strong> <br><i>{authors}</i>""")
        if paper_link == paper_link:
            if additional_link == additional_link: 
                print(f"""  <a href="{paper_link}">Paper Link</a> | <a href="{additional_link}">Additional Link</a></li>""")
            else:
                print(f"""  <a href="{paper_link}">Paper Link</a></li>""")
        print(f"""  <button type="button" class="collapsible">Abstract</button>""")
        print(f"""  <div class="content2" style="font-size:12px">""")
        print(f"""    {abstract}""")
        print(f"""  </div>""")
    print(f"""</ul></td>""")

