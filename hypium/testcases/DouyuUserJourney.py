import os

from devicetest.core.test_case import Step, TestCase
from hypium import BY, UiDriver
from hypium.model import KeyCode


class DouyuUserJourney(TestCase):
    """Exercise a realistic Douyu PC journey without requiring login."""

    BUNDLE = "com.douyu.ho.app"
    ABILITY = "EntryAbility"
    VIDEO_KEY = "gesture_play"
    MINIMIZE_KEY = "EnhanceMinimizeBtn"
    CLOSE_KEY = "EnhanceCloseBtn"

    ROOM_TITLES = (
        "【PIGFF】神箭手的直播间",
        "这是一个直播间 2448877",
        "我爱露营，我爱爬山",
        "轰轰：每天下午两点不见不散！",
        "【双倍】下午登基7点开黑",
    )

    def __init__(self, controllers):
        super().__init__(self.__class__.__name__, controllers)
        self.driver = UiDriver(self.device1)
        self.background_cycles = int(os.getenv("DOUYU_BACKGROUND_CYCLES", "3"))
        self.action_wait = float(os.getenv("DOUYU_ACTION_WAIT", "2"))
        self.search_term = os.getenv("DOUYU_SEARCH_TERM", "pubg")
        self.closed = False

    def _wait(self, seconds=None):
        self.driver.wait(self.action_wait if seconds is None else seconds)

    def _find(self, selector):
        try:
            return self.driver.find_component(selector)
        except Exception:
            return None

    def _open_search_results(self):
        Step("搜索正在直播的房间")
        # Focusing the home search field replaces its placeholder widget, so
        # use a coordinate target instead of retaining a now-stale component.
        self.driver.input_text((0.4, 0.095), self.search_term)
        self._wait(1)

        suggestion = self._find(BY.text(self.search_term).type("Text"))
        if suggestion is not None:
            self.driver.touch(suggestion, wait_time=0.5)
        else:
            self.driver.touch((0.06, 0.12), wait_time=0.5)
        self._wait(4)

    def _enter_live_room(self):
        Step("进入一个新的直播间")
        for title in self.ROOM_TITLES:
            room = self._find(BY.text(title))
            if room is not None:
                self.driver.touch(room, wait_time=1)
                self._wait(4)
                return

        # Search results use a stable four-column layout on HarmonyOS PC.
        self.driver.touch((0.14, 0.61), wait_time=1)
        self._wait(4)

    def _exercise_room(self):
        Step("模拟观看并切换直播间信息页")
        video_tab = self._find(BY.text("视频"))
        if video_tab is not None:
            self.driver.touch(video_tab, wait_time=0.5)
            self._wait(1)
        chat_tab = self._find(BY.text("聊天"))
        if chat_tab is not None:
            self.driver.touch(chat_tab, wait_time=0.5)
            self._wait(1)

        video = self._find(BY.key(self.VIDEO_KEY))
        if video is not None:
            self.driver.touch(video, wait_time=0.5)
            self._wait(1)
            video = self._find(BY.key(self.VIDEO_KEY))
            if video is not None:
                self.driver.touch(video, wait_time=0.5)
            self._wait(1)

    def _background_and_restore(self, cycle):
        Step(f"前后台切换 {cycle + 1}/{self.background_cycles}")
        minimize = self._find(BY.key(self.MINIMIZE_KEY))
        if minimize is not None:
            self.driver.touch(minimize, wait_time=0.5)
        else:
            self.driver.press_key(KeyCode.HOME)
        self._wait()

        self.driver.start_app(self.BUNDLE, self.ABILITY, wait_time=self.action_wait)
        self._wait()

    def setup(self):
        Step("启动斗鱼")
        self.driver.start_app(self.BUNDLE, self.ABILITY, wait_time=3)
        self._wait(2)

        # The app may restore the last live room. Return to search/results first.
        if self._find(BY.key(self.VIDEO_KEY)) is not None:
            Step("退出上次恢复的直播间")
            self.driver.press_key(KeyCode.BACK)
            self._wait(3)

    def process(self):
        self._open_search_results()
        self._enter_live_room()

        if self._find(BY.key(self.VIDEO_KEY)) is None:
            raise RuntimeError("未进入直播间：找不到 gesture_play 控件")

        self._exercise_room()
        for cycle in range(self.background_cycles):
            self._background_and_restore(cycle)

        Step("关闭斗鱼")
        close = self._find(BY.key(self.CLOSE_KEY))
        if close is not None:
            self.driver.touch(close, wait_time=1)
            self._wait(2)
        self.driver.stop_app(self.BUNDLE, wait_time=1)
        self.closed = True

    def teardown(self):
        if not self.closed:
            self.driver.stop_app(self.BUNDLE, wait_time=1)
