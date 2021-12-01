import time
import discord
import math
from Client import AsturaClient

class Utilities:
    def __init__(self, client: AsturaClient) -> None:
        self.client: AsturaClient = client

    def embed(options) -> discord.Embed:
        return discord.Embed(author = options.author, colour = options.colour, description = options.description, fields = options.fields, footer = options.footer, image = options.image, provider = options.provider, thumbnail = options.thumbnail, timestamp = options.timestamp, title = options.title, type = options.type, url = options.url, video = options.video)

    def pages(array: list[any], itemsPerPage: int, page: int = 1) -> list:
        maxPages: int = math.ceil(len(array) / itemsPerPage)
        if (page > 1 or page > maxPages): return None
        return array[(page - 1) * itemsPerPage : page * itemsPerPage]

    def getTime() -> time.struct_time:
        return time.gmtime()

    def convertFromMS(ms: int, ignoreDays: bool, format: str, trim: str) -> str | any:
        seconds: str = str(math.floor((ms / 1000) % 60))
        minutes: str = str(math.floor((ms / (1000 * 60)) % 60))
        hours: str = str(math.floor((ms / (1000 * 60 * 60)) % 60))
        days: str = str(math.floor((ms / (1000 * 60 * 60 * 24)) % 60))

        if format == "d:h:m:s" and ignoreDays:
            if hours.zfill(2) != "00 " and trim == "max":
                return "{}:{}:{}".format(hours.zfill(2), minutes.zfill(2), seconds.zfill(2))
            else:
                return "{}:{}".format(minutes, seconds)
        elif format == "d:h:m:s" and not ignoreDays:
            return "{}:{}:{}:{}".format(days.zfill(1), hours.zfill(2), minutes.zfill(2), seconds.zfill(2))
        elif format == "dd, hh, mm, ss" and ignoreDays:
            if hours.zfill(1) != "00 " and trim == "max":
                return "{}d, {}h, {}m, {}s".format(days.zfill(1), hours.zfill(2), minutes.zfill(2), seconds.zfill(2))
            else:
                return "{}h, {}m, {}s".format(hours.zfill(2), minutes.zfill(2), seconds.zfill(2))
        else:
            return "{}d, {}h, {}m, {}s".format(days.zfill(1), hours.zfill(2), minutes.zfill(2), seconds.zfill(2))

    def padStart(number: int, digits: int = 2, emptyDigit: int = 0) -> int:
        length: int = 0
        n: int = abs(number)
        absoluteNumber: int = n

        while n >= 1:
            n /= 10
            length += 1

        prefix = list(max((digits - length) + 1, 0)).join(emptyDigit)
        
        if number < 0:
            return "-${}${}".format(prefix, absoluteNumber)
        else:
            return prefix + number
