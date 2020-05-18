AREAS = {
    "rat_cave":
        {
            "name": "Rat Cave",
            "rooms":
                {
                    "1_1":
                    {
                        "monster": "rat",
                        "next_rooms": ["2_1", "2_2"],
                        "tiers": [
                            {1: 100}
                        ],
                        "explored": False
                    },
                    "2_1":
                    {
                        "monster": "rat",
                        "next_rooms": ["4_2"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    },
                    "2_2":
                    {
                        "monster": "bat",
                        "next_rooms": ["3_1", "3_2"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    },
                    "3_1":
                    {
                        "monster": "bat",
                        "next_rooms": ["4_2"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    },
                    "3_2":
                    {
                        "monster": "bat",
                        "next_rooms": ["4_1"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    },
                    "4_1":
                    {
                        "monster": "bat",
                        "next_rooms": ["5_1"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    }
                    ,
                    "4_2":
                    {
                        "monster": "bat",
                        "next_rooms": ["6_1"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    },
                    "5_1":
                    {
                        "monster": "bat",
                        "next_rooms": ["6_1"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    },
                    "6_1":
                    {
                        "monster": "bat",
                        "next_rooms": ["7_1"],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    },
                    "7_1":
                    {
                        "monster": "bat",
                        "next_rooms": [],
                        "tiers": [
                            {1: 80},
                            {2: 20}
                        ],
                        "explored": False
                    }
                }
        }
}
