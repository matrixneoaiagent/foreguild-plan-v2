#!/usr/bin/env python3
"""Generate inline SVG charts for the Foreguild v2 plan. No external assets."""
import os

INK="#12211d"; MUTED="#5d6b64"; LINE="#d8d2c4"; PAPER="#fbf8f0"
RUST="#c8552f"; GREEN="#2f7d68"; GOLD="#d9a441"; SAND="#e9e2d2"; SLATE="#3f5a52"

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def txt(x,y,s,size=13,fill=INK,anchor="start",weight="400",family="ui-sans-serif,system-ui,sans-serif"):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{esc(s)}</text>'

def rect(x,y,w,h,fill,stroke="none",rx=0,opacity=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" rx="{rx}" opacity="{opacity}"/>'

def line(x1,y1,x2,y2,stroke=LINE,w=1,dash=""):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}"{d}/>'

# ---------- chart 1: net revenue build ----------
def chart_rev():
    W,H=860,380; L,R,T,B=70,30,30,70
    data={"Y1": [84.6,33.7,11.0,63.0,4.0], "Y2":[297.0,167.3,64.6,218.4,80.0], "Y3":[712.8,462.4,192.4,567.0,235.4]}
    labels=["Principal contracts","Board take","Guarantee premium","Verify API","Float + data"]
    colors=[INK,GREEN,RUST,GOLD,MUTED]
    maxv=2400; plot_h=H-T-B; plot_w=W-L-R
    def y(v): return T+plot_h-(v/maxv)*plot_h
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Net revenue build by product, years 1 to 3">']
    s.append(rect(0,0,W,H,"#fffdf8"))
    for g in range(0,2500,500):
        s.append(line(L,y(g),W-R,y(g),LINE,1))
        s.append(txt(L-10,y(g)+4,f"${g/1000:.1f}M" if g>=1000 else f"${g}k",11,MUTED,"end"))
    bw=110; xs=[160,390,620]
    for x,(yr,vals) in zip(xs,data.items()):
        acc=0
        for v,c in zip(vals,colors):
            if v<=0: continue
            h=(v/maxv)*plot_h
            s.append(rect(x,y(acc+v),bw,h,c))
            if v>=40:
                s.append(txt(x+bw/2,y(acc+v)+h/2+4,f"{v:.0f}",11,"#fff","middle","700"))
            acc+=v
        s.append(txt(x+bw/2,H-B+22,yr,13,INK,"middle","700"))
        s.append(txt(x+bw/2,H-B+40,f"${acc:.0f}k net",11,MUTED,"middle"))
    # legend
    lx=70; ly=H-18
    for lab,c in zip(labels,colors):
        s.append(rect(lx,ly-8,10,10,c))
        s.append(txt(lx+15,ly,lab,10,MUTED))
        lx+=150
    s.append(txt(W-R,T-8,"Net revenue after worker pay, claims, verification and payment costs",10,MUTED,"end"))
    s.append("</svg>")
    return "".join(s)

# ---------- chart 2: EBITDA and cumulative cash ----------
def chart_ebitda():
    W,H=860,380; L,R,T,B=70,30,40,70
    ebitda=[-103.7,177.3,820.0]; cum=[-103.7,73.6,893.6]
    maxv=1000; minv=-200; plot_h=H-T-B; plot_w=W-L-R
    def y(v): return T+plot_h-((v-minv)/(maxv-minv))*plot_h
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="EBITDA and cumulative cash by year">']
    s.append(rect(0,0,W,H,"#fffdf8"))
    for g in range(-200,1001,200):
        s.append(line(L,y(g),W-R,y(g),LINE,1))
        s.append(txt(L-10,y(g)+4,f"${g}k",11,MUTED,"end"))
    zero=y(0); s.append(line(L,zero,W-R,zero,INK,1.4))
    bw=90; xs=[200,420,640]
    for x,v in zip(xs,ebitda):
        top=min(y(v),zero); h=abs(y(v)-zero)
        s.append(rect(x-bw/2,top,bw,h,GREEN if v>=0 else RUST))
        if v>=0:
            s.append(txt(x,top+24,f"+${abs(v):.0f}k",12,"#fff","middle","700"))
        else:
            s.append(txt(x,top+h+16,f"−${abs(v):.0f}k",12,RUST,"middle","700"))
        s.append(txt(x,H-B+22,f"Year {xs.index(x)+1}",12,INK,"middle","700"))
    pts=" ".join(f"{x},{y(v)}" for x,v in zip(xs,cum))
    s.append(f'<polyline points="{pts}" fill="none" stroke="{GOLD}" stroke-width="3"/>')
    for x,v in zip(xs,cum):
        s.append(f'<circle cx="{x}" cy="{y(v)}" r="4.5" fill="{GOLD}" stroke="#fff" stroke-width="1.5"/>')
        s.append(txt(x+12,y(v)-10,f"${v:.0f}k",11,GOLD,"start","700"))
    # legend
    s.append(rect(70,H-18,10,10,GREEN)); s.append(txt(85,H-9,"EBITDA",10,MUTED))
    s.append(line(150,H-13,170,H-13,GOLD,3)); s.append(txt(176,H-9,"cumulative EBITDA",10,MUTED))
    s.append(txt(W-R,T-8,"Base case; negative EBITDA funded from the seed and prize",10,MUTED,"end"))
    s.append("</svg>")
    return "".join(s)

# ---------- chart 3: loss ratio waterfall ----------
def chart_loss():
    W,H=860,220; L,R,T,B=70,30,44,54
    parts=[("Claims",46.7,RUST),("Verification",10.0,GOLD),("Payment + fixed",10.0,SLATE),("Underwriting margin",33.3,GREEN)]
    total=100.0; plot_w=W-L-R
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Guarantee premium waterfall: combined ratio 66.7 percent, margin 33.3 percent">']
    s.append(rect(0,0,W,H,"#fffdf8"))
    x=L
    for lab,v,c in parts:
        w=(v/total)*plot_w
        s.append(rect(x,T,w,50,c))
        if v>5:
            s.append(txt(x+w/2,T+30,f"{v:.1f}%",12,"#fff","middle","700"))
        s.append(txt(x+w/2,T+70,lab,10,MUTED,"middle"))
        x+=w
    gx=L+0.85*plot_w
    s.append(line(gx,T-10,gx,T+58,INK,2,"4 3"))
    s.append(txt(gx,T-18,"85% guardrail",10,INK,"middle","700"))
    s.append(txt(L,H-12,"Every $100 of guarantee premium: $46.7 claims, $10 verification, $10 payment + fixed, $33.3 underwriting margin.",10,MUTED))
    s.append("</svg>")
    return "".join(s)

# ---------- chart 4: futarchy market structure ----------
def chart_fut():
    W,H=860,430
    s=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Seer parent market and two conditional scalar markets on RAC90">']
    s.append(rect(0,0,W,H,"#fffdf8"))
    # parent
    s.append(rect(270,26,320,76,"#fff",INK,2))
    s.append(txt(430,50,"PARENT · binary",10,MUTED,"middle","700"))
    s.append(txt(430,72,"Will FIP-2027-03 be adopted?",13,INK,"middle","700"))
    s.append(txt(430,118,"7-day trade · 72h TWAP · Reality.eth + Kleros",10,MUTED,"middle"))
    # branches
    s.append(line(430,132,430,150,INK,2))
    s.append(line(200,150,660,150,INK,2))
    s.append(line(200,150,200,172,INK,2)); s.append(line(660,150,660,172,INK,2))
    s.append(rect(70,172,260,120,"#eef6f2",GREEN,2))
    s.append(txt(200,196,"YES branch · scalar",10,GREEN,"middle","700"))
    s.append(txt(200,218,"What will RAC90 be if",12,INK,"middle"))
    s.append(txt(200,236,"FIP-03 is adopted?",12,INK,"middle"))
    s.append(txt(200,262,"range −$500k … +$2M",10,MUTED,"middle"))
    s.append(rect(530,172,260,120,"#fbeee9",RUST,2))
    s.append(txt(660,196,"NO branch · scalar",10,RUST,"middle","700"))
    s.append(txt(660,218,"What will RAC90 be if",12,INK,"middle"))
    s.append(txt(660,236,"FIP-03 is not adopted?",12,INK,"middle"))
    s.append(txt(660,262,"range −$500k … +$2M",10,MUTED,"middle"))
    # decision rule
    s.append(rect(180,306,500,54,"#fff",INK,2))
    s.append(txt(430,328,"ADOPT iff YES TWAP > NO TWAP by 5%",12,INK,"middle","700"))
    s.append(txt(430,346,"and liquidity ≥ $5,000 and ≥ 20 unique traders",10,MUTED,"middle"))
    # resolution
    s.append(line(430,360,430,382,GOLD,2))
    s.append(f'<polygon points="430,390 424,380 436,380" fill="{GOLD}"/>')
    s.append(txt(430,410,"Audited RAC90 report → hash anchored on Base → Reality.eth → Kleros appeal",10,MUTED,"middle"))
    s.append("</svg>")
    return "".join(s)

for name,fn in [("chart_rev.svg",chart_rev),("chart_ebitda.svg",chart_ebitda),("chart_loss.svg",chart_loss),("chart_fut.svg",chart_fut)]:
    open(name,"w").write(fn())
    print("wrote",name,len(fn()))
