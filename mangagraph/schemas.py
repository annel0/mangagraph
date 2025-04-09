import dataclasses
from typing import Dict, Any, List, Optional

@dataclasses.dataclass
class Cover:
    thumbnail: str
    default: str
    md: str

@dataclasses.dataclass
class Rating:
    average: float
    votes: int
    raw_average: str
    raw_votes: str

@dataclasses.dataclass
class SearchData:
    id: int
    name: str
    rus_name: str
    eng_name: str
    slug: str
    slug_url: str
    cover: Cover
    age_restriction: str
    type: str
    release_year: str
    rating: Rating
    status: str
    tags: list[str]
    
    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'SearchData':
        """Create SearchData instance from API response dictionary."""
        cover_data = data.get('cover', {})
        cover = Cover(
            thumbnail=cover_data.get('thumbnail', ''),
            default=cover_data.get('default', ''),
            md=cover_data.get('md', '')
        )
        
        rating_data = data.get('rating', {})
        rating = Rating(
            average=float(rating_data.get('average', 0)),
            votes=int(rating_data.get('votes', 0)),
            raw_average=rating_data.get('averageFormated', 'N/A'),
            raw_votes=rating_data.get('votesFormated', 'N/A')
        )
        
        return cls(
            id=data.get('id', 0),
            name=data.get('name', 'Unknown'),
            rus_name=data.get('rus_name', ''),
            eng_name=data.get('eng_name', ''),
            slug=data.get('slug', ''),
            slug_url=data.get('slug_url', ''),
            cover=cover,
            age_restriction=data.get('ageRestriction', {}).get('label', 'Unknown'),
            type=data.get('type', {}).get('label', 'Unknown'),
            release_year=data.get('releaseDate', 'Unknown'),
            rating=rating,
            status=data.get('status', {}).get('label', 'Unknown'),
            tags=data.get('tags', [])
        )

@dataclasses.dataclass
class Cover:
    thumbnail: str = ''
    default: str = ''
    md: str = ''
    filename: Optional[str] = None

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Cover':
        return cls(
            thumbnail=data.get('thumbnail', ''),
            default=data.get('default', ''),
            md=data.get('md', ''),
            filename=data.get('filename', None)
        )

@dataclasses.dataclass
class Background:
    filename: Optional[str] = None
    url: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Background':
        return cls(
            filename=data.get('filename', None),
            url=data.get('url', '')
        )

@dataclasses.dataclass
class AgeRestriction:
    id: int = 0
    label: str = 'Unknown'

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'AgeRestriction':
        return cls(
            id=data.get('id', 0),
            label=data.get('label', 'Unknown')
        )

@dataclasses.dataclass
class ContentType:
    id: int = 0
    label: str = 'Unknown'

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'ContentType':
        return cls(
            id=data.get('id', 0),
            label=data.get('label', 'Unknown')
        )

@dataclasses.dataclass
class Views:
    total: int = 0
    short: str = ''
    formated: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Views':
        return cls(
            total=int(data.get('total', 0)),
            short=data.get('short', ''),
            formated=data.get('formated', '')
        )

@dataclasses.dataclass
class Rating:
    average: float = 0.0
    averageFormated: str = 'N/A'
    votes: int = 0
    votesFormated: str = 'N/A'
    user: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Rating':
        return cls(
            average=float(data.get('average', 0.0) or 0.0), # Обработка случая, когда average может быть None или пустой строкой
            averageFormated=data.get('averageFormated', 'N/A'),
            votes=int(data.get('votes', 0)),
            votesFormated=data.get('votesFormated', 'N/A'),
            user=int(data.get('user', 0))
        )

@dataclasses.dataclass
class Moderated:
    id: int = 0
    label: str = 'Unknown'

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Moderated':
        return cls(
            id=data.get('id', 0),
            label=data.get('label', 'Unknown')
        )

@dataclasses.dataclass
class TeamCover:
    filename: str = ''
    thumbnail: str = ''
    default: str = ''
    md: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'TeamCover':
        return cls(
            filename=data.get('filename', ''),
            thumbnail=data.get('thumbnail', ''),
            default=data.get('default', ''),
            md=data.get('md', '')
        )

@dataclasses.dataclass
class TeamDetails:
    branch_id: Optional[int] = None
    is_active: bool = False
    subscriptions_count: Optional[int] = None

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'TeamDetails':
        return cls(
            branch_id=data.get('branch_id', None),
            is_active=data.get('is_active', False),
            subscriptions_count=data.get('subscriptions_count', None)
        )

@dataclasses.dataclass
class Team:
    id: int = 0
    slug: str = ''
    slug_url: str = ''
    model: str = ''
    name: str = ''
    cover: TeamCover = dataclasses.field(default_factory=TeamCover)
    details: TeamDetails = dataclasses.field(default_factory=TeamDetails)
    donate_enabled: bool = False

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Team':
        cover_data = data.get('cover', {})
        cover = TeamCover.de_json(cover_data)
        details_data = data.get('details', {})
        details = TeamDetails.de_json(details_data)
        return cls(
            id=data.get('id', 0),
            slug=data.get('slug', ''),
            slug_url=data.get('slug_url', ''),
            model=data.get('model', ''),
            name=data.get('name', ''),
            cover=cover,
            details=details,
            donate_enabled=data.get('donate_enabled', False)
        )

@dataclasses.dataclass
class Genre:
    id: int = 0
    name: str = ''
    adult: bool = False
    alert: bool = False

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Genre':
        return cls(
            id=data.get('id', 0),
            name=data.get('name', ''),
            adult=data.get('adult', False),
            alert=data.get('alert', False)
        )

@dataclasses.dataclass
class Tag:
    id: int = 0
    name: str = ''
    adult: bool = False
    alert: bool = False

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Tag':
        return cls(
            id=data.get('id', 0),
            name=data.get('name', ''),
            adult=data.get('adult', False),
            alert=data.get('alert', False)
        )

@dataclasses.dataclass
class PublisherCover:
    filename: str = ''
    thumbnail: str = ''
    default: str = ''
    md: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'PublisherCover':
        return cls(
            filename=data.get('filename', ''),
            thumbnail=data.get('thumbnail', ''),
            default=data.get('default', ''),
            md=data.get('md', '')
        )

@dataclasses.dataclass
class Subscription:
    is_subscribed: bool = False
    source_type: str = ''
    source_id: int = 0
    relation: Optional[str] = None

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Subscription':
        return cls(
            is_subscribed=data.get('is_subscribed', False),
            source_type=data.get('source_type', ''),
            source_id=data.get('source_id', 0),
            relation=data.get('relation', None)
        )

@dataclasses.dataclass
class Publisher:
    id: int = 0
    slug: str = ''
    slug_url: str = ''
    model: str = ''
    name: str = ''
    rus_name: Optional[str] = None
    cover: PublisherCover = dataclasses.field(default_factory=PublisherCover)
    subscription: Subscription = dataclasses.field(default_factory=Subscription)

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Publisher':
        cover_data = data.get('cover', {})
        cover = PublisherCover.de_json(cover_data)
        subscription_data = data.get('subscription', {})
        subscription = Subscription.de_json(subscription_data)

        return cls(
            id=data.get('id', 0),
            slug=data.get('slug', ''),
            slug_url=data.get('slug_url', ''),
            model=data.get('model', ''),
            name=data.get('name', ''),
            rus_name=data.get('rus_name', None),
            cover=cover,
            subscription=subscription
        )

@dataclasses.dataclass
class AuthorCover:
    filename: Optional[str] = None
    thumbnail: str = ''
    default: str = ''
    md: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'AuthorCover':
        return cls(
            filename=data.get('filename', None),
            thumbnail=data.get('thumbnail', ''),
            default=data.get('default', ''),
            md=data.get('md', '')
        )

@dataclasses.dataclass
class AuthorSubscription:
    is_subscribed: bool = False
    source_type: str = ''
    source_id: int = 0
    relation: Optional[str] = None

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Subscription': # Используем Subscription, т.к. структура одинаковая
        return Subscription.de_json(data) # Просто делегируем Subscription.de_json

@dataclasses.dataclass
class Author:
    id: int = 0
    slug: str = ''
    slug_url: str = ''
    model: str = ''
    name: str = ''
    rus_name: Optional[str] = None
    alt_name: Optional[str] = None
    cover: AuthorCover = dataclasses.field(default_factory=AuthorCover)
    subscription: AuthorSubscription = dataclasses.field(default_factory=AuthorSubscription)
    confirmed: bool = False
    user_id: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Author':
        cover_data = data.get('cover', {})
        cover = AuthorCover.de_json(cover_data)
        subscription_data = data.get('subscription', {})
        subscription = AuthorSubscription.de_json(subscription_data) # Используем AuthorSubscription.de_json

        return cls(
            id=data.get('id', 0),
            slug=data.get('slug', ''),
            slug_url=data.get('slug_url', ''),
            model=data.get('model', ''),
            name=data.get('name', ''),
            rus_name=data.get('rus_name', None),
            alt_name=data.get('alt_name', None),
            cover=cover,
            subscription=subscription,
            confirmed=data.get('confirmed', False),
            user_id=data.get('user_id', 0)
        )

@dataclasses.dataclass
class Avatar:
    filename: str = ''
    url: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Avatar':
        return cls(
            filename=data.get('filename', ''),
            url=data.get('url', '')
        )

@dataclasses.dataclass
class Premium:
    enabled: bool = False

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Premium':
        return cls(
            enabled=data.get('enabled', False)
        )

@dataclasses.dataclass
class User:
    id: int = 0
    username: str = ''
    avatar: Avatar = dataclasses.field(default_factory=Avatar)
    last_online_at: Optional[str] = None
    premium: Premium = dataclasses.field(default_factory=Premium)

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'User':
        avatar_data = data.get('avatar', {})
        avatar = Avatar.de_json(avatar_data)
        premium_data = data.get('premium', {})
        premium = Premium.de_json(premium_data)
        return cls(
            id=data.get('id', 0),
            username=data.get('username', ''),
            avatar=avatar,
            last_online_at=data.get('last_online_at', None),
            premium=premium
        )

@dataclasses.dataclass
class CommentsDisabled:
    media: bool = False
    content: bool = False

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'CommentsDisabled':
        return cls(
            media=data.get('media', False),
            content=data.get('content', False)
        )

@dataclasses.dataclass
class CharactersCount:
    Main: int = 0
    Supporting: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'CharactersCount':
        return cls(
            Main=data.get('Main', 0),
            Supporting=data.get('Supporting', 0)
        )

@dataclasses.dataclass
class ReviewsCount:
    neutral: int = 0
    positive: int = 0
    negative: int = 0
    all: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'ReviewsCount':
        return cls(
            neutral=data.get('neutral', 0),
            positive=data.get('positive', 0),
            negative=data.get('negative', 0),
            all=data.get('all', 0)
        )

@dataclasses.dataclass
class Counts:
    branches: int = 0
    characters: CharactersCount = dataclasses.field(default_factory=CharactersCount)
    reviews: ReviewsCount = dataclasses.field(default_factory=ReviewsCount)
    relations: int = 0
    people: int = 0
    covers: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Counts':
        characters_data = data.get('characters', {})
        characters = CharactersCount.de_json(characters_data)
        reviews_data = data.get('reviews', {})
        reviews = ReviewsCount.de_json(reviews_data)
        return cls(
            branches=data.get('branches', 0),
            characters=characters,
            reviews=reviews,
            relations=data.get('relations', 0),
            people=data.get('people', 0),
            covers=data.get('covers', 0)
        )

@dataclasses.dataclass
class Metadata:
    close_comments: int = 0
    comments_disabled: CommentsDisabled = dataclasses.field(default_factory=CommentsDisabled)
    count: Counts = dataclasses.field(default_factory=Counts)

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Metadata':
        comments_disabled_data = data.get('comments_disabled', {})
        comments_disabled = CommentsDisabled.de_json(comments_disabled_data)
        count_data = data.get('count', {})
        count = Counts.de_json(count_data)
        return cls(
            close_comments=data.get('close_comments', 0),
            comments_disabled=comments_disabled,
            count=count
        )

@dataclasses.dataclass
class Status:
    id: int = 0
    label: str = 'Unknown'

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Status':
        return cls(
            id=data.get('id', 0),
            label=data.get('label', 'Unknown')
        )

@dataclasses.dataclass
class ItemsCount:
    uploaded: int = 0
    total: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'ItemsCount':
        return cls(
            uploaded=data.get('uploaded', 0),
            total=data.get('total', 0)
        )

@dataclasses.dataclass
class ScanlateStatus:
    id: int = 0
    label: str = 'Unknown'

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'ScanlateStatus':
        return cls(
            id=data.get('id', 0),
            label=data.get('label', 'Unknown')
        )

@dataclasses.dataclass
class ArtistCover:
    filename: Optional[str] = None
    thumbnail: str = ''
    default: str = ''
    md: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'ArtistCover':
        return cls(
            filename=data.get('filename', None),
            thumbnail=data.get('thumbnail', ''),
            default=data.get('default', ''),
            md=data.get('md', '')
        )

@dataclasses.dataclass
class ArtistSubscription:
    is_subscribed: bool = False
    source_type: str = ''
    source_id: int = 0
    relation: Optional[str] = None

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Subscription': # Используем Subscription, т.к. структура одинаковая
        return Subscription.de_json(data) # Просто делегируем Subscription.de_json

@dataclasses.dataclass
class Artist:
    id: int = 0
    slug: str = ''
    slug_url: str = ''
    model: str = ''
    name: str = ''
    rus_name: Optional[str] = None
    alt_name: Optional[str] = None
    cover: ArtistCover = dataclasses.field(default_factory=ArtistCover)
    subscription: ArtistSubscription = dataclasses.field(default_factory=ArtistSubscription)
    confirmed: bool = False
    user_id: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Artist':
        cover_data = data.get('cover', {})
        cover = ArtistCover.de_json(cover_data)
        subscription_data = data.get('subscription', {})
        subscription = ArtistSubscription.de_json(subscription_data) # Используем ArtistSubscription.de_json

        return cls(
            id=data.get('id', 0),
            slug=data.get('slug', ''),
            slug_url=data.get('slug_url', ''),
            model=data.get('model', ''),
            name=data.get('name', ''),
            rus_name=data.get('rus_name', None),
            alt_name=data.get('alt_name', None),
            cover=cover,
            subscription=subscription,
            confirmed=data.get('confirmed', False),
            user_id=data.get('user_id', 0)
        )

@dataclasses.dataclass
class FormatPivot:
    manga_id: int = 0
    format_id: int = 0

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'FormatPivot':
        return cls(
            manga_id=data.get('manga_id', 0),
            format_id=data.get('format_id', 0)
        )

@dataclasses.dataclass
class Format:
    id: int = 0
    name: str = ''
    pivot: FormatPivot = dataclasses.field(default_factory=FormatPivot)

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'Format':
        pivot_data = data.get('pivot', {})
        pivot = FormatPivot.de_json(pivot_data)
        return cls(
            id=data.get('id', 0),
            name=data.get('name', ''),
            pivot=pivot
        )


@dataclasses.dataclass
class MangaData:
    id: int = 0
    name: str = ''
    rus_name: str = ''
    eng_name: str = ''
    otherNames: List[str] = dataclasses.field(default_factory=list)
    model: str = ''
    slug: str = ''
    slug_url: str = ''
    cover: Cover = dataclasses.field(default_factory=Cover)
    background: Background = dataclasses.field(default_factory=Background)
    ageRestriction: AgeRestriction = dataclasses.field(default_factory=AgeRestriction)
    site: int = 0
    type: ContentType = dataclasses.field(default_factory=ContentType)
    summary: str = ''
    close_view: int = 0
    releaseDate: str = 'Unknown'
    views: Views = dataclasses.field(default_factory=Views)
    rating: Rating = dataclasses.field(default_factory=Rating)
    is_licensed: bool = False
    moderated: Moderated = dataclasses.field(default_factory=Moderated)
    teams: List[Team] = dataclasses.field(default_factory=list)
    genres: List[Genre] = dataclasses.field(default_factory=list)
    tags: List[Tag] = dataclasses.field(default_factory=list)
    publisher: List[Publisher] = dataclasses.field(default_factory=list)
    franchise: List[Any] = dataclasses.field(default_factory=list) # Тип Any, так как франшиза пустая в примере
    authors: List[Author] = dataclasses.field(default_factory=list)
    user: User = dataclasses.field(default_factory=User)
    metadata: Metadata = dataclasses.field(default_factory=Metadata)
    status: Status = dataclasses.field(default_factory=Status)
    items_count: ItemsCount = dataclasses.field(default_factory=ItemsCount)
    scanlateStatus: ScanlateStatus = dataclasses.field(default_factory=ScanlateStatus)
    artists: List[Artist] = dataclasses.field(default_factory=list)
    format: List[Format] = dataclasses.field(default_factory=list)
    releaseDateString: str = ''

    @classmethod
    def de_json(cls, data: Dict[str, Any]) -> 'MangaData':
        data_item = data.get('data', {}) # Получаем словарь из ключа 'data'
        cover_data = data_item.get('cover', {})
        cover = Cover.de_json(cover_data)
        background_data = data_item.get('background', {})
        background = Background.de_json(background_data)
        age_restriction_data = data_item.get('ageRestriction', {})
        age_restriction = AgeRestriction.de_json(age_restriction_data)
        type_data = data_item.get('type', {})
        content_type = ContentType.de_json(type_data)
        views_data = data_item.get('views', {})
        views = Views.de_json(views_data)
        rating_data = data_item.get('rating', {})
        rating = Rating.de_json(rating_data)
        moderated_data = data_item.get('moderated', {})
        moderated = Moderated.de_json(moderated_data)
        teams_data = data_item.get('teams', [])
        teams = [Team.de_json(team_item) for team_item in teams_data]
        genres_data = data_item.get('genres', [])
        genres = [Genre.de_json(genre_item) for genre_item in genres_data]
        tags_data = data_item.get('tags', [])
        tags = [Tag.de_json(tag_item) for tag_item in tags_data]
        publisher_data = data_item.get('publisher', [])
        publishers = [Publisher.de_json(publisher_item) for publisher_item in publisher_data]
        authors_data = data_item.get('authors', [])
        authors = [Author.de_json(author_item) for author_item in authors_data]
        user_data = data_item.get('user', {})
        user = User.de_json(user_data)
        metadata_data = data_item.get('metadata', {})
        metadata = Metadata.de_json(metadata_data)
        status_data = data_item.get('status', {})
        status = Status.de_json(status_data)
        items_count_data = data_item.get('items_count', {})
        items_count = ItemsCount.de_json(items_count_data)
        scanlate_status_data = data_item.get('scanlateStatus', {})
        scanlate_status = ScanlateStatus.de_json(scanlate_status_data)
        artists_data = data_item.get('artists', [])
        artists = [Artist.de_json(artist_item) for artist_item in artists_data]
        format_data = data_item.get('format', [])
        formats = [Format.de_json(format_item) for format_item in format_data]


        return cls(
            id=data_item.get('id', 0),
            name=data_item.get('name', 'Unknown'),
            rus_name=data_item.get('rus_name', ''),
            eng_name=data_item.get('eng_name', ''),
            otherNames=data_item.get('otherNames', []),
            model=data_item.get('model', ''),
            slug=data_item.get('slug', ''),
            slug_url=data_item.get('slug_url', ''),
            cover=cover,
            background=background,
            ageRestriction=age_restriction,
            site=data_item.get('site', 1),
            type=content_type,
            summary=data_item.get('summary', ''),
            close_view=data_item.get('close_view', 0),
            releaseDate=data_item.get('releaseDate', 'Unknown'),
            views=views,
            rating=rating,
            is_licensed=data_item.get('is_licensed', False),
            moderated=moderated,
            teams=teams,
            genres=genres,
            tags=tags,
            publisher=publishers,
            franchise=data_item.get('franchise', []),
            authors=authors,
            user=user,
            metadata=metadata,
            status=status,
            items_count=items_count,
            scanlateStatus=scanlate_status,
            artists=artists,
            format=formats,
            releaseDateString=data_item.get('releaseDateString', '')
        )