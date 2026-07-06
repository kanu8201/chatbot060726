import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from PIL import Image, ImageFilter
import speech_recognition as sr
from deep_translator import GoogleTranslator

def check(words):
    check = ["what","are","the", "happens","body","when","you","a","for","effects","how","can",
    "your","health","do","to","over","time","early","warning","know","if","my","difference","role","affect"
    "benefits","why","contribute","should","differ","lack","role","someone","reverse","reversed","serious"
    ""]
    filter = [word for word in words if word.lower() not in check]
    return filter
def check_in(words):
    check =["cardiac","PTSD","anemia","water","chronic","stress","prolonged","organ","system","pollution","alcohol"
    "lifestyle","processed food","healthimage","cardiovascular","sleep","virus","viral","bacterial","adult","grown-up"
    "screening","immune","lymphatic","omega-3","musculoskeletal","posture","Mediterranean","anxiety","asthma","age","artial","tumors","bipolardisorder","bronchitisisbron","calciumvitamin","chroniclower","cardiovascual","cognitive","guthealth","glucose","ulcer","kidney","neuropathy","nonmedication","endometriosis","sodium","sugar","metabolism","gestational","glycemic","goutdietary","bowel"]
    filter =[word for word in words if word.lower() in check]
    return filter

def Chronic():
    with open("acute_chronic_illness.txt",'r') as chronicfile:
        x = chronicfile.read()
    return x

def airpol():
  with open("air_pollution_affect.txt",'r') as airpolaffect:
        x = airpolaffect.read()
  return x

def alcohol():
  with open("alcohol_consumption_damage.txt",'r') as alcoholconsumption:
        x = alcoholconsumption.read()
  return x

def anxiety():
  with open("anxiety_disorder_differ.txt",'r') as anxietydisorder:
        x = anxietydisorder.read()
  return x

def asthma():
  with open("asthma_chronic_obstructive.txt",'r') as asthmachronic:
        x = asthmachronic.read()
  return x

def age():
  with open("at_age_should.txt",'r') as atage:
        x = atage.read()
  return x

def artial():
  with open("atrial_fibrillation_its.txt",'r') as artialfibrillation:
        x = artialfibrillation.read()
  return x

def benigntumors():
  with open("benign_malignant_tumors.txt",'r') as tumors:
        x = tumors.read()
  return x

def bipolar():
  with open("bipolar_i_bipolar.txt",'r') as bipolardisorder:
        x = bipolardisorder.read()
  return x

def bronchitis():
  with open("bronchitis_bronchiolitis.txt",'r') as bronchitisisbron:
        x = bronchitisisbron.read()
  return x

def calcium():
  with open("calcium_vitamin_d.txt",'r') as calciumvitamin:
        x = calciumvitamin.read()
  return x

def chroniccause():
  with open("cause_chronic_lower.txt",'r') as chroniclower:
        x = chroniclower.read()
  return x

def cholesterol():
  with open("cholesterol_contribute_cardiovascul.txt",'r') as cardiovascual:
        x = cardiovascual.read()
  return x

def chronicstress():
  with open("chronic_stress_affect.txt",'r') as chronicstress:
        x = chronicstress.read()
  return x

def cognitive():
  with open("cognitive_behavioral_therapy.txt",'r') as cognitive_behavioral:
        x = cognitive_behavioral.read()
  return x

def commonchronic():
  with open("common_causes_chronic.txt",'r') as commonchronic:
        x = commonchronic.read()
  return x

def clinical():
  with open("common_symptoms_clinical.txt",'r') as clinicalsymptoms:
        x = clinicalsymptoms.read()
  return x

def commonasthma():
  with open("common_triggers_asthma.txt",'r') as asthmatriggers:
        x = asthmatriggers.read()
  return x

def gut():
  with open("connection_gut_health.txt",'r') as guthealth:
        x = guthealth.read()
  return x

def glucose():
  with open("continuous_glucose_monitors.txt",'r') as glucosemonitors:
        x = glucosemonitors.read()
  return x

  def crohns():
   with open("crohns_disease_ulcerative.txt",'r') as ulcerative:
        x = ulcerative.read()
  return x

def kidney():
  with open("diabetes_affect_kidney.txt",'r') as kidneydiabetes:
        x = kidneydiabetes.read()
  return x

def neuropathy():
  with open("diabetic_neuropathy_its.txt",'r') as neuropathydiabetic:
        x = neuropathydiabetic.read()
  return x

def fiber():
  with open("dietary_fiber_support.txt",'r') as fibersupport:
        x = fibersupport.read()
  return x

  def habits():
   with open("dietary_habits_reduce.txt",'r') as habitsreduce:
        x = habitsreduce.read()
  return x

def undiagnosed():
  with open("early_symptoms_undiagnosed.txt",'r') as undiagnosedsymptoms:
        x = undiagnosedsymptoms.read()
  return x

def warning():
  with open("early_warning_signs.txt",'r') as warningsigns:
        x = warningsigns.read()
  return x

def nonmedication():
  with open("effective_nonmedication_strategies.txt",'r') as nonmedicationstrategies:
        x = nonmedicationstrategies.read()
  return x

def vegan():
  with open("effects_vegan_diet.txt",'r') as vegandiet:
        x = vegandiet.read()
  return x

def eatingdisorder():
  with open("eating_disorder_differ.txt",'r') as eatingdisorder:
        x = eatingdisorder.read()
  return x

def endometriosis():
  with open("endometriosis_it_affect.txt",'r') as endometriosisaffect:
        x = endometriosisaffect.read()
  return x

def sodium():
  with open("excessive_sodium_intake.txt",'r') as sodiumintake:
        x = sodiumintake.read()
  return x

def exercise():
  with open("exercise_influence_mood.txt",'r') as exerciseinfluence:
        x = exerciseinfluence.read()
  return x

def gestational():
  with open("gestational_diabetes_affect.txt",'r') as gestationaldiabetes:
        x = gestationaldiabetes.read()
  return x

def glycemic():
  with open("glycemic_index_it.txt",'r') as glycemicindex:
        x = glycemicindex.read()
  return x

def gout():
  with open("gout_dietary_changes.txt",'r') as goutdietary:
        x = goutdietary.read()
  return x

def gutmicrobiome():
  with open("gut_microbiome_influence.txt",'r') as microbiomeinfluence:
        x = microbiomeinfluence.read()
  return x

def healthbenefit():
  with open("health_benefits_spending.txt",'r') as healthspending:
        x = healthspending.read()
  return x

def healthdiet():
  with open("health_consequences_diet.txt",'r') as healthdietcon:
        x = healthdietcon.read()
  return x

def hormonal():
  with open("health_effects_hormonal.txt",'r') as healthhormonal:
        x = healthhormonal.read()
  return x

def healthrisk():
  with open("health_risks_associated.txt",'r') as healthriskassoc:
        x = healthriskassoc.read()
  return x

def heartattack():
  with open("heart_attack_cardiac.txt",'r') as cardiac:
        x = cardiac.read()
  return x

def heartfailure():
  with open("heart_failure_it.txt",'r') as failure:
        x = failure.read()
  return x

def hearthealth():
  with open("heart_health_screenings.txt",'r') as screenings:
        x = screenings.read()
  return x

def highblood():
  with open("high_blood_pressure.txt",'r') as bloodpressure:
        x = bloodpressure.read()
  return x

def indoor():
  with open("indoor_air_quality.txt",'r') as indoorquality:
        x = indoorquality.read()
  return x

def insulin():
  with open("insulin_resistance_develop.txt",'r') as insulinresistance:
        x = insulinresistance.read()
  return x

def intermittent():
  with open("intermittent_fasting_affect.txt",'r') as intermittentfasting:
        x = intermittentfasting.read()
  return x

def bowel():
  with open("irritable_bowel_syndrome.txt",'r') as bowelsyndrome:
        x = bowelsyndrome.read()
  return x

def lifestyle():
  with open("lifestyle_changes_prevent.txt",'r') as lifestylechange:
        x = lifestylechange.read()
  return x


def lifestylefac():
  with open("lifestyle_factors_most.txt",'r') as lifestylefactors:
        x = lifestylefactors.read()
  return x

def psychological():
  with open("longterm_psychological_effects.txt",'r') as psychologicaleffects:
        x = psychologicaleffects.read()
  return x

def majorrisk():
  with open("major_risk_factors.txt",'r') as riskfactors:
        x = riskfactors.read()
  return x

def sleep():
  with open("many_hours_sleep.txt",'r') as sleephours:
        x = sleephours.read()
  return x

def fruits():
  with open("many_servings_fruits.txt",'r') as fruitserving:
        x = fruitserving.read()
  return x

def mediterranean():
  with open("mediterranean_diet_reduce.txt",'r') as mediterraneandiet:
        x = mediterraneandiet.read()
  return x

def menopause():
  with open("menopause_accelerate_bone.txt",'r') as menopausebone:
        x = menopausebone.read()
  return x

def menopausesym():
  with open("menopause_symptoms_accompany.txt",'r') as menopausesymptoms:
        x = menopausesymptoms.read()
  return x

def metabolic():
  with open("metabolic_syndrome_it.txt",'r') as metabolicsyndrome:
        x = metabolicsyndrome.read()
  return x

def mindfulness():
  with open("mindfulness_meditation_reduce.txt",'r') as mindfulnessmeditation:
        x = mindfulnessmeditation.read()
  return x


def cancer():
  with open("most_common_cancers.txt",'r') as commoncancer:
        x = commoncancer.read()
  return x

  def liver():
   with open("nonalcoholic_fatty_liver.txt",'r') as fattyliver:
        x = fattyliver.read()
  return x

  def healthy():
   with open("often_should_healthy.txt",'r') as healthyoften:
        x = healthyoften.read()
  return x

  def oftenmen():
   with open("often_should_men.txt",'r') as ofshmen:
        x = ofshmen.read()
  return x

def omega3():
  with open("omega3_fatty_acids.txt",'r') as omega3fatty:
        x = omega3fatty.read()
  return x

def osteoarthritis():
  with open("osteoarthritis_rheumatoid_arthritis.txt",'r') as osteoporosisarthritis:
        x = osteoporosisarthritis.read()
  return x

def osteoporosis():
  with open("osteoporosis_who_most.txt",'r') as osteoporosiswho:
        x = osteoporosiswho.read()
  return x


def peripheral_artery_disease():
  with open("peripheral_artery_disease.txt",'r') as peripheralartery:
        x = peripheralartery.read()
  return x

def pneumonia():
  with open("pneumonia_it_treated.txt",'r') as penumoniatreated:
        x = penumoniatreated.read()
  return x


def posttraumatic():
  with open("posttraumatic_stress_disorder.txt",'r') as posttraumaticstress:
        x = posttraumaticstress.read()
  return x

def posture():
  with open("posture_affect_longterm.txt",'r') as postureaffect:
        x = postureaffect.read()
  return x

def prediabetes():
  with open("prediabetes_it_reversed.txt",'r') as prediabetesreversed:
        x = prediabetesreversed.read()
  return x

def dailyintake():
  with open("recommended_daily_intake.txt",'r') as recommendedintake:
        x = recommendedintake.read()
  return x

def dailysteps():
  with open("recommended_daily_steps.txt",'r') as recommendedsteps:
        x = recommendedsteps.read()
  return x

def weightbearing():
  with open("regular_weightbearing_exercise.txt",'r') as weightbearingexercise:
        x = weightbearingexercise.read()
  return x

def recommendedsteps():
  with open("recommended_steps.txt",'r') as recommendedsteps:
        x = recommendedsteps.read()
  return x

def hpv():
  with open("role_hpv_vaccination.txt",'r') as hpvvaccination:
        x = hpvvaccination.read()
  return x

def lymphatic():
  with open("role_lymphatic_system.txt",'r') as lymphaticsystem:
        x = lymphaticsystem.read()
  return x

def physical():
  with open("role_physical_therapy.txt",'r') as lymphaticsystem:
        x = lymphaticsystem.read()
  return x

def serotonin():
  with open("role_serotonin_play.txt",'r') as serotoninplay:
        x = serotoninplay.read()
  return x

def seasonal():
  with open("seasonal_affective_disorder.txt",'r') as seasonalaffective:
        x = seasonalaffective.read()
  return x

def smoke():
  with open("secondhand_smoke_affect.txt",'r') as smokeaffect:
        x = smokeaffect.read()
  return x

def gastroesophageal():
  with open("signs_gastroesophageal_reflux.txt",'r') as gasreflux:
        x = gasreflux.read()
  return x

def iron():
  with open("signs_iron_deficiency.txt",'r') as irondeficiency:
        x = irondeficiency.read()
  return x

def joint():
  with open("signs_that_joint.txt",'r') as jointsigns:
        x = jointsigns.read()
  return x

def breakfast():
  with open("skipping_breakfast_affect.txt",'r') as skipbreakfast:
        x = skipbreakfast.read()
  return x

def sleep():
  with open("sleep_apnea_diagnosed.txt",'r') as sleepapnea:
        x = sleepapnea.read()
  return x

def sleepdep():
  with open("sleep_deprivation_affect.txt",'r') as sleepdeprivation:
        x = sleepdeprivation.read()
  return x

def smoking():
  with open("smoking_damage_heart.txt",'r') as smokeheart:
        x = smokeheart.read()
  return x

def smokerisk():
  with open("smoking_increase_risk.txt",'r') as smokerisked:
        x = smokerisked.read()
  return x

def isolation():
  with open("social_isolation_negatively.txt",'r') as socialisolation:
        x = socialisolation.read()
  return x

def soluble():
  with open("soluble_insoluble_fiber.txt",'r') as fiber:
        x = fiber.read()
  return x

def stressdigest():
  with open("stress_affect_digestive.txt",'r') as stressdigestive:
        x = stressdigestive.read()
  return x

def sun():
  with open("sun_exposure_increase.txt",'r') as sunexposure:
        x = sunexposure.read()
  return x

  def herniated():
   with open("symptoms_herniated_disc.txt",'r') as herniateddisc:
        x = herniateddisc.read()
  return x

def polycystic():
  with open("symptoms_polycystic_ovary.txt",'r') as polycysticovary:
        x = polycysticovary.read()
  return x

def pulmonary():
  with open("symptoms_pulmonary_embolism.txt",'r') as embolism:
        x = embolism.read()
  return x

def thyroid():
  with open("thyroid_function_affect.txt",'r') as thyroidfunction:
        x = thyroidfunction.read()
  return x

def type1():
  with open("type_1_type.txt",'r') as typeone:
        x = typeone.read()
  return x

def probiotics():
  with open("use_probiotics_support.txt",'r') as protonsupport:
        x = protonsupport.read()
  return x

def vaccinations():
  with open("vaccinations_recommended_prevent.txt",'r') as vacprevent:
        x = vacprevent.read()
  return x

def virusbac():
  with open("virus_bacterial_infection.txt",'r') as virusbacterial:
        x = virusbacterial.read()
  return x

def appendictis():
  with open("warning_signs_appendicitis.txt",'r') as appendixwarning:
        x = appendixwarning.read()
  return x

def burnout():
  with open("warning_signs_burnout.txt",'r') as burnoutsigns:
        x = burnoutsigns.read()
  return x

def colorectal():
  with open("warning_signs_colorectal.txt",'r') as colorectalsigns:
        x = colorectalsigns.read()
  return x

  def impending():
   with open("warning_signs_impending.txt",'r') as impendingsigns:
        x = smokeaffect.read()
  return x

def vitmin():
  with open("which_vitamins_minerals.txt",'r') as vitminerals:
        x = vitminerals.read()
  return x

def health_image():
  a = input("enter the image")
  if a == "processed food":
   food = Image.open('Processed Food.jpg')
   display(food)
   
  elif a == "development":
    food = Image.open('DevelopmentMilestone.png')
    display(food)

  elif a == "Fiber":
   food = Image.open('Fiber.jpg')
   display(food)

  elif a == "thyroid":
    food =Image.open('ThyroidWEM.png')
    display(food)

  elif a == "serotonin":
    food = Image.open('serotonin.jpg')
    display(food)

  elif a == "vaccinations":
   food = Image.open('vaccination.png')
   display(food)

  else:
    print('no images are found')

call_file = health_image()
print(call_file)

def healthaudio():
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:
    print("Adjusting for background noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Listening... Speak something!")
    audio = recognizer.listen(source)


    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    if text == "healthimage":
      print(call_file)
    else:
     print('file not found')


print("You said:", text)
translated_text = GoogleTranslator(source='en', target='ta').translate(text)
print(translated_text)
if text == "healthimage":
  print(call_file)
else:
  print('file not found')



#def virus():
  #y = pd.read_excel('VirusBacterial')

query = input(f"Write your query")
#convert_lower = resp.lower()
#key1 = " ".join(check(convert_lower.split()))
key1 = " ".join(check_in(query.split()))
print("KEY IS =",key1)

if key1 == "chronic":
  call_file = Chronic()
  print(call_file)

elif key1 =="healthimage":
  call_image = health_image()
  print(call_image)


elif key1 == "airpol":
  call_air = airpol()
  print(call_air)



else:
  print('not data found')







