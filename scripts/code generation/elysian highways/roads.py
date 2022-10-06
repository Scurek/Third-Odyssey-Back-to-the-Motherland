roads = [
    {
        "name": "north_apaleisian",
        "has_mission_trigger": True,
        "has_add_modifiers": True,
        "has_ownership_check": True,
        "no_decision": True,
        "provinces": [
            {"id": 2551},
            # {"id": 2555},
            {"id": 948},
            {"id": 2525},
            {"id": 2526},
            {"id": 940},
            {"id": 4921},
            {"id": 2520},
            {"id": 4904},
        ]
    },
    {
        "name": "south_apaleisian",
        "has_mission_trigger": True,
        "has_add_modifiers": True,
        "has_ownership_check": True,
        "no_decision": True,
        "provinces": [
            # {"id": 935},
            # {"id": 2527},
            {"id": 2531},
            {"id": 4883},
            {"id": 918},
            {"id": 939},
            {"id": 4887},
            {"id": 2520, "duplicate": True},
            {"id": 4904, "duplicate": True},
            # {"id": 2514},
            # {"id": 900},
        ]
    },
    {
        "name": "south",
        "tier": 1,
        "cost": 500,
        "requires_build": [
            917
        ],
        "provinces": [
            {"id": 2528},
            {"id": 2529},
            {"id": 4884},
            {"id": 921},
            {"id": 893},
        ]
    },
    {
        "name": "coastal",
        "tier": 2,
        "cost": 1500,
        "requires_build": [
            4887, 918, 2528, 2529, 4884
        ],
        "provinces": [
            {"id": 2530},
            {"id": 922},
            {"id": 923},
            {"id": 2533},
            {"id": 4881},
            {"id": 2539},
            {"id": 929},
            {"id": 2542},
            {"id": 932},
            {"id": 2543},
            {"id": 2546},
            {"id": 938},
            {"id": 2547},
            {"id": 950},
            {"id": 952},
            {"id": 2550},
            # {"id": 953},
        ]
    },
    {
        "name": "vinlandic",
        "tier": 2,
        "cost": 1000,
        "requires_build": [
            953
        ],
        "provinces": [
            # {"id": 953, "duplicate": True},
            {"id": 2554},
            {"id": 956},
            {"id": 2639},
            {"id": 965},
            {"id": 963},
            {"id": 2559},
            {"id": 2584},
            {"id": 993},
            {"id": 990},
            {"id": 994},
        ]
    },
    {
        "name": "north",
        "tier": 1,
        "cost": 800,
        "requires_build": [
            917
        ],
        "provinces": [
            # {"id": 917},
            {"id": 915},
            {"id": 4903},
            {"id": 913},
            {"id": 2518},
            {"id": 2517},
            {"id": 908},
            {"id": 2016},
            {"id": 1008}
        ]
    },
    {
        "name": "west",
        "tier": 3,
        "cost": 2500,
        "requires_build": [
            4887, 918, 2528
        ],
        "provinces": [
            {"id": 895},
            {"id": 894},
            {"id": 4911},
            {"id": 886},
            {"id": 4909},
            {"id": 2500},
            {"id": 2497},
            {"id": 4628},
            {"id": 881},
            {"id": 2492},
            {"id": 879},
            {"id": 4633},
            {"id": 877},
            {"id": 876},
            {"id": 867},
            {"id": 5368},
            {"id": 5394},
            {"id": 868},
            {"id": 5387},
            {"id": 2478},
            {"id": 870},
            {"id": 5364},
            {"id": 2021}
        ]
    },
    {
        "name": "atlas",
        "tier": 3,
        "cost": 2500,
        "requires_build": [
            917
        ],
        "provinces": [
            # {"id": 917, "duplicate": True},
            {"id": 4906},
            {"id": 902},
            {"id": 898},
            {"id": 903},
            {"id": 4916},
            {"id": 2009},
            {"id": 1809},
            {"id": 2506},
            {"id": 5402},
            {"id": 2490},
            {"id": 5374},
            {"id": 5404},
            {"id": 5383},
            {"id": 5380},
            {"id": 5386},
            {"id": 5371},
            {"id": 2480},
            {"id": 5365},
            {"id": 5363},
            {"id": 2021, "duplicate": True}
        ]
    }
]
