#!/usr/bin/env python3
"""Foreguild v2 financial model. All figures are planning assumptions, not observed results.
Run: python3 model.py  -> writes model.csv and prints annual summary.
"""
import csv, json

MONTHS = 36

def ramp(vals, n=MONTHS):
    assert len(vals) == n
    return vals

# --- base drivers ---------------------------------------------------------
principal_contracts = ramp([
    1,1,2,2,3,3,4,5,5,6,7,8,                 # Y1 = 47
    7,8,9,10,11,12,13,14,15,16,17,18,        # Y2 = 150
    22,23,24,25,26,27,28,29,30,31,32,33,     # Y3 = 330
])
avg_contract = ramp([5000]*12 + [5500]*12 + [6000]*12)
board_gmv = ramp([
    10000,12000,15000,18000,22000,28000,35000,45000,55000,70000,85000,100000,
    150000,160000,170000,180000,190000,200000,210000,220000,230000,240000,250000,260000,
    400000,430000,460000,490000,520000,550000,580000,610000,640000,670000,700000,750000,
])
# guarantee attach on Foreguild board + external guaranteed value
board_attach = ramp([0.25]*12 + [0.40]*12 + [0.50]*12)
external_guaranteed = ramp([
    25000]*12 + [125000]*12 + [333333]*12)

# product economics
principal_direct = 0.64          # worker + rework + verification + payment
board_fee = 0.09
board_verif = 0.018
board_pay = 0.004
guarantee_premium = 0.06
guarantee_claims = 0.028
guarantee_verif = 0.006
api_price = 1.00
api_cost = 0.30
api_checks = ramp([
    2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,
    15000,17000,19000,21000,23000,25000,27000,29000,31000,33000,35000,37000,
    40000,45000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,
])
float_yield = 0.04
data_rev = ramp([0]*12 + [5000]*12 + [15000]*12)

fixed = ramp([25000]*12 + [54167]*12 + [112500]*12)
headcount = ramp([2]*12 + [6]*12 + [12]*12)
reserve_ratio_target = 1.5
capital_charge_rate = 0.08

rows=[]
cum=0.0
for i in range(MONTHS):
    pc = principal_contracts[i]
    principal_gross = pc * avg_contract[i]
    principal_net = principal_gross * (1-principal_direct)
    board_fee_rev = board_gmv[i]*board_fee
    board_net = board_gmv[i]*(board_fee-board_verif-board_pay)
    guaranteed = board_gmv[i]*board_attach[i] + external_guaranteed[i]
    g_prem = guaranteed*guarantee_premium
    g_claims = guaranteed*guarantee_claims
    g_verif = guaranteed*guarantee_verif
    g_net = g_prem-g_claims-g_verif
    api_gross = api_checks[i]*api_price
    api_net = api_checks[i]*(api_price-api_cost)
    # float: 20% of annualised board GMV + claims reserve
    reserve = guaranteed*guarantee_claims*3*reserve_ratio_target  # 90-day expected claims x 1.5
    float_base = board_gmv[i]*12*0.20 + guaranteed*guarantee_claims*reserve_ratio_target  # float on average monthly reserve
    float_rev = float_base*float_yield/12
    gross_rev = principal_gross + board_fee_rev + g_prem + api_gross + float_rev + data_rev[i]
    net_rev = principal_net + board_net + g_net + api_net + float_rev + data_rev[i]
    ebitda = net_rev - fixed[i]
    cum += ebitda
    rows.append(dict(month=i+1, year=i//12+1, principal_contracts=pc,
        principal_gross=principal_gross, principal_net=principal_net,
        board_gmv=board_gmv[i], board_net=board_net,
        guaranteed=guaranteed, guarantee_premium=g_prem, guarantee_claims=g_claims,
        guarantee_net=g_net, api_gross=api_gross, api_net=api_net,
        float_rev=float_rev, data_rev=data_rev[i],
        gross_rev=gross_rev, net_rev=net_rev, fixed=fixed[i], ebitda=ebitda,
        cum_ebitda=cum, reserve=reserve, headcount=headcount[i],
        loss_ratio=g_claims/g_prem if g_prem else 0))

# annual summary
years={}
for y in (1,2,3):
    rs=[r for r in rows if r['year']==y]
    years[y]={k:sum(r[k] for r in rs) for k in
        ['principal_contracts','principal_gross','principal_net','board_gmv','board_net',
         'guaranteed','guarantee_premium','guarantee_claims','guarantee_net','api_gross','api_net',
         'float_rev','data_rev','gross_rev','net_rev','fixed','ebitda']}
    years[y]['ending_cum']=rs[-1]['cum_ebitda']
    years[y]['ending_reserve']=rs[-1]['reserve']
    years[y]['headcount']=rs[-1]['headcount']
    years[y]['loss_ratio']=years[y]['guarantee_claims']/years[y]['guarantee_premium']
    years[y]['net_margin']=years[y]['ebitda']/years[y]['net_rev']

print(json.dumps(years, indent=2))

with open('model.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['month','year','principal_contracts','principal_gcv','principal_net','board_gmv','board_net',
        'guaranteed_value','guarantee_premium','guarantee_claims','guarantee_net','api_checks','api_gross','api_net',
        'float_rev','data_rev','gross_revenue','net_revenue','fixed_cost','ebitda','cum_ebitda','reserve','headcount','loss_ratio'])
    for r in rows:
        w.writerow([r['month'],r['year'],r['principal_contracts'],round(r['principal_gross']),round(r['principal_net']),
            round(r['board_gmv']),round(r['board_net']),round(r['guaranteed']),round(r['guarantee_premium']),
            round(r['guarantee_claims']),round(r['guarantee_net']),api_checks[r['month']-1],round(r['api_gross']),
            round(r['api_net']),round(r['float_rev']),r['data_rev'],round(r['gross_rev']),round(r['net_rev']),
            round(r['fixed']),round(r['ebitda']),round(r['cum_ebitda']),round(r['reserve']),r['headcount'],
            round(r['loss_ratio'],4)])
print('wrote model.csv')

# break-even month (first month ebitda>0)
be=next((r['month'] for r in rows if r['ebitda']>0), None)
print('first EBITDA-positive month:',be)
print('max cash trough:',round(min(r['cum_ebitda'] for r in rows)))

# --- scenarios ------------------------------------------------------------
def scenario(vol=1.0, claims=0.028, fixed_mult=1.0, api_mult=1.0, price_mult=1.0):
    out={}
    for y in (1,2,3):
        rs=[r for r in rows if r['year']==y]
        pc=sum(r['principal_contracts'] for r in rs)*vol
        pg=sum(r['principal_gross'] for r in rs)*vol*price_mult
        pn=pg*(1-principal_direct)
        bg=sum(r['board_gmv'] for r in rs)*vol*price_mult
        bn=bg*(board_fee-board_verif-board_pay)
        gv=sum(r['guaranteed'] for r in rs)*vol*price_mult
        gp=gv*guarantee_premium
        gc=gv*claims
        gn=gp-gc-gv*guarantee_verif
        an=sum(r['api_net'] for r in rs)*api_mult
        fl=sum(r['float_rev'] for r in rs)
        dr=sum(r['data_rev'] for r in rs)*vol
        nr=pn+bn+gn+an+fl+dr
        fx=sum(r['fixed'] for r in rs)*fixed_mult
        out[y]=dict(contracts=round(pc),gcv=round(pg),board=round(bg),guaranteed=round(gv),
            gross=round(pg+bg*board_fee+gp+an/(1-api_cost/api_price)+fl+dr),net=round(nr),fixed=round(fx),
            ebitda=round(nr-fx),loss_ratio=round(gc/gp,3) if gp else 0)
    return out
print('BEAR',json.dumps(scenario(vol=0.55,claims=0.065,fixed_mult=0.85,api_mult=0.60,price_mult=0.95),indent=2))
print('BULL',json.dumps(scenario(vol=1.35,claims=0.022,fixed_mult=1.10,api_mult=1.25,price_mult=1.05),indent=2))
