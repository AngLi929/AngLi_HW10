POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

RR_STROKE = 0.65

RR_BLEEDING = 1.05

# annual cost of each health state
ANNUAL_STATE_COST = [
    0,
    5000,
    200
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1,
    0.8865,
    0.9
    ]


ANNUAL_COST= [
    0,
    0,
    0,
    0]


ANTI_ANNUAL_COST= [
    0,
    0,
    2000,
    0]
