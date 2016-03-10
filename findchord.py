import urllib, cStringIO
from bs4 import BeautifulSoup

chordName = raw_input("What chord do you need?")

url = 'http://www.ukulele-chords.com/get?ak=d41d8cd98f00b204e9800998ecf8427e&r=' + chordName + '&typ=major'
chordResponse = urlopen(url).read()
soup = BeautifulSoup('chord_diag','xml')

f = open(soup,'w')
