import os

__all__ = [
    "SCMLAGENTS_FASTRUN",
    "SCMLAGENTS_RUN2019",
    "SCMLAGENTS_RUN2020",
    "SCMLAGENTS_RUN2021",
    "SCMLAGENTS_RUN2021_TOURNAMENT",
    "SCMLAGENTS_RUN2021_ONESHOT",
    "SCMLAGENTS_RUN2021_ONESHOT_SYNC",
    "SCMLAGENTS_RUN2021_STD",
    "SCMLAGENTS_RUN_GENIUS",
    "SCMLAGENTS_RUN_TOURNAMENTS",
    "SCMLAGENTS_RUN_STD_TOURNAMENTS",
    "SCMLAGENTS_RUN_COLLUSION_TOURNAMENTS",
    "SCMLAGENTS_RUN_SABOTAGE_TOURNAMENTS",
    "SCMLAGENTS_RUN_TEMP_FAILING",
]

SCMLAGENTS_ON_GITHUB = (os.environ.get("GITHUB_ACTIONS", False),)
SCMLAGENTS_FASTRUN = os.environ.get("SCMLAGENTS_FASTRUN", SCMLAGENTS_ON_GITHUB)
SCMLAGENTS_RUN_TEMP_FAILING = os.environ.get("SCMLAGENTS_RUN_TEMP_FAILING", False)
SCMLAGENTS_RUN2021_ONESHOT = os.environ.get("SCMLAGENTS_RUN2021_ONESHOT", True)
SCMLAGENTS_RUN2021_STD = os.environ.get("SCMLAGENTS_RUN2021_STD", True)
SCMLAGENTS_RUN_GENIUS = os.environ.get("SCMLAGENTS_RUN_GENIUS", not SCMLAGENTS_FASTRUN)
SCMLAGENTS_RUN_TOURNAMENTS = os.environ.get(
    "SCMLAGENTS_RUN_TOURNAMENTS", not SCMLAGENTS_FASTRUN
)
SCMLAGENTS_RUN_STD_TOURNAMENTS = os.environ.get(
    "SCMLAGENTS_RUN_STD_TOURNAMENTS", not SCMLAGENTS_RUN_TOURNAMENTS
)
SCMLAGENTS_RUN_COLLUSION_TOURNAMENTS = os.environ.get(
    "SCMLAGENTS_RUN_COLLUSION_TOURNAMENTS", not SCMLAGENTS_RUN_TOURNAMENTS
)
SCMLAGENTS_RUN_SABOTAGE_TOURNAMENTS = os.environ.get(
    "SCMLAGENTS_RUN_SABOTAGE_TOURNAMENTS", not SCMLAGENTS_RUN_TOURNAMENTS
)

SCMLAGENTS_RUN2021_TOURNAMENT = os.environ.get(
    "SCMLAGENTS_RUN2021_TOURNAMENT", not SCMLAGENTS_FASTRUN
)
SCMLAGENTS_RUN2021_ONESHOT_SYNC = os.environ.get(
    "SCMLAGENTS_RUN2021_ONESHOT_SYNC", not SCMLAGENTS_FASTRUN
)

SCMLAGENTS_RUN2019 = os.environ.get("SCMLAGENTS_RUN2019", not SCMLAGENTS_FASTRUN)
SCMLAGENTS_RUN2020 = os.environ.get("SCMLAGENTS_RUN2020", not SCMLAGENTS_FASTRUN)
SCMLAGENTS_RUN2021 = os.environ.get("SCMLAGENTS_RUN2021", True)
