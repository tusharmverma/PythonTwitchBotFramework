from enum import Enum, IntFlag, auto

__all__ = ('Event', 'CommandContext', 'MessageType', 'UserType')


class NamedEnum(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self


class UserType(NamedEnum):
    GLOBAL_MOD = auto()
    ADMIN = auto()
    STAFF = auto()
    AFFILIATE = auto()
    NORMAL = auto()


class MessageType(NamedEnum):
    PRIVMSG = auto()
    WHISPER = auto()
    COMMAND = auto()
    PING = auto()
    USER_JOIN = auto()
    USER_PART = auto()
    SUBSCRIPTION = auto()
    RAID = auto()
    USER_NOTICE = auto()
    CHANNEL_POINTS_REDEMPTION = auto()
    BITS = auto()
    NONE = auto()


class CommandContext(IntFlag):
    CHANNEL = auto()
    WHISPER = auto()
    BOTH = CHANNEL | WHISPER


class Event(NamedEnum):
    on_before_command_execute = auto()
    on_after_command_execute = auto()
    on_bits_donated = auto()
    on_channel_subscription = auto()
    on_channel_raided = auto()
    on_channel_joined = auto()
    on_connected = auto()
    on_privmsg_received = auto()
    on_privmsg_sent = auto()
    on_whisper_received = auto()
    on_whisper_sent = auto()
    on_permission_check = auto()
    on_raw_message = auto()
    on_user_join = auto()
    on_user_part = auto()
    on_mod_reloaded = auto()
    on_channel_points_redemption = auto()
