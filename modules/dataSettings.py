from os.path import getsize, getctime
from datetime import datetime


class tenuresDataSettings:
    # CrownTenures
    currentTenuresPath = r"C:\Users\laure\Desktop\test\tenuresShapefileProcessed.shp"
    size = getsize(currentTenuresPath)
    downloadFolder = r"C:\Users\laure\Desktop\test"
    tenuresRawPath = r"C:\Users\laure\Desktop\HTGproject\data\TA_CROWN_TENURES_SVW\TA_CRT_SVW_polygon.shp"
    email = ""
    archiveFolder = r"C:\Users\laure\Desktop\test\testArchive"
    htgLandsPath = r"C:\Users\laure\Desktop\HTGproject\data\dummy_lands.gdb\lands1_sub_2"
    soiPath = r"C:\Users\laure\Desktop\HTGproject\data\HTG_SOIs_all.shp"
    arcgisWorkspaceFolder = downloadFolder
    tenuresCreatedDate = datetime.fromtimestamp(
        getctime(currentTenuresPath)).strftime('%B %d-%Y')

    # any adjustments must be in exactly the same format!!
    tenuresDictionary = {
        'AGRICULTURE, EXTENSIVE': 'agriculture',
        'AGRICULTURE, INTENSIVE': 'agriculture',
        'AQUACULTURE, PLANTS': 'aquaculture',
        'AQUACULTURE, SHELL FISH': 'aquaculture',
        'COMMERCIAL RECREATION, COMMUNITY OUTDOOR RECREATION': 'commercial recreation',
        'COMMERCIAL RECREATION, ECO TOURIST LODGE/RESORT': 'commercial recreation',
        'COMMERCIAL RECREATION, MISCELLANEOUS': 'commercial recreation',
        'COMMERCIAL RECREATION, TRAIL RIDING': 'commercial recreation',
        'COMMERCIAL, COMMERCIAL A': 'commercial',
        'COMMERCIAL, COMMERCIAL B': 'commercial',
        'COMMERCIAL, COMMERCIAL WHARF': 'wharf',
        'COMMERCIAL, FILM PRODUCTION': 'commercial',
        'COMMERCIAL, GENERAL': 'commercial',
        'COMMERCIAL, GOLF COURSE': 'commercial',
        'COMMERCIAL, MARINA': 'marina',
        'COMMERCIAL, MISCELLANEOUS': 'commercial',
        'COMMERCIAL, PRIVATE YACHT CLUB': 'commercial',
        'COMMUNICATION, COMBINED USES': 'communication',
        'COMMUNICATION, COMMUNICATION SITES': 'communication',
        'COMMUNITY, COMMUNITY FACILITY': 'community',
        'COMMUNITY, MISCELLANEOUS': 'community',
        'COMMUNITY, TRAIL MAINTENANCE': 'community',
        'ENVIRONMENT, CONSERVATION, & RECR, BUFFER ZONE': 'environment protection',
        'ENVIRONMENT, CONSERVATION, & RECR, ECOLOGICAL RESERVE': 'environment protection',
        'ENVIRONMENT, CONSERVATION, & RECR, ENVIRONMENT PROTECTION/CONSERVATION': 'environment protection',
        'ENVIRONMENT, CONSERVATION, & RECR, FISH AND WILDLIFE MANAGEMENT': 'wildlife management',
        'ENVIRONMENT, CONSERVATION, & RECR, FISHERY FACILITY': 'fishery facility',
        'ENVIRONMENT, CONSERVATION, & RECR, FOREST MANAGEMENT RESEARCH': 'forest/other research',
        'ENVIRONMENT, CONSERVATION, & RECR, PUBLIC ACCESS/PUBLIC TRAILS': 'public access',
        'ENVIRONMENT, CONSERVATION, & RECR, SCIENCE MEASUREMENT/RESEARCH': 'forest/other research',
        'ENVIRONMENT, CONSERVATION, & RECR, UREP/RECREATION RESERVE': 'recreation reserve',
        'ENVIRONMENT, CONSERVATION, & RECR, WATERSHED RESERVE': 'watershed reserve',
        'FIRST NATIONS, CULTURAL SIGNIFICANCE': 'First Nations',
        'FIRST NATIONS, INTERIM MEASURES': 'First Nations',
        'FIRST NATIONS, LAND CLAIM SETTLEMENT': 'First Nations',
        'FIRST NATIONS, RESERVE EXPANSION': 'First Nations',
        'FIRST NATIONS, TRADITIONAL USE': 'First Nations',
        'FIRST NATIONS, TREATY AREA': 'First Nations',
        'INDUSTRIAL, GENERAL': 'industrial',
        'INDUSTRIAL, HEAVY INDUSTRIAL': 'industrial',
        'INDUSTRIAL, LIGHT INDUSTRIAL': 'industrial',
        'INDUSTRIAL, LOG HANDLING/STORAGE': 'log handling',
        'INDUSTRIAL, MISCELLANEOUS': 'industrial',
        'INSTITUTIONAL, FIRE HALL': 'institutional',
        'INSTITUTIONAL, HOSPITAL/HEALTH FACILITY': 'institutional',
        'INSTITUTIONAL, INDOOR RECREATION FACILITY': 'institutional',
        'INSTITUTIONAL, LOCAL/REGIONAL PARK': 'park',
        'INSTITUTIONAL, MILITARY SITE': 'institutional',
        'INSTITUTIONAL, MISCELLANEOUS': 'institutional',
        'INSTITUTIONAL, PUBLIC WORKS': 'public works',
        'INSTITUTIONAL, SCHOOL/OUTDOOR EDUCATION FACILITY': 'institutional',
        'INSTITUTIONAL, WASTE DISPOSAL SITE': 'waste disposal',
        'MISCELLANEOUS LAND USES, LAND USE PLAN INTERIM AGREEMENT': 'other uses',
        'MISCELLANEOUS LAND USES, OTHER': 'other uses',
        'MISCELLANEOUS LAND USES, PLANNING/MARKETING/DEVELOP PROJECTS': 'other uses',
        'OCEAN ENERGY, INVESTIGATIVE AND MONITORING PHASE': 'ocean energy',
        'QUARRYING, CONSTRUCTION STONE': 'quarrying',
        'QUARRYING, MISCELLANEOUS': 'quarrying',
        'QUARRYING, SAND AND GRAVEL': 'quarrying',
        'RESIDENTIAL, APPLICATION ONLY - PRIVATE MOORAGE': 'moorage',
        'RESIDENTIAL, FLOATING CABIN': 'residential',
        'RESIDENTIAL, MISCELLANEOUS': 'residential',
        'RESIDENTIAL, PRIVATE MOORAGE': 'moorage',
        'RESIDENTIAL, RECREATIONAL RESIDENTIAL': 'residential',
        'RESIDENTIAL, REMOTE RESIDENTIAL': 'residential',
        'RESIDENTIAL, RURAL RESIDENTIAL': 'residential',
        'RESIDENTIAL, STRATA MOORAGE': 'moorage',
        'RESIDENTIAL, THERMAL LOOPS': 'alternate energy',
        'RESIDENTIAL, URBAN RESIDENTIAL': 'residential',
        'TRANSPORTATION, BRIDGES': 'bridges',
        'TRANSPORTATION, FERRY TERMINAL': 'ferry terminal',
        'TRANSPORTATION, NAVIGATION AID': 'navigation',
        'TRANSPORTATION, PUBLIC WHARF': 'wharf',
        'TRANSPORTATION, RAILWAY': 'rail',
        'TRANSPORTATION, ROADWAY': 'road',
        'UTILITY, ELECTRIC POWER LINE': 'electrical',
        'UTILITY, GAS AND OIL PIPELINE': 'pipeline',
        'UTILITY, MISCELLANEOUS': 'utility - other',
        'UTILITY, SEWER/EFFLUENT LINE': 'sewer line',
        'UTILITY, TELECOMMUNICATION LINE': 'communication',
        'UTILITY, WATER LINE': 'water line',
        'WINDPOWER, INVESTIGATIVE AND MONITORING PHASE': 'alternate energy'
    }
