from enum import Enum


class FriendStatus(Enum):
    '''Choices for friendship status'''
    PENDING = 1
    ACCEPTED = 2
    DENIED = 3


class Reactions(Enum):
    '''Different reactions to posts and projects'''
    LIKE = 1
    DISLIKE = 2
    LOVE = 3
    SAD = 4
    LAUGH = 5
