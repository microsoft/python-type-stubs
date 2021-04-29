# COMPLETE

import abc
from typing import (
    Any,
    Callable,
    ContextManager,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Literal,
    Optional,
    Protocol,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)

from matplotlib.artist import Artist
from matplotlib.figure import Figure

_Frame = TypeVar("_Frame")

class Animation(Generic[_Frame]):
    def __init__(self, fig: Figure, event_source: Optional[object] = ..., blit: bool = ...) -> None: ...
    def new_frame_seq(self) -> Iterator[_Frame]: ...
    def new_saved_frame_seq(self) -> Iterator[_Frame]: ...
    def save(
        self,
        filename: str,
        writer: Optional[Union[MovieWriter, str]],
        fps: Optional[int] = ...,
        dpi: Optional[Union[float, Literal['figure']]] = ...,
        codec: Optional[str] = ...,
        bitrate: Optional[int] = ...,
        extra_args: Optional[Sequence[str]] = ...,
        metadata: Optional[Dict[str, str]] = ...,
        extra_anim: Optional[Sequence[Animation[Any]]] = ...,
        savefig_kwargs: Optional[Dict[str, Any]] = ...,
        *,
        progress_callback: Optional[Callable[[int, int], Any]] = ...
    ) -> None: ...
    def to_html5_video(self, embed_limit: Optional[float] = ...) -> str: ...
    def to_jshtml(self, fps: Optional[int] = ..., embed_frames: bool = ..., default_mode: Optional[Literal['loop', 'once']] = ...) -> str: ...


class TimedAnimation(Animation[_Frame]):
    def __init__(
        self,
        fig: Figure,
        interval: int = ...,
        repeat_delay: int = ...,
        repeat: bool = ...,
        event_source: Optional[object] = ...,
        *args: Any,
        **kwarg: Any
    ) -> None: ...


class _AnimationFunc(Protocol[_Frame]):
    def __call__(self, frame: _Frame, *fargs: Any) -> Iterable[Artist]: ...

class FuncAnimation(TimedAnimation[_Frame]):
    def __init__(
        self,
        fig: Figure,
        func: _AnimationFunc[_Frame],
        frames: Optional[Union[Iterable[_Frame], int, Callable[[], Any]]] = ...,
        init_func: Optional[Callable[[], Iterable[_Frame]]] = ...,
        fargs: Optional[Tuple[Any, ...]] = ...,
        save_count: Optional[int] = ...,
        *,
        cache_frame_data: bool = ...,
        **kwargs: Any
    ) -> None: ...


class ArtistAnimation(TimedAnimation[Artist]):
    def __init__(
        self,
        fig: Figure,
        artists: Sequence[Artist],
        *args: Any,
        **kwargs: Any
    ) -> None: ...

_T = TypeVar("_T", bound=AbstractMovieWriter)

class AbstractMovieWriter(abc.ABC):
    def __init__(
        self,
        fps: int = ...,
        metadata: Optional[Dict[str, str]] = ...,
        codec: Optional[str] = ...,
        bitrate: Optional[int] = ...
    ) -> None: ...

    @abc.abstractmethod
    def setup(self, fig: Figure, outfile: str, dpi: Optional[float] = ...) -> None: ...

    @property
    def frame_size(self) -> Tuple[int, int]: ...

    @abc.abstractmethod
    def grab_frame(self, **savefig_kwargs: Any) -> None: ...

    @abc.abstractmethod
    def finish(self) -> None: ...

    def saving(self: _T, fig: Figure, outfile: str, dpi: float, *args: Any, **kwargs: Any) -> ContextManager[_T]: ...

class MovieWriter(AbstractMovieWriter):
    def __init__(
        self,
        fps: int = ...,
        codec: Optional[str] = ...,
        bitrate:  Optional[int] = ...,
        extra_args: Optional[Sequence[str]] = ...,
        metadata: Optional[Dict[str, str]] = ...
    ) -> None: ...

    @classmethod
    def bin_path(cls) -> str: ...

    @classmethod
    def isAvailable(cls) -> bool: ...

class FileMovieWriter(MovieWriter):
    ...

class PillowWriter(AbstractMovieWriter):
    @classmethod
    def isAvailable(cls) -> bool: ...

class HTMLWriter(FileMovieWriter):
    supported_formats: List[str]

    def __init__(
        self,
        fps: int = ...,
        codec: Optional[str] = ...,
        bitrate:  Optional[int] = ...,
        extra_args: Optional[Sequence[str]] = ...,
        metadata: Optional[Dict[str, str]] = ...,
        embed_frames: bool = ...,
        default_mode: Literal['loop', 'once', 'reflect'] = ...,
        embed_limit: Optional[int] = ...
    ) -> None: ...

    @classmethod
    def isAvailable(cls) -> bool: ...

class FFMpegBase:
    @property
    def output_args(self) -> List[str]: ...

    @classmethod
    def isAvailable(cls) -> bool: ...

class FFMpegWriter(FFMpegBase, MovieWriter): ...

class FFMpegFileWriter(FFMpegBase, FileMovieWriter):
    supported_formats: List[str]

class AVConvBase(FFMpegBase): ...

class AVConvWriter(AVConvBase, FFMpegWriter): ...

class AVConvFileWriter(AVConvBase, FFMpegFileWriter): ...

class ImageMagickBase:
    @property
    def delay(self) -> float: ...

    @property
    def output_args(self) -> List[str]: ...

    @classmethod
    def bin_path(cls) -> str: ...

    @classmethod
    def isAvailable(cls) -> bool: ...

class ImageMagickWriter(ImageMagickBase, MovieWriter): ...

class ImageMagickFileWriter(ImageMagickBase, FileMovieWriter):
    supported_formats: List[str]


class MovieWriterRegistry:
    def ensure_not_dirty(self) -> None: ...
    def is_available(self, name: str) -> bool: ...
    def list(self) -> List[MovieWriter]: ...
    def register(self, name: str) -> Any: ...  # TODO: ParamSpec
    def reset_available_writers(self) -> None: ...
    def set_dirty(self) -> None: ...

    def __iter__(self) -> Iterator[MovieWriter]: ...
    def __getitem__(self, name: str) -> MovieWriter: ...

    @property
    def avail(self) -> Dict[str, MovieWriter]: ...
