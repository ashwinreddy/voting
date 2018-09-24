import numpy as np

class Method(object):
    """Superclass for all voting algorithms
    """
    def __init__(self, preference_schedule):
        """Set preference schedule for this class
        """
        self.preference_schedule = preference_schedule
        self.points = np.zeros(self.preference_schedule.number_of_candidates)

    def _loop_through_preferences(self, func):
        """Allows subclasses to easily loop through all preferences, a common occurence
        """
        for preference in self.preference_schedule.votes:
            number_of_votes = preference[0]
            ballot_order = preference[1:]

            func(number_of_votes, ballot_order)

    def _compute_ranking(self):
        """This method finds a ranking of all candidates
        By default, Method is set up to need 1 run-through of the preferences.
        """
        self._loop_through_preferences(self._parse_ballot)
        
    def _parse_ballot(self):
        pass
    
    def _idx_to_name(self, idx):
        """A bidirectional map relating names and indices
        """
        return self.preference_schedule.name_idx_map[idx]

    @property
    def winner(self):
        """This method sets a property for the winner by first computing the winner via `_compute_ranking()`
        """
        self._compute_ranking()
        return self._idx_to_name(np.argmax(self.points))
