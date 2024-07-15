from pretty_html_table import build_table
from database.db import get_active, get_data, countdown
from modules.email import email_events

df = get_data()
df['Action'] = df.apply(lambda row: get_active(row), axis=1)
df = df[df['Action'] == 'Action']
df['Weeks'] = df.apply(lambda row: countdown(row)[0], axis=1)
df['Days'] = df.apply(lambda row: countdown(row)[1], axis=1)
cols = ['Event', 'Weeks', 'Days']
df = df.loc[:, cols]
df = df.sort_values(by=['Weeks', 'Days'], ascending=[True, True])

events_html = build_table(
    df,
    "orange_light",
    text_align="right",
    font_family="Sans-Serif",
    font_size="14px",
    width="300px",
)

email_events(['simon@muddypaws.net', 'alison@muddypaws.net'], events_html)