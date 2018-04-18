import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov



cohort_notherapy = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_NO = cohort_notherapy.simulate()

cohort_therapy = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_THERAPY = cohort_therapy.simulate()

SupportMarkov.print_outcomes(simOutputs_NO, "No Therapy:")
SupportMarkov.print_outcomes(simOutputs_THERAPY, "Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_NO, simOutputs_THERAPY)

SupportMarkov.report_CEA_CBA(simOutputs_NO, simOutputs_THERAPY)
