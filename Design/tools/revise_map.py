from pathlib import Path
import json,html
root=Path(__file__).resolve().parents[1]
p=root/'map-layout.json';d=json.loads(p.read_text());d['revision']=2;d['playable_size']=[3200,2800]
rows=[('01','Allied staging',1600,220,500,220),('02','Miller Farm',950,850,500,380),('03','Bell Crossroads',2250,900,480,380),('04','Central bridge',1600,1300,160,120),('05','East ford',2700,1320,200,160),('06','Artillery ridge',1650,1700,700,360),('07','Pine woods',500,1600,600,700),('08','South suburbs',1400,2150,1200,350),('09','Rail yard',2600,2260,650,650),('10','Courthouse',1600,2530,700,400),('11','West bridge',550,1280,160,120)]
d['pois']=[dict(id=i,name=n,center_xy=[x,y],footprint_wh=[w,h]) for i,n,x,y,w,h in rows];d['sector_y_bounds']={'farms':[0,1380],'ridge':[1380,1950],'city':[1950,2800]}
units=[('U1','US rifle squad',750,590),('U2','US rifle squad',1150,620),('U3','US rifle squad',2050,620),('U4','US rifle squad',2450,600),('C1','Canadian section',600,410),('C2','Canadian section',2650,410),('AT1','Antitank team',1350,560),('AT2','Antitank team',1850,560),('S','Scout/sniper team',380,650),('M','Mortar detachment',1600,360),('T1','Sherman',1250,350),('T2','Sherman',1950,350),('TR1','Transport',1400,180),('TR2','Transport',1600,180),('TR3','Transport',1800,180)]
enemies=[('E1',700,1040),('E2',1150,1080),('E3',2100,1100),('E4',2450,1190),('E5',1050,1590),('E6',1600,1520),('E7',2200,1840),('E8',1000,2050),('E9',1750,2070),('E10',2470,2070),('E11',1300,2480),('E12',1900,2550),('AX1',1200,1950),('AX2',2700,2430),('AC',2300,1810),('G1',1350,1720),('G2',1650,1790),('G3',1950,1720),('F1',800,920),('K1',2380,950),('F2',2250,2360),('F3',2000,2400)]
d['allied_deployment']=[dict(id=i,role=r,xy=[x,y]) for i,r,x,y in units];d['enemy_deployment']=[dict(id=i,xy=[x,y]) for i,x,y in enemies]
roads=[[(1600,0),(1600,2800)],[(1600,450),(950,850),(550,1280),(650,1800),(1000,2150),(1150,2530)],[(1600,450),(2250,900),(2700,1320),(2750,1800),(2600,2260),(2250,2550)],[(300,450),(300,1050),(550,1280),(300,1750),(550,2050),(850,2350),(1150,2530),(1600,2700),(2250,2550)],[(2900,450),(2950,1050),(2700,1320),(2950,1800),(2900,2450),(2250,2550)],[(550,720),(950,650),(1600,700),(2250,700),(2750,800)],[(550,1120),(1000,1150),(1600,1120),(2250,1180),(2800,1130)],[(550,1450),(1100,1450),(1600,1500),(2250,1500),(2750,1450)],[(650,1900),(1150,1900),(1650,1950),(2200,1900),(2750,1900)],[(850,2200),(1600,2250),(2600,2260)],[(1150,2530),(1600,2530),(2250,2550)]]
d['road_polylines']=roads
trenches=[('allied',[(500,600),(900,640),(1300,650)]),('allied',[(1900,650),(2300,660),(2700,610)]),('enemy',[(650,1000),(950,1040),(1250,1030)]),('enemy',[(1950,1060),(2250,1090),(2650,1040)]),('enemy',[(1050,1550),(1450,1580),(1950,1550),(2200,1600)]),('enemy',[(850,2030),(1250,2050),(1850,2020)]),('enemy',[(2350,2020),(2700,2050)])]
d['trench_baselines']=[dict(side=s,points=pts) for s,pts in trenches];d['notes']=['Planning view: all enemy placements revealed, gameplay uses fog of war.','No tank-proof continuous trench wall; preserve traffic gaps and crossings.','Reinforcement E4 is farm reserve, E7 ridge reserve, E12 city reserve.','F1 F2 F3 fictional collaborators; K1 Klan auxiliary; AC armored car; AX tanks.']
p.write_text(json.dumps(d,indent=2)+'\n')
# Vector diagram in meters, rendered at 0.35 px/m.
S=.35;ox=90;oy=1080
xy=lambda x,y:(ox+x*S,oy-y*S)
s=['<svg xmlns="http://www.w3.org/2000/svg" width="1300" height="1330" viewBox="0 0 1300 1330">','<rect width="1300" height="1330" fill="#12212b"/>','<style>text{font-family:Arial,sans-serif;fill:#f5ecd6}.label{font-size:14px;font-weight:bold}.small{font-size:13px}</style>','<text x="90" y="40" font-size="27" font-weight="bold">BRIAR COUNTY • FRONT LINE / REVISION 2</text>','<text x="90" y="70" font-size="17">3.2 × 2.8 km • Initial deployment • All units revealed for design review • North ↑</text>','<rect x="90" y="100" width="1120" height="980" fill="#53654e"/>']
def line(pts,col,w,dash=''):
 a=' '.join(f'{xy(x,y)[0]:.1f},{xy(x,y)[1]:.1f}' for x,y in pts);s.append(f'<polyline points="{a}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="{dash}"/>')
for x in range(0,3201,400):line([(x,0),(x,2800)],'#748166',.6)
for y in range(0,2801,400):line([(0,y),(3200,y)],'#748166',.6)
for y in (1380,1950):line([(0,y),(3200,y)],'#ddbe77',1.5,'7 8')
line([(0,1250),(550,1280),(1100,1250),(1600,1300),(2200,1340),(2700,1320),(3200,1280)],'#75b4c7',12)
for road in roads:line(road,'#c5b291',6)
for i,n,x,y,w,h in rows:
 a,b=xy(x-w/2,y+h/2);color='#2e503c' if i=='07' else '#80715a' if i in ('02','03') else '#63716a'
 s.append(f'<rect x="{a}" y="{b}" width="{w*S}" height="{h*S}" rx="5" fill="{color}" fill-opacity=".6" stroke="#e2d2ae"/>')
 cx,cy=xy(x,y);cy=b+45 if i in ('02','03') else b+17
 s.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" class="label">{i} {html.escape(n)}</text>')
for side,pts in trenches:
 z=[]
 for (x,y),(xx,yy) in zip(pts,pts[1:]):
  count=max(2,int(abs(xx-x)/35))
  for k in range(count):
   t=k/count;z.append((x+(xx-x)*t,y+(yy-y)*t+(15 if k%2 else -15)))
 z.append(pts[-1]);line(z,'#14211a',8);line(z,'#6dbbff' if side=='allied' else '#ee8a79',3)
# Communication trenches to rear assembly areas.
for pts in [[(750,620),(720,500),(800,430)],[(1150,640),(1100,510),(1200,420)],[(2050,650),(2000,510),(2100,420)],[(2450,640),(2500,520),(2450,420)]]:line(pts,'#6dbbff',3,'6 3')
# Optional assault loops, not a single highway.
for pts in [[(600,600),(400,850),(550,1120),(950,1150)],[(1150,650),(1350,850),(1250,1120)],[(2050,650),(1850,900),(2100,1180)],[(2500,650),(2820,930),(2600,1150)],[(650,1450),(900,1800),(1150,1900),(1500,1800)],[(2250,1450),(2350,1800),(2200,1900),(1900,1800)],[(1000,2150),(850,2350),(1150,2650),(1550,2650)],[(2600,2260),(2200,2350),(1950,2530)]]:line(pts,'#9edfff',2.5,'8 6')
for pts in [[(700,1040),(950,1150),(1150,1080),(900,950),(700,1040)],[(1050,1590),(1350,1720),(1950,1720),(2200,1620)],[(1000,2050),(1400,2200),(1750,2070),(1300,2100),(1000,2050)]]:line(pts,'#ffb4a2',2,'3 6')
def icon(i,x,y,col):
 a,b=xy(x,y);s.append(f'<rect x="{a-16}" y="{b-10}" width="32" height="20" rx="3" fill="{col}" stroke="#f5ead5"/><text x="{a}" y="{b+4}" text-anchor="middle" font-size="11" font-weight="bold">{i}</text>')
for i,r,x,y in units:icon(i,x,y,'#1b639b')
for i,x,y in enemies:icon(i,x,y,'#9d3e38')
s+=['<text x="90" y="1120" font-size="18">BLUE: AMERICAN / CANADIAN FRONT • RED: OCCUPATION DEFENSES</text>','<text x="90" y="1150" class="small">U = US squad • C = Canadian section • AT = antitank • S = scouts • M = mortar • T = Sherman • TR = transport</text>','<text x="90" y="1175" class="small">E = enemy rifle group • G = artillery • AX = tank • AC = armored car • F = collaborator • K = Klan auxiliary</text>','<text x="90" y="1200" class="small">Zigzags = trenches • Blue dashed = alternate approaches • Red dotted = local patrols • Grid = 400 m</text>','<text x="90" y="1225" class="small">E4 / E7 / E12 are sector reserves. Trench breaks preserve maneuver lanes. Unit icons are not to scale.</text>','<text x="90" y="1250" class="small">Provisional game layout: test sight lines, travel times, crossings and destruction before locking placements.</text>','<path d="M90 1285h175m-175 -5v10m175 -10v10" stroke="#eee5cd" stroke-width="3"/>','<text x="280" y="1290" class="small">500 m</text>','</svg>']
(root/'References/frontline-plan-v2.svg').write_text('\n'.join(s))
