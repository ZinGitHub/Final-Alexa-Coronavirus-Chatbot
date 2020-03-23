# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Class for What Is Coronavirus Intent Handler.
class WhatIsCoronavirusIntentHandler(AbstractRequestHandler):
    """Handler for What Is Coronavirus Intent."""
    # Recognizes each incoming request that Alexa when it recieves WhatIsCoronavirusIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (WhatIsCoronavirusIntent) and it's handler_input.
        return ask_utils.is_intent_name("WhatIsCoronavirusIntent")(handler_input)
    
    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the WhatIsCoronavirusIntent
        speak_output = "Coronaviruses are a large family of viruses which may cause illness in animals or humans.  In humans, several coronaviruses are known to cause respiratory infections. The most recently discovered coronavirus causes coronavirus disease COVID-19."
        
        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for What Is Covid Intent Handler.
class WhatIsCovidIntentHandler(AbstractRequestHandler):
    """Handler for What Is Covid Intent."""
    # Recognizes each incoming request that Alexa when it recieves WhatIsCovidIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (WhatIsCovidIntent) and it's handler_input.
        return ask_utils.is_intent_name("WhatIsCovidIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the WhatIsCovidIntent
        speak_output = "COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019."
        
        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for What Are Symptoms Intent Handler.
class WhatAreSymptomsIntentHandler(AbstractRequestHandler):
    """Handler for What Are Symptoms Intent."""
    # Recognizes each incoming request that Alexa when it recieves WhatAreSymptomsIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (WhatAreSymptomsIntent) and it's handler_input.
        return ask_utils.is_intent_name("WhatAreSymptomsIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the WhatAreSymptomsIntent
        speak_output = "Symptoms: include fever, coughing, shortness of breath, fatigue, dry cough, runny nose, nasal congestion, runny nose, sore throat, and body aches."
        
        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for How Does Spread Intent Handler.
class HowDoesSpreadIntentHandler(AbstractRequestHandler):
    """Handler for How Does Spread Intent."""
    # Recognizes each incoming request that Alexa when it recieves HowDoesSpreadIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (HowDoesSpreadIntent) and it's handler_input.
        return ask_utils.is_intent_name("HowDoesSpreadIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the HowDoesSpreadIntent
        speak_output = "People can catch COVID-19 from others who have the virus. The disease can spread from person to person through small droplets from the nose or mouth which are spread when a person with COVID-19 coughs or exhales. These droplets land on objects and surfaces around the person. Other people then catch COVID-19 by touching these objects or surfaces, then touching their eyes, nose or mouth. People can also catch COVID-19 if they breathe in droplets from a person with COVID-19 who coughs out or exhales droplets."
        
        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )   
# Class for Protection Measures Intent Handler.
class ProtectionMeasuresIntentHandler(AbstractRequestHandler):
    """Handler for Protection Measures Intent."""
    # Recognizes each incoming request that Alexa when it recieves ProtectionMeasuresIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (ProtectionMeasuresIntent) and it's handler_input.
        return ask_utils.is_intent_name("ProtectionMeasuresIntent")(handler_input)
    
    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the ProtectionMeasuresIntent
        speak_output = "Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing. Avoid touching eyes, nose and mouth. Make sure you, and the people around you, follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately. Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. Follow the directions of your local health authority. Keep up to date on the latest COVID-19 hotspots (cities or local areas where COVID-19 is spreading widely). If possible, avoid traveling to places  – especially if you are an older person or have diabetes, heart or lung disease."

        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for How Likely To Catch Intent Handler.
class HowLikelyToCatchIntentHandler(AbstractRequestHandler):
    """Handler for How Likely To Catch Intent."""
    # Recognizes each incoming request that Alexa when it recieves HowLikelyToCatchIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (HowLikelyToCatchIntent) and it's handler_input.
        return ask_utils.is_intent_name("HowLikelyToCatchIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the HowLikelyToCatchIntent
        speak_output = "The risk depends on where you  are - and more specifically, whether there is a COVID-19 outbreak unfolding there. For most people in most locations the risk of catching COVID-19 is still low. However, there are now places around the world (cities or areas) where the disease is spreading. For people living in, or visiting, these areas the risk of catching COVID-19 is higher. Governments and health authorities are taking vigorous action every time a new case of COVID-19 is identified. Be sure to comply with any local restrictions on travel, movement or large gatherings. Cooperating with disease control efforts will reduce your risk of catching or spreading COVID-19."
        
        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for Should I Worry Intent Handler.
class ShouldIWorryIntentHandler(AbstractRequestHandler):
    """Handler for Should I Worry Intent."""
    # Recognizes each incoming request that Alexa when it recieves ShouldIWorryIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (ShouldIWorryIntent) and it's handler_input.
        return ask_utils.is_intent_name("ShouldIWorryIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the ShouldIWorryIntent
        speak_output = "Illness due to COVID-19 infection is generally mild, especially for children and young adults. However, it can cause serious illness: about 1 in every 5 people who catch it need hospital care. It is therefore quite normal for people to worry about how the COVID-19 outbreak will affect them and their loved ones. We can channel our concerns into actions to protect ourselves, our loved ones and our communities. First and foremost among these actions is regular and thorough hand-washing and good respiratory hygiene. Secondly, keep informed and follow the advice of the local health authorities including any restrictions put in place on travel, movement and gatherings."

        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for Who Risk Severe Illness Intent Handler.
class WhoRiskSevereIllnessIntentHandler(AbstractRequestHandler):
    """Handler for Who Risk Severe Illness Intent."""
    # Recognizes each incoming request that Alexa when it recieves WhoRiskSevereIllnessIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (WhoRiskSevereIllnessIntent) and it's handler_input.
        return ask_utils.is_intent_name("WhoRiskSevereIllnessIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the WhoRiskSevereIllnessIntent
        speak_output = "While we are still learning about how COVID-2019 affects people, older persons and persons with pre-existing medical conditions (such as high blood pressure, heart disease, lung disease, cancer or diabetes)  appear to develop serious illness more often than others."

        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for Are Antibiotics Effecttive Intent Handler.
class AreAntibioticsEffecttiveIntentIntentHandler(AbstractRequestHandler):
    """Handler for Are Antibiotics Effecttive Intent."""
    # Recognizes each incoming request that Alexa when it recieves AreAntibioticsEffecttiveIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (AreAntibioticsEffecttiveIntent) and it's handler_input.
        return ask_utils.is_intent_name("AreAntibioticsEffecttiveIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the AreAntibioticsEffecttiveIntent
        speak_output = "No. Antibiotics do not work against viruses, they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19. They should only be used as directed by a physician to treat a bacterial infection."

        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for Any Medication Prevent Intent Handler.        
class AnyMedicationPreventIntentHandler(AbstractRequestHandler):
    """Handler for Any Medication Prevent Intent."""
    # Recognizes each incoming request that Alexa when it recieves AnyMedicationPreventIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (AnyMedicationPreventIntent) and it's handler_input.
        return ask_utils.is_intent_name("AnyMedicationPreventIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the AnyMedicationPreventIntent
        speak_output = "While some western, traditional or home remedies may provide comfort and alleviate symptoms of COVID-19, there is no evidence that current medicine can prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19. However, there are several ongoing clinical trials that include both western and traditional medicines. WHO will continue to provide updated information as soon as clinical findings are available."

        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for Vaccine Or Treatment Intent Handler.
class VaccineOrTreatmentIntentHandler(AbstractRequestHandler):
    """Handler for  Vaccine Or Treatment Intent."""
    # Recognizes each incoming request that Alexa when it recieves VaccineOrTreatmentIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (VaccineOrTreatmentIntent) and it's handler_input.
        return ask_utils.is_intent_name("VaccineOrTreatmentIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the VaccineOrTreatmentIntent
        speak_output = "Not yet. To date, there is no vaccine and no specific antiviral medicine to prevent or treat COVID-2019. However, those affected should receive care to relieve symptoms. People with serious illness should be hospitalized. Most patients recover thanks to supportive care. Possible vaccines and some specific drug treatments are under investigation. They are being tested through clinical trials."

        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for Coronavirus Like Sars Intent Handler.
class CoronavirusLikeSarsIntentHandler(AbstractRequestHandler):
    """Handler for Coronavirus Like Sars Intent."""
    # Recognizes each incoming request that Alexa when it recieves CoronavirusLikeSarsIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (CoronavirusLikeSarsIntent) and it's handler_input.
        return ask_utils.is_intent_name("CoronavirusLikeSarsIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the CoronavirusLikeSarsIntent
        speak_output = "No. The virus that causes COVID-19 and the one that caused the outbreak of Severe Acute Respiratory Syndrome (SARS) in 2003 are related to each other genetically, but the diseases they cause are quite different. SARS was more deadly but much less infectious than COVID-19. There have been no outbreaks of SARS anywhere in the world since 2003."

        # Return the handler_input response_builder
        return (
            handler_input.response_builder
                # Return the speak output
                .speak(speak_output)
                # Keep the session open for the user to respond
                .ask(speak_output)
                # Return response
                .response
        )
# Class for Should I Wear Mask Intent Handler.
class ShouldIWearMaskIntentHandler(AbstractRequestHandler):
    """Handler for Should I Wear Mask Intent."""
    # Recognizes each incoming request that Alexa when it recieves ShouldIWearMaskIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (ShouldIWearMaskIntent) and it's handler_input.
        return ask_utils.is_intent_name("ShouldIWearMaskIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the ShouldIWearMaskIntent.
        speak_output = "Only wear a mask if you are ill with COVID-19 symptoms (especially coughing) or looking after someone who may have COVID-19. Disposable face mask can only be used once. If you are not ill or looking after someone who is ill then you are wasting a mask. There is a world-wide shortage of masks, and the World Health Organization urges people to use masks wisely."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Mask Procedure Intent Handler.
class MaskProcedureIntentHandler(AbstractRequestHandler):
    """Handler for Mask Procedure Intent."""
    # Recognizes each incoming request that Alexa when it recieves MaskProcedureIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (MaskProcedureIntent) and it's handler_input.
        return ask_utils.is_intent_name("MaskProcedureIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the MaskProcedureIntent.
        speak_output = "1) Remember, a mask should only be used by health workers, care takers, and individuals with respiratory symptoms, such as fever and cough. 2) Before touching the mask, clean hands with an alcohol-based hand rub or soap and water. 3)Take the mask and inspect it for tears or holes. 4) Orient which side is the top side (where the metal strip is). 5) Ensure the proper side of the mask faces outwards (the coloured side). 6) Place the mask to your face. Pinch the metal strip or stiff edge of the mask so it moulds to the shape of your nose. 7) Pull down the mask’s bottom so it covers your mouth and your chin. 8) After use, take off the mask; remove the elastic loops from behind the ears while keeping the mask away from your face and clothes, to avoid touching potentially contaminated surfaces of the mask. 9) Discard the mask in a closed bin immediately after use. 10) Perform hand hygiene after touching or discarding the mask – Use alcohol-based hand rub or, if visibly soiled, wash your hands with soap and water."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Incubation Period Intent Handler.
class IncubationPeriodIntentHandler(AbstractRequestHandler):
    """Handler for Incubation Period Intent."""
    # Recognizes each incoming request that Alexa when it recieves IncubationPeriodIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (IncubationPeriodIntent) and it's handler_input.
        return ask_utils.is_intent_name("IncubationPeriodIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the IncubationPeriodIntent.
        speak_output = "The “incubation period” means the time between catching the virus and beginning to have symptoms of the disease. Most estimates of the incubation period for COVID-19 range from 1-14 days, most commonly around five days. These estimates will be updated as more data become available."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Animal Source Infection Intent Handler.
class AnimalSourceInfectionIntentHandler(AbstractRequestHandler):
    """Handler for Animal Source Infection Intent."""
    # Recognizes each incoming request that Alexa when it recieves AnimalSourceInfectionIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (AnimalSourceInfectionIntent) and it's handler_input.
        return ask_utils.is_intent_name("AnimalSourceInfectionIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the AnimalSourceInfectionIntent.
        speak_output = "Coronaviruses are a large family of viruses that are common in animals. Occasionally, people get infected with these viruses which may then spread to other people. For example, SARS-CoV was associated with civet cats and MERS-CoV is transmitted by dromedary camels. Possible animal sources of COVID-19 have not yet been confirmed."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Pet Catch Corona Intent Handler.
class PetCatchCoronaIntentHandler(AbstractRequestHandler):
    """Handler for Pet Catch Corona Intent."""
    # Recognizes each incoming request that Alexa when it recieves PetCatchCoronaIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (PetCatchCoronaIntent) and it's handler_input.
        return ask_utils.is_intent_name("PetCatchCoronaIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the PetCatchCoronaIntent.
        speak_output = "While there has been one instance of a dog being infected in Hong Kong, to date, there is no evidence that a dog, cat or any pet can transmit COVID-19. COVID-19 is mainly spread through droplets produced when an infected person coughs, sneezes, or speaks. To protect yourself, clean your hands frequently and thoroughly."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Virus Survive Surface Intent Handler.    
class VirusSurviveSurfaceIntentHandler(AbstractRequestHandler):
    """Handler for Virus Survive Surface Intent."""
    # Recognizes each incoming request that Alexa when it recieves VirusSurviveSurfaceIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (VirusSurviveSurfaceIntent) and it's handler_input.
        return ask_utils.is_intent_name("VirusSurviveSurfaceIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the VirusSurviveSurfaceIntent.
        speak_output = "It is not certain how long the virus that causes COVID-19 survives on surfaces, but it seems to behave like other coronaviruses. Studies suggest that coronaviruses (including preliminary information on the COVID-19 virus) may persist on surfaces for a few hours or up to several days. This may vary under different conditions (e.g. type of surface, temperature or humidity of the environment). If you think a surface may be infected, clean it with simple disinfectant to kill the virus and protect yourself and others. Clean your hands with an alcohol-based hand rub or wash them with soap and water. Avoid touching your eyes, mouth, or nose."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Package Safety Intent Handler.
class PackageSafetyIntentHandler(AbstractRequestHandler):
    """Handler for Package Safety Intent."""
    # Recognizes each incoming request that Alexa when it recieves PackageSafetyIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (PackageSafetyIntent) and it's handler_input.
        return ask_utils.is_intent_name("PackageSafetyIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the PackageSafetyIntent.
        speak_output = "Yes. The likelihood of an infected person contaminating commercial goods is low and the risk of catching the virus that causes COVID-19 from a package that has been moved, travelled, and exposed to different conditions and temperature is also low."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Package Safety Intent Handler.
class SickProcedureIntentHandler(AbstractRequestHandler):
    """Handler for Package Safety Intent."""
    # Recognizes each incoming request that Alexa when it recieves SickProcedureIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (SickProcedureIntent) and it's handler_input.
        return ask_utils.is_intent_name("SickProcedureIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the SickProcedureIntent.
        speak_output = "Stay home except to get medical care and avoid public transportation. Separate yourself from other people in your home. Call ahead before visiting your doctor. Wear a facemask if you are sick, Cover your coughs and sneezes. Dispose tissues, masks, and wash your hands. Clean your hands often and Avoid sharing personal household items. Clean all high-touch surfaces everyday, and monitor your symptoms."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Severe Symptoms Intent Handler.
class SevereSymptomsIntentHandler(AbstractRequestHandler):
    """Handler for Severe Symptoms Intent."""
    # Recognizes each incoming request that Alexa when it recieves SevereSymptomsIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (SevereSymptomsIntent) and it's handler_input.
        return ask_utils.is_intent_name("SevereSymptomsIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the SevereSymptomsIntent.
        speak_output = "The most severe symptoms are difficult breathing, pain/pressure in chest, high fever, and Pneumonia."

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )
# Class for Sources Intent Handler.
class SourcesIntentHandler(AbstractRequestHandler):
    """Handler for Sources Intent."""
    # Recognizes each incoming request that Alexa when it recieves SourcesIntent Utterances.
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        # Return the intent name (SourcesIntent) and it's handler_input.
        return ask_utils.is_intent_name("SourcesIntent")(handler_input)

    # Returns an appropriate response.
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # This will be what Alexa outputs for the SourcesIntent.
        speak_output = "The sources that Peanut Medic Bot uses are the CDC, World Health Organization, Mayo Clinic, and Harvard Medical School. "

        # Return the handler_input response_builder.
        return (
            handler_input.response_builder
                # Return the speak output.
                .speak(speak_output)
                # Keep the session open for the user to respond.
                .ask(speak_output)
                # Return response.
                .response
        )

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )



class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

# Variable sb is equal to the SkillBuilder object which passes the intent handler class as an argurment to .add_request_handler
sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())

# Passing the WhatIsCoronavirusIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(WhatIsCoronavirusIntentHandler())

# Passing the WhatIsCovidIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(WhatIsCovidIntentHandler())

# Passing the WhatAreSymptomsIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(WhatAreSymptomsIntentHandler())

# Passing the HowDoesSpreadIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(HowDoesSpreadIntentHandler())

# Passing the ProtectionMeasuresIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(ProtectionMeasuresIntentHandler())

# Passing the HowLikelyToCatchIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(HowLikelyToCatchIntentHandler())

# Passing the ShouldIWorryIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(ShouldIWorryIntentHandler())

# Passing the WhoRiskSevereIllnessIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(WhoRiskSevereIllnessIntentHandler())

# Passing the AreAntibioticsEffecttiveIntentIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(AreAntibioticsEffecttiveIntentIntentHandler())

# Passing the AnyMedicationPreventIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(AnyMedicationPreventIntentHandler())

# Passing the VaccineOrTreatmentIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(VaccineOrTreatmentIntentHandler())

# Passing the CoronavirusLikeSarsIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(CoronavirusLikeSarsIntentHandler())

# Passing the ShouldIWearMaskIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(ShouldIWearMaskIntentHandler())

# Passing the MaskProcedureIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(MaskProcedureIntentHandler())

# Passing the IncubationPeriodIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(IncubationPeriodIntentHandler())

# Passing the AnimalSourceInfectionIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(AnimalSourceInfectionIntentHandler())

# Passing the PetCatchCoronaIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(PetCatchCoronaIntentHandler())

# Passing the VirusSurviveSurfaceIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(VirusSurviveSurfaceIntentHandler())

# Passing the PackageSafetyIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(PackageSafetyIntentHandler())

# Passing the SickProcedureIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(SickProcedureIntentHandler())

# Passing the SevereSymptomsIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(SevereSymptomsIntentHandler())

# Passing the SourcesIntentHandler() class as an argurment to .add_request_handler().
sb.add_request_handler(SourcesIntentHandler())

sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
