exarchs = [
    {
        "tag": 'ELG',
        "special": True
    },

    {
        "tag": 'EEA',
        "name": 'armenia',
        "culture_group": 'caucasian',
        "primary_culture": 'georgian',
        "desc": "Armenia was a nominally independent client kingdom often divided between "
                "and (fought over) by the Ancient Roman and Persian Empires. Now that it has "
                "been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with "
                "the local elite."
    },
    {
        "tag": 'EEB',
        "name": 'anglia',
        "culture_group": 'british',
        "primary_culture": 'english',
        "desc": "Anglia or Britannia was one of Ancient Rome's most troublesome provinces and was among the first to be "
                "abandoned as the Western Empire collapsed. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEC',
        "name": 'skanza',
        "culture_group": 'scandinavian',
        "primary_culture": 'danish',
        "desc": 'Skanza was far beyond the borders of the ancient Roman Empire; however, the fearsome Vikings that '
                'resided there would raid Western Europe for centuries before their conversion to Christianity. Now that we have conquered the region, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite.'
    },
    {
        "tag": 'EED',
        "name": 'pannonia',
        "culture_group": 'carpathian',
        "primary_culture": 'hungarian',
        "desc": "Once at the forefront of Trajan's conquests, this area was gradually abandoned over the centuries as raids and invasions took their toll. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."

    },
    {
        "tag": 'EEE',
        "name": 'aigyptos',
        "culture_group": 'turko_semitic',
        "primary_culture": 'al_misr_arabic',
        "additional_effects":
            "if = {\n"
            "				limit = { mission_completed = to_in_alexios_footsteps_mission }\n"
            "				custom_tooltip = nhs_new_line_tt\n"
            "				to_add_old_world_exarch_claim = { TERRITORY = egypt_region TAG = EEE }\n"
            "			}",
        "desc": "Aigyptos was once the breadbasket of the Ancient Roman Empire and one of its wealthiest provinces before being lost to Muslim conquest. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },

    {
        "tag": 'EEF',
        "name": 'aphrike',
        "culture_group": 'maghrebi',
        "primary_culture": 'tunisian',
        "check_supply_lines": True,
        "desc": "Afrika was once the homeland of the hated Carthaginian Empire and was one of the few provinces that were retaken in Justinian's reconquests. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEG',
        "name": 'frankia',
        "culture_group": 'french',
        "primary_culture": 'occitain',
        "desc": "Gallia, once the heartland of the Western Empire, and the last bastion in the west to fall "
                "to the Franks. What remains of the formidable power would be better "
                "managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEH',
        "name": 'spania',
        "culture_group": 'iberian',
        "primary_culture": 'catalan',
        "check_supply_lines": True,
        "gibraltar_check": True,
        "merchant_tooltip_overwrite": "custom_tooltip = nhs_exarch_bonus_merchant_eeh_tt",
        "desc": "Spania has long been the home of warring tribes and petty kingdoms, from before we came to this land thousands of years ago to long after we left at the fall of the Western Empire. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEI',
        "name": 'ano_germania',
        "culture_group": 'germanic',
        "primary_culture": 'austrian',
        "desc": "Comprising mainly the land between the Italian Alps and the Danubian frontier, this land was one of the borders of the ancient empire. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEJ',
        "name": 'baltikos',
        "culture_group": 'baltic',
        "primary_culture": 'lithuanian',
        "desc": "Baltikos was far from the borders of the Ancient Romans, with the area being largely unknown to them. Now that we have conquered the region, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },

    {
        "tag": 'EEL',
        "name": 'rhosia',
        "culture_group": 'east_slavic',
        "primary_culture": 'russian',
        "desc": "Rhosia was once home to the Kievan Rus, a people to which we gave the gift of the written word through the creation of the Cyrillic alphabet. Now that we have returned, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEM',
        "name": 'sarmatia',
        "culture_group": 'east_slavic',
        "primary_culture": 'ruthenian',
        "desc": "Sarmatia was an ancient land, little-known to the Ancient Empire. Long after the fall of the Western Empire, these lands were increasingly settled by the ancient Varangians. Now that it has been taken over, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEO',
        "name": 'syria',
        "culture_group": 'turko_semitic',
        "primary_culture": 'al_suryah_arabic',
        "additional_effects":
            "if = {\n"
            "				limit = { mission_completed = to_in_alexios_footsteps_mission }\n"
            "				custom_tooltip = nhs_new_line_tt\n"
            "				to_add_old_world_exarch_claim = { TERRITORY = aleppo_area TAG = EEO }\n"
            "				to_add_old_world_exarch_claim = { TERRITORY = syria_area TAG = EEO }\n"
            "				to_add_old_world_exarch_claim = { TERRITORY = palestine_area TAG = EEO }\n"
            "				to_add_old_world_exarch_claim = { TERRITORY = syrian_desert_area TAG = EEO }\n"
            "				to_add_old_world_exarch_claim = { TERRITORY = trans_jordan_area TAG = EEO }\n"
            "			}",
        "desc": "Syria includes much of the land taken from the Sassanid Empire at the Roman Empire's greatest extent, as well as the large, urbanized cities of the Levant. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EER',
        "name": 'italia',
        "culture_group": 'latin',
        "primary_culture": 'umbrian',
        "check_supply_lines": True,
        "varangians_check": True,
        "merchant_tooltip_overwrite": "if = {\n"
                                      "				limit = { "
                                      "VGD = { is_subject_of = ROOT is_subject_of_type = "
                                      "elysian_subject_varangian }"
                                      " }\n"
                                      "				custom_tooltip = nhs_exarch_bonus_merchant_eer_tt\n"
                                      "			}\n"
                                      "			else = {\n"
                                      "				custom_tooltip = nhs_exarch_bonus_merchant_tt\n"
                                      "			}",
        "desc": "Italia was once the political, cultural and economic centre of the Ancient Roman Empire, however, "
                "over the centuries it has developed its own distinct culture far from that of our own. Now that it has been finally retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EES',
        "name": 'megale_kimmeria',
        "culture_group": 'tartar',
        "primary_culture": 'crimean',
        "desc": "The corridor that presented a starting point for every invasion by the horsemen of the steppes, "
                "from the Huns "
                "themselves to the Avars, the Magyars, the Khazars, the Pechenegs, all the way to the Mongols. Now that it is under [Root.GetAdjective] control, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite (such as it is on the steppe)."
    },

    {
        "tag": 'EET',
        "name": 'kato_germania',
        "culture_group": 'germanic',
        "primary_culture": 'dutch',
        "desc": "Germania Inferior or Kato Germania was an important border province during the time of the Ancient "
                "Roman Empire before falling to Germanic conquest. Now that it has been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEU',
        "name": 'megali_germania',
        "culture_group": 'germanic',
        "primary_culture": 'saxon',
        "desc": "Magna Germania or Megali Germania was once inhabited by the most fearsome of the Germanic tribes, "
                "many of whom eventually settled in the lands of the former Western Roman Empire. Now that it has been finally taken over, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEV',
        "name": 'venedai',
        "culture_group": 'west_slavic',
        "primary_culture": 'polish',
        "desc": "Venedai was a dangerous land far from the borders of the Roman Empire in which monsters and monster "
                "slayers were said to have fought an ever losing battle against the march of time. Now that it has been taken over, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEQ',
        "name": 'aravia',
        "culture_group": 'turko_semitic',
        "primary_culture": 'hejazi_culture',
        "desc": "The deserts of the Arabian Peninsula once unleashed an army that conquered half our empire in a holy fury. Now, however, we have a foothold in this land, the birthplace of Islam. Now that we are in control, we find that it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite."
    },
    {
        "tag": 'EEP',
        "name": 'perses',
        "culture_group": 'iranian',
        "primary_culture": 'persian',
        "desc": "Persia, our most ancient foe, falters at our spears. This land, lying once beyond our farthest "
                "borders, is now within our dominion. To lessen the threat of rebellion, we should appoint an [Root.GetAdjective]-led Exarch to govern the land in cooperation with the local elite."
    }
]
