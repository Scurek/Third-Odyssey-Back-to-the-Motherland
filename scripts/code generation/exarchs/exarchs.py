exarchs = [
    {
        "tag": 'EEA',
        "name": 'armenia',
        "culture_group": 'caucasian',
        "primary_culture": 'georgian',
        "desc": "Armenia was a nominally independent client kingdom often divided between "
                "and (fought over) by the Ancient Roman and Persian Empires. Now that it has "
                "been retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with "
                "the local elite.",
        "land": "[H][4301.GetRegionName][!H] region"
    },
    {
        "tag": 'EEB',
        "name": 'anglia',
        "culture_group": 'british',
        "primary_culture": 'english',
        "desc": "Anglia or Britannia was one of Ancient Rome's most troublesome provinces and was among the first to be "
                "abandoned as the Western Empire collapsed. Now that it has been retaken, it would be better managed "
                "under an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][236.GetRegionName][!H] region"
    },
    {
        "tag": 'EEC',
        "name": 'skanza',
        "culture_group": 'scandinavian',
        "primary_culture": 'danish',
        "desc": 'Skanza was far beyond the borders of the ancient Roman Empire; however, the fearsome Vikings that '
                'resided there would raid Western Europe for centuries before their conversion to Christianity. '
                'Now that we have conquered the region, it would be better managed under an [Root.GetAdjective]-led '
                'Exarch in cooperation with the local elite.',
        "land": "[H][1.GetRegionName][!H] region"
    },
    {
        "tag": 'EED',
        "name": 'pannonia',
        "culture_group": 'carpathian',
        "primary_culture": 'hungarian',
        "desc": "Once at the forefront of Trajan's conquests, this area was gradually abandoned over the centuries as "
                "raids and invasions took their toll. Now that it has been retaken, it would be better managed under "
                "an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][153.GetRegionName][!H] region, except for [A][1772.GetAreaName][!A] area"
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
            "				custom_tooltip = nhs_new_line_tt\n"
            "			}",
        "desc": "Aigyptos was once the breadbasket of the Ancient Roman Empire and one of its wealthiest provinces "
                "before being lost to Muslim conquest. Now that it has been retaken, it would be better managed under "
                "an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][361.GetRegionName][!H] region"
    },

    {
        "tag": 'EEF',
        "name": 'aphrike',
        "culture_group": 'maghrebi',
        "primary_culture": 'tunisian',
        "check_supply_lines": True,
        "desc": "Afrika was once the homeland of the hated Carthaginian Empire and was one of the few provinces that "
                "were retaken in Justinian's reconquests. Now that it has been retaken, it would be better managed "
                "under an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][341.GetRegionName][!H] region"
    },
    {
        "tag": 'EEG',
        "name": 'frankia',
        "culture_group": 'french',
        "primary_culture": 'occitain',
        "desc": "Gallia, once the heartland of the Western Empire, and the last bastion in the west to fall "
                "to the Franks. What remains of the formidable power would be better "
                "managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][183.GetRegionName][!H] region"
    },
    {
        "tag": 'EEH',
        "name": 'spania',
        "culture_group": 'iberian',
        "primary_culture": 'catalan',
        "check_supply_lines": True,
        "gibraltar_check": True,
        "merchant_tooltip_overwrite": "custom_tooltip = to_exarch_bonus_merchant_eeh_tt",
        "desc": "Spania has long been the home of warring tribes and petty kingdoms, from before we came to this land "
                "thousands of years ago to long after we left at the fall of the Western Empire. Now that it has been "
                "retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation with "
                "the local elite.",
        "land": "[H][219.GetRegionName][!H] region"
    },
    {
        "tag": 'EEI',
        "name": 'ano_germania',
        "culture_group": 'germanic',
        "primary_culture": 'austrian',
        "desc": "Comprising mainly the land between the Italian Alps and the Danubian frontier, this land was one of "
                "the borders of the ancient empire. Now that it has been retaken, it would be better managed under "
                "an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][134.GetRegionName][!H] region"
    },
    {
        "tag": 'EEJ',
        "name": 'baltikos',
        "culture_group": 'baltic',
        "primary_culture": 'lithuanian',
        "desc": "Baltikos was far from the borders of the Ancient Romans, with the area being largely unknown to them. "
                "Now that we have conquered the region, it would be better managed under an [Root.GetAdjective]-led "
                "Exarch in cooperation with the local elite.",
        "land": "[H][38.GetRegionName][!H] region"
    },

    {
        "tag": 'EEL',
        "name": 'rhosia',
        "culture_group": 'east_slavic',
        "primary_culture": 'russian',
        "desc": "Rhosia was once home to the Kievan Rus, a people to which we gave the gift of the written word "
                "through the creation of the Cyrillic alphabet. Now that we have returned, it would be better managed "
                "under an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][295.GetRegionName][!H] and [H][1963.GetRegionName][!H] regions, except for the following areas: "
                "[A][302.GetAreaName][!A], [A][303.GetAreaName][!A], [A][473.GetAreaName][!A], [A][1082.GetAreaName][!A], "
                "[A][2421.GetAreaName][!A], [A][475.GetAreaName][!A], [A][469.GetAreaName][!A], [A][465.GetAreaName][!A]"
    },
    {
        "tag": 'EEM',
        "name": 'antaia',
        "culture_group": 'east_slavic',
        "primary_culture": 'ruthenian',
        "desc": "Ever since the fall of the Western Empire, the lands north of the Pontic steppe came to be mostly "
                "inhabited by Anteans, Slavic people, who were at different times our enemies, allies and subjects."
                " Undeterred by intermittent invasions of steppe peoples, their descendants still govern those fertile"
                " lands. Now that we that our Empire claims sovereignty over those territories, the people would be "
                "undoubtedly better managed by [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][280.GetRegionName][!H] region and [1940.GetAreaName] area"
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
            "				custom_tooltip = nhs_new_line_tt\n"
            "			}",
        "desc": "Syria includes much of the land taken from the Sassanid Empire at the Roman Empire's greatest extent, "
                "as well as the large, urbanized cities of the Levant. Now that it has been retaken, it would be "
                "better managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][379.GetRegionName][!H] region"
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
                                      "				custom_tooltip = to_exarch_bonus_merchant_eer_tt\n"
                                      "			}\n"
                                      "			else = {\n"
                                      "				custom_tooltip = to_exarch_bonus_merchant_tt\n"
                                      "			}",
        "desc": "Italia was once the political, cultural and economic centre of the Ancient Roman Empire, however, "
                "over the centuries it has developed its own distinct culture far from that of our own. Now that it has "
                "been finally retaken, it would be better managed under an [Root.GetAdjective]-led Exarch in "
                "cooperation with the local elite.",
        "land": "[H][118.GetRegionName][!H] region"
    },
    {
        "tag": 'EES',
        "name": 'megale_kimmeria',
        "culture_group": 'tartar',
        "primary_culture": 'crimean',
        "desc": "The corridor that presented a starting point for every invasion by the horsemen of the steppes, "
                "from the Huns "
                "themselves to the Avars, the Magyars, the Khazars, the Pechenegs, all the way to the Mongols. "
                "Now that it is under [Root.GetAdjective] control, it would be better managed under an "
                "[Root.GetAdjective]-led Exarch in cooperation with the local elite (such as it is on the steppe).",
        "land": "[H][2410.GetRegionName][!H] region and [H][302.GetAreaName][!H], [H][303.GetAreaName][!H], "
                "[H][473.GetAreaName][!H], [H][1082.GetAreaName][!H], [H][2421.GetAreaName][!H], [H][475.GetAreaName][!H], "
                "[H][469.GetAreaName][!H], [H][465.GetAreaName][!H] areas"
    },

    {
        "tag": 'EET',
        "name": 'kato_germania',
        "culture_group": 'germanic',
        "primary_culture": 'dutch',
        "desc": "Germania Inferior or Kato Germania was an important border province during the time of the Ancient "
                "Roman Empire before falling to Germanic conquest. Now that it has been retaken, it would be better "
                "managed under an [Root.GetAdjective]-led Exarch in cooperation with the local elite.",
        "land": "[H][98.GetRegionName][!H] region"
    },
    {
        "tag": 'EEU',
        "name": 'megali_germania',
        "culture_group": 'germanic',
        "primary_culture": 'saxon',
        "desc": "Magna Germania or Megali Germania was once inhabited by the most fearsome of the Germanic tribes, "
                "many of whom eventually settled in the lands of the former Western Roman Empire. Now that it has been "
                "finally taken over, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation "
                "with the local elite.",
        "land": "[H][50.GetRegionName][!H] region, except for the following areas: [A][60.GetAreaName][!A], "
                "[A][266.GetAreaName][!A], [A][267.GetAreaName][!A], [A][265.GetAreaName][!A]"
    },
    {
        "tag": 'EEV',
        "name": 'vendia',
        "culture_group": 'west_slavic',
        "primary_culture": 'polish',
        "desc": "Vendia was a dangerous land far from the borders of the Roman Empire in which monsters and monster "
                "slayers were said to have fought an ever losing battle against the march of time. Now that it has "
                "been taken over, it would be better managed under an [Root.GetAdjective]-led Exarch in cooperation "
                "with the local elite.",
        "land": "[H][262.GetRegionName][!H] region and the following areas: [H][60.GetAreaName][!H], [H][266.GetAreaName][!H], "
                "[H][267.GetAreaName][!H], [H][265.GetAreaName][!H], [H][1772.GetAreaName][!H]"
    },
    {
        "tag": 'EEQ',
        "name": 'arabia',
        "culture_group": 'turko_semitic',
        "primary_culture": 'hejazi_culture',
        "desc": "The deserts of the Arabian Peninsula once unleashed an army that conquered half our empire in a holy "
                "fury. Now, however, we have a foothold in this land, the birthplace of Islam. Now that we are in "
                "control, we find that it would be better managed under an [Root.GetAdjective]-led Exarch in "
                "cooperation with the local elite.",
        "land": "[H][385.GetRegionName][!H] region"
    },
    {
        "tag": 'EEP',
        "name": 'perses',
        "culture_group": 'iranian',
        "primary_culture": 'persian',
        "desc": "Persia, our most ancient foe, falters at our spears. This land, lying once beyond our farthest "
                "borders, is now within our dominion. To lessen the threat of rebellion, we should appoint "
                "an [Root.GetAdjective]-led Exarch to govern the land in cooperation with the local elite.",
        "land": "[H][429.GetRegionName][!H] and [H][446.GetRegionName][!H] regions and [H][440.GetAreaName][!H], "
                "[H][442.GetAreaName][!H], [H][1968.GetAreaName][!H], [H][437.GetAreaName][!H] areas"
    },
    {
        "tag": 'EEY',
        "name": 'illyris',
        "land": "[H][145.GetRegionName][!H] region, except for the following areas: [A][145.GetAreaName][!A], "
                "[A][147.GetAreaName][!A], [A][148.GetAreaName][!A], "
                "[A][151.GetAreaName][!A], [A][164.GetAreaName][!A], [A][150.GetAreaName][!A], "
                "[A][159.GetAreaName][!A]"
    },
    {
        "tag": 'ELG',
        "name": 'konstantinia',
        "land": "[H][145.GetAreaName][!H], [H][147.GetAreaName][!H], [H][148.GetAreaName][!H], "
                "[H][151.GetAreaName][!H], [H][164.GetAreaName][!H], [H][150.GetAreaName][!H], "
                "[H][159.GetAreaName][!H] areas and provinces in [H][151.GetRegionName][!H] and "
                "[H][317.GetRegionName][!H] regions with [H]Greek[!H] or [H]Pontic[!H] culture. They will NOT "
                "receive [H][151.GetCapitalName][!H] itself"
    }
]