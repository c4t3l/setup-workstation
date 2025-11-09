# Elisa config notes

All config is stored in a sqlite3 db.  See session dump below.

## Sqlite session dump

```
sqlite> .show 
        echo: off
         eqp: off
     explain: auto
     headers: off
        mode: list
   nullvalue: ""
      output: stdout
colseparator: "|"
rowseparator: "\n"
       stats: off
       width: 
    filename: elisaDatabase.db
sqlite> .databases
main: /home/rcallicotte/.local/share/elisa/elisaDatabase.db r/w
sqlite> .tables
Albums              DatabaseVersion     Genre               Tracks            
Artists             DatabaseVersionV15  Lyricist            TracksData        
Composer            DiscoverSource      Radios            
sqlite> .tables Radios
Radios
sqlite> select * from Radios
   ...> ;
1|https://ouifm.ice.infomaniak.ch/ouifm-high.mp3||OuiFM_Classic_Rock|0||
2|https://ouifmrock70s.ice.infomaniak.ch/ouifmseventies.mp3||OuiFM_70s|0||
3|https://jazzradio.ice.infomaniak.ch/jazzradio-high.mp3||Jazz_Radio|0||
6|http://sc-classrock.1.fm:8200||Classic rock replay|0||
7|https://quincy.torontocast.com:1925/stream||Instrumentals Forever|0||
8|https://stream.laut.fm/jahfari||Jahfari|0||
9|https://ice1.somafm.com/groovesalad-256.mp3|https://somafm.com/img/groovesalad120.png|SomaFM - Groove Salad|0||
10|https://ice1.somafm.com/dronezone-256.mp3|https://somafm.com/img/dronezone120.jpg|SomaFM - Drone Zone|0||
11|https://ice1.somafm.com/deepspaceone-128.mp3|https://somafm.com/img/deepspaceone120.gif|SomaFM - Deep Space One|0||
12|https://ice1.somafm.com/u80s-256-mp3|https://somafm.com/img/u80s-120.png|SomaFM - Underground 80s|0||
13|https://ice1.somafm.com/synphaera-256-mp3|https://somafm.com/img3/synphaera120.jpg|SomaFM - Synphaera Radio|0||
14|https://ice1.somafm.com/defcon-256-mp3|https://somafm.com/img/defcon120.png|SomaFM - DEF CON Radio|0||
15|https://ice1.somafm.com/dubstep-256-mp3|https://somafm.com/img/dubstep120.png|SomaFM - Dub Step Beyond|0||
16|https://ice1.somafm.com/vaporwaves-128-mp3|https://somafm.com/img/vaporwaves120.jpg|SomaFM - Vaporwaves|0||
17|https://ice1.somafm.com/missioncontrol-128-mp3|https://somafm.com/img/missioncontrol120.jpg|SomaFM - Mission Control|0||
18|http://ams1.reliastream.com:8054/stream|https://c64radio.com/images/coollogo_com-24210747.png|c64radio.com - The SID Station|0||
19|http://relay1.slayradio.org:8000/|https://www.slayradio.org/styles/default/images/SLAY_Radio_top_log_metal.png|slayradio.org - SLAYRadio|0||
20|https://icecast.radiofrance.fr/francemusique-lofi.mp3|https://static.radio.fr/images/broadcasts/07/f7/3366/c44.png|France Musique|0||
21|https://localradio.streamb.live/SB00349?args=web_01&starttime=1762667604|https://media-cdn.socastsrm.com/wordpress/wp-content/blogs.dir/3310/files/2024/11/indie-88-logo-ko.png|Indy 88 Toronto|0||
22|https://ice1.somafm.com/tikitime-64-aac|https://api.somafm.com/logos/256/tikitime256.jpg|SomaFM - Tiki Time|0||
23|https://ice6.somafm.com/7soul-64-aac|https://api.somafm.com/logos/256/7soul256.png|SomaFM - Seven Inch Soul|0||
24|https://ice1.somafm.com/sonicuniverse-64-aac|https://api.somafm.com/logos/256/sonicuniverse256.png|SomaFM - Sonic Universe|0||
25|https://ice4.somafm.com/deptstore-64-aac|https://api.somafm.com/logos/256/deptstore256.png|SomaFM - Department Store Christmas|0||
```
