"""Views for Introduction."""
from ._builtin import Page


class ExperimentIntroduction(Page):
    """
    Page introducing the entire experiment.

    Assumes this is the first test.
    """

    pass


class GamesIntroduction(Page):
    """Page introducing the games. Assumes this is the first test."""

    pass


page_sequence = [
    ExperimentIntroduction,
    GamesIntroduction
]
