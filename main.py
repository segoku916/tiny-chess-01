import json as j,os,urllib.request as u
E=os.environ['MAKEFUN_ENV_URL']
def P(p,b):return j.load(u.urlopen(E+p,j.dumps(b).encode()))
VL=[0,100,320,330,500,900,0]
NK=(33,31,18,14,-14,-18,-31,-33);KG=(1,-1,16,-16,15,17,-15,-17);BS=KG[4:];DT=(NK,BS,KG[:4],KG,KG)
z=9;ZB=[]
for _ in range(2049):
 z=z*6364136223846793005+1&(1<<64)-1;ZB.append(z)
SN=['abcdefgh'[i&7]+str((i>>4)+1)for i in range(128)]
PS=[[VL[t]]*128 for t in range(7)]
for r in range(8):
 for f in range(8):
  i=r*16+f;c=min(f,7-f)+min(r,7-r)
  PS[1][i]+=5*r
  for t in(2,3,5):PS[t][i]+=4*c-10
  PS[6][i]=25-15*r+10*(f in(2,6))
TT={}
def A(x):return SN.index(x[:2])|SN.index(x[2:4])<<7|(('nbrq'.index(x[4])+2)<<14 if len(x)>4 else 0)
def W(m):return SN[m&127]+SN[m>>7&127]+('nbrq'[(m>>14)-2]if m>>14 else '')
def T(s,o):
 e=o<<3
 for d in((-15,-17),(15,17))[o]+NK:
  t=s+d
  if not(t&136)and B[t]==(1 if abs(d)in(15,17)else 2)|e:return 1
 for d in KG:
  t=s+d
  while not(t&136):
   x=B[t]
   if x:
    if x==(3 if d in BS else 4)|e or x==5|e or x==6|e and t==s+d:return 1
    break
   t+=d
 return 0
def G(c=0):
 m=[];a=m.append
 for f,p in enumerate(B):
  if not p or p>>3!=S:continue
  t=p&7
  if t==1:
   d=16-32*S;r=f>>4;l=6-5*S;g=[]
   o=f+d
   if not B[o]:
    g.append(o)
    if r==1+5*S and not c and not B[o+d]:g.append(o+d)
   for o in(f+d-1,f+d+1):
    if not(o&136)and B[o]and B[o]>>3!=S:g.append(o)
   for o in g:
    if r==l:
     for q in(5,4,3,2):a(f|o<<7|q<<14)
    elif not c or B[o]:a(f|o<<7)
  else:
   for d in DT[t-2]:
    o=f+d
    while not(o&136):
     x=B[o]
     if x:
      if x>>3!=S:a(f|o<<7)
      break
     if not c:a(f|o<<7)
     if t in(2,6):break
     o+=d
   if t==6 and not c and f in(4,116)and not T(f,1-S):
    for d in(1,-1):
     r=f+3 if d>0 else f-4
     if B[r]==4+(S<<3) and not B[f+d]and not B[f+2*d]and not(d<0 and B[f-3])and not T(f+d,1-S)and not T(f+2*d,1-S):a(f|(f+2*d)<<7)
 return m
def MK(m):
 global S,Z
 f=m&127;t=m>>7&127;q=m>>14&7;p=B[f]
 w=t-16+32*S if p&7==1 and not B[t] and abs(t-f)in(15,17)else t
 c=B[w]
 U.append((m,w,c,Z))
 if c:B[w]=0;Z^=ZB[c*128+w]
 B[f]=0;Z^=ZB[p*128+f]
 n=q|(S<<3) if q else p
 B[t]=n;Z^=ZB[n*128+t]
 if p&7==6:
  K[S]=t
  if t-f==2 or f-t==2:
   g=f+3-7*(t<f);h=f+1-2*(t<f);r=B[g];B[g]=0;Z^=ZB[r*128+g];B[h]=r;Z^=ZB[r*128+h]
 S^=1;Z^=ZB[2048]
 if T(K[1-S],S):UM();return 0
 return 1
def UM():
 global S,Z
 m,w,c,Z=U.pop()
 f=m&127;t=m>>7&127;q=m>>14&7
 S^=1
 n=B[t]
 p=1|(S<<3) if q else n
 B[f]=p;B[t]=0
 if p&7==6:
  K[S]=f
  if t-f==2 or f-t==2:
   g=f+3-7*(t<f);h=f+1-2*(t<f);r=B[h];B[h]=0;B[g]=r
 if c:B[w]=c
def EV():
 s=0
 for i,p in enumerate(B):
  if p:
   v=PS[p&7][i^(112*(p>7))]
   s+=(v,-v)[p>7]
 return s*(1-2*S)
def SR(d,a,b,pl):
 global N,AB
 N+=1
 if N>=LIM:AB=1;return 0
 if pl>96:return EV()
 q=d<=0
 k=T(K[S],1-S)
 s=-99999
 if q and not k:
  e=EV()
  if e>=b:return e
  s=e
  if e>a:a=e
 tm=0
 if not q and(e:=TT.get(Z)):
  tm=e[3]
  if e[0]>=d and(e[2]==1 or e[2]==2 and e[1]>=b or e[2]==3 and e[1]<=a):return e[1]
 a0=a;bs=s;bm=0;l=0
 for m in sorted(G(q and not k),key=lambda m:999999 if m==tm else(10000+10*VL[B[m>>7&127]&7]-VL[B[m&127]&7] if B[m>>7&127] else 0),reverse=True):
  if not MK(m):continue
  l+=1
  v=-SR(d-1,-b,-a,pl+1)
  UM()
  if AB:return 0
  if v>bs:bs=v;bm=m
  if v>a:a=v
  if a>=b:break
 if not l:return -99999+pl if k else s*q
 if not q and abs(bs)<99000:TT[Z]=(d,bs,1+2*(bs<=a0)+(bs>=b),bm)
 return bs
def RT(ms):
 global N,AB,LIM
 if len(TT)>2e5:TT.clear()
 N=0;bm=ms[0];od=ms[:]
 for d in range(64):
  AB=0;LIM=150000
  a=-99999;sc={}
  for m in od:
   if not MK(m):sc[m]=-99999;continue
   v=-SR(d,-99999,-a,1)
   UM()
   if AB:break
   sc[m]=v
   if v>a:a=v
  if AB:break
  od.sort(key=sc.get,reverse=True)
  bm=od[0]
 return bm
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  B=[4,2,3,5,6,3,2,4]+[0]*8+[1]*8+[0]*72+[9]*8+[0]*8+[12,10,11,13,14,11,10,12]+[0]*8
  K=[4,116];S=0;Z=15606333317072369408;U=[]
  for x in g['moves']:MK(A(x))
  lm=g['legal_moves']
  v=W(RT([*map(A,lm)]))
  if v not in lm:v=lm[0]
  g=P('/move',{'game':g['game'],'move':v})
