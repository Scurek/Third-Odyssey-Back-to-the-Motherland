"""
Constants definitions used by `localisation_search.py`.
Changes to this file may affect the quality of the output.
"""

GROUP_MIN_SIZE = 6  # Minimum size of groups, when sorting by group

# Subdirectories within the mod to exclude from search
EXCLUDED_SUBDIRS = [
    'localisation',  # Of course, if we don't exclude localisation, we'll find all!
    'gfx',
    'history',
    'interface',
    'sound',
    'common/units',  # Contain no localisation
    'common/countries',  # Contain no localisation
]

# Categories sorted by appearance instead of alphabetically
CAT_SORT_BY_APPEARANCE = [
    'events',
]

# Maps categories (subdirs of mod/vanilla) to prefix/suffix combinations that may apply on localisation.
CAT_VARIANTS_PREFIX_SUFFIX_MAP = {
    'common/event_modifiers': [('desc_', ''), ],
    'common/triggered_modifiers': [('desc_', '')],
    'common/province_triggered_modifiers': [('desc_', ''), ],
    'decisions': [('', '_desc'), ('', '_title')],
    'common/tradegoods': [('', 'DESC')],
    'common/governments': [
        ('', '_desc'),
        ('', '_name'),
    ],
    'common/government_names': [
        # Note: not all of these may still be used in current EU4
        ('', '_desc'),
        ('', '_ruler'),
        ('', '_ruler_female'),
        ('', '_vassal'),
        ('', '_ruler_vassal'),
        ('', '_long_desc'),
        ('', '_is_our'),
        ('', '_title'),
        ('', '_title_plural')
    ],
    'common/subject_types': [
        # Note: Assume same as government names?
        ('', '_desc'),
        ('', '_ruler'),
        ('', '_ruler_female'),
        ('', '_vassal'),
        ('', '_ruler_vassal'),
        ('', '_long_desc'),
        ('', '_is_our'),
        ('', '_title'),
        ('', '_title_plural'),
    ],
    'common/rebel_types': [
        ('', '_army'),
        ('', '_name'),
        ('', '_title'),
        ('', '_desc'),
        ('', '_demand_desc'),
    ],
    'common/ideas': [('', '_start'), ('', '_bonus'), ('', '_desc')],
    'common/country_tags': [('', '_ADJ')],
    'common/personal_deities': [('', '_desc')],
    'common/estates': [('', '_desc')],
    'common/estate_privileges': [('', '_desc')],
    'missions': [('', '_desc'), ('', '_title')],
    'common/factions': [('', '_FACTION_DESC'), ('', '_influence')],
    'common/government_reforms': [('mechanic_', ''), ('mechanic_', '_yes'), ('mechanic_', '_no'),('', '_desc')],
    'common/peace_treaties': [
        ('', '_desc'),
        ('PEACE_', ''),
        ('CB_ALLOWED_', ''),
    ],
    'common/cb_types': [('', '_desc')],
    'common/policies': [('desc_', '')],
    'common/religions': [
        ('desc_', ''),  # Orthodox icons are in religion file, description localisations preceded by 'desc_'
        ('', '_religion_desc'),
    ],
    'common': [
        ('', '_desc'),  # Tech groups in common/technology.txt
    ],
    'common/technologies': [
        ('', 'DESCR'),  # Unit types are present in military techs
    ],
    'common/advisortypes': [('', '_desc')],
    'common/disasters': [('', '_desc')],
    'common/new_diplomatic_actions': [('', '_title'), ('', '_desc'), ('', '_tooltip'), ('', '_dialog')],
    'common/flagship_modifications': [('', '_desc')],
    'common/great_projects': [('great_project_', '')],
    'common/naval_doctrines': [('', '_desc')],
    'common/ruler_personalities': [('desc_', ''), ('', '_die_desc')],
    'common/government_mechanics': [('', '_desc'), ('monthly_', '')],
    'common/ages': [('', '_desc')]
}

CAT_PRIORITIES_MAP = {
    # Greater values -> later in sorting (sorting defaults to ascending order)
    'common/country_tags': -140,
    'common': -130,  # Graphical culture type, technologies
    'common/tradegoods': -120,
    'common/religions': -116,  # Referred to in personal_deities
    'common/personal_deities': -115,  # Some names in cultures are deities
    'common/cultures': -110,
    'common/opinion_modifiers': -102,
    'common/province_modifiers': -101,
    'common/event_modifiers': -100,
    'common/ideas': -90,
    'common/subject_types': -80,
    'common/government_names': -75,
    'common/government_reforms': -74,
    'common/governments': -73,
    'common/estates': -70,
    'common/estate_privileges': -69,
    'common/disasters': -60,
    'common/triggered_modifiers': 90,  # May contain all kinds of stuff
    'events': 100,  # May contain all kinds of stuff  (NOTE: maybe not an issue to put at latest, since event localisations != unlocalised event identifier?)
    'decisions': 110,  # May trigger events and contain all kinds of conditions
    'missions': 120,  # May trigger events and contain all kinds of conditions  (NOTE: are missions used as conditions?)
    'common/on_actions': 130,  # Contains no localisation itself
}
