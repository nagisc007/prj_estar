# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.s100 import config as cnf
THM = cnf.THEMES


# episodes
def ep_intro(w: wd.World):
    h, osaki, fuyumi, ft_fuyumi = w.hero, w.osaki, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("追い詰められた作家の苦悩",
                w.tag.comment("主人公の人間性紹介と彼女との状況設定"),
                h.be(w.stage.apart, w.day.current),
                h.do("phone", w.osaki, "原稿締め切り", w.stage.indream),
                h.do("wake", "メール着信音"),
                h.deal(fuyumi, "普段メールよこさない彼女から", THM["2"]),
                h.do("返信しない"),
                h.hear("再度着信音"),
                h.look("押入れの中から"),
                h.look(w.terminal, THM["3"]),
                h.have(w.terminal),
                h.deal(w.fear_mail, THM["1"]),
                h.do("write", "$must"),
                h.do("write", w.i.novel),
                ),
            w.scene("未来人の隣人",
                h.hear("インタフォン"),
                h.look(fuyumi),
                h.ask(fuyumi, "ごめんまだメール見てない"),
                ft_fuyumi.talk("何のこと？"),
                h.look(ft_fuyumi, "冷たく豹変", THM["4"]),
                ft_fuyumi.ask("中に入れてくれない？"),
                ),
            ]
    return [w.chaptertitle("冒頭"),
            *scenes,
            ]


def ep_middle(w: wd.World):
    h, fuyumi, ft_fuyumi = w.hero, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("もう一人の冬美",
                ft_fuyumi.explain(h, "隣に越してきた", THM["8"]),
                h.look(ft_fuyumi),
                ft_fuyumi.talk("相談"),
                h.know(ft_fuyumi, w.ichioku, THM["7"]),
                h.remember(fuyumi, "機械音痴", THM["11"]),
                h.know(ft_fuyumi, w.i.future_mail, THM["12"]),
                ),
            w.scene("学生時代",
                h.remember(w.day.schoolday),
                h.be(w.i.lostmemory, THM["19"]),
                h.meet(ft_fuyumi, "あの時の女性"),
                h.deal(w.terminal, "時間を戻る"),
                h.be("透明人間として", THM["17"]),
                ft_fuyumi.talk("ずっと待ってる", THM["18"]),
                ),
            w.scene("現在の自分は",
                h.have("コーヒーと煙草", THM["20"]),
                h.remember("当時は言えなかった秘密の趣味＝妄想小説", THM["21"]),
                h.think("あの頃のキラキラがない", THM["22"]),
                h.have(w.nishikawa, "著作"),
                h.think("同期", "面白くて悔しい", THM["23"]),
                ),
            w.scene("未来からの警告",
                h.be(w.stage.apart, w.day.current),
                h.think(w.i.future_mail),
                h.have(fuyumi, w.i.fuyumi_call),
                h.talk(fuyumi, "別離"),
                h.talk("説得", fuyumi),
                h.look(fuyumi, "自分の小説", "彼女に自分の才能を示す"),
                h.have(w.i.help_mail, "助けて", THM["24"]),
                h.look("未来の自分からだった", THM["27"]),
                ),
            ]
    return [w.chaptertitle("展開"),
            *scenes,
            ]


def ep_climax(w: wd.World):
    h = w.hero
    scenes = [
            w.scene("そして自分が死ぬ",
                h.be(w.stage.apart, w.day.current),
                h.think(w.i.help_mail),
                h.do("help", w.futureman),
                h.know(w.futureman, "dead"),
                h.do(w.futureman, "小説を書く"),
                h.be("dead"),
                ),
            ]
    return [w.chaptertitle("これ以上書けない"),
            *scenes,
            ]


def ep_end(w: wd.World):
    h = w.hero
    scenes = [
            w.scene("過去の自分",
                h.be("dead"),
                h.deal(w.terminal),
                h.go("過去に戻る", w.day.schoolday),
                h.go(w.stage.school),
                h.meet(w.pastman),
                ),
            w.scene("小説を書く意味",
                h.know(w.i.his_reason),
                h.be("未解決テーマ",
                    THM["5"],
                    THM["6"],
                    THM["9"],
                    THM["10"],
                    THM["13"],
                    THM["14"],
                    THM["15"],
                    THM["16"],
                    THM["25"],
                    THM["26"],
                    THM["28"],
                    THM["29"],
                    THM["30"],
                    THM["31"],
                    THM["32"],
                    THM["33"],
                    THM["34"],
                    THM["35"],
                    THM["36"],
                    THM["37"],
                    THM["38"],
                    THM["39"],
                    THM["40"],
                    THM["41"],
                    THM["42"],
                    THM["43"],
                    THM["44"],
                    THM["45"],
                    THM["46"],
                    THM["47"],
                    THM["48"],
                    THM["49"],
                    THM["50"],
                    THM["51"],
                    THM["52"],
                    THM["53"],
                    THM["54"],
                    THM["55"],
                    THM["56"],
                    THM["57"],
                    THM["58"],
                    THM["59"],
                    THM["60"],
                    THM["61"],
                    THM["62"],
                    THM["63"],
                    THM["64"],
                    THM["65"],
                    THM["66"],
                    THM["67"],
                    THM["68"],
                    THM["69"],
                    THM["70"],
                    THM["71"],
                    THM["72"],
                    THM["73"],
                    THM["74"],
                    THM["75"],
                    THM["76"],
                    THM["77"],
                    THM["78"],
                    THM["79"],
                    THM["80"],
                    THM["81"],
                    THM["82"],
                    THM["83"],
                    THM["84"],
                    THM["85"],
                    THM["86"],
                    THM["87"],
                    THM["88"],
                    THM["89"],
                    THM["90"],
                    THM["91"],
                    THM["92"],
                    THM["93"],
                    THM["94"],
                    THM["95"],
                    THM["96"],
                    THM["97"],
                    THM["98"],
                    THM["99"],
                    THM["100"],
                    ),
                ),
            ]
    return [w.chaptertitle("最後の作品"),
            *scenes,
            ]


# main
def world():
    w = wd.World("100 stories project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS)
    return w


def story(w: wd.World):
    return [w.maintitle("百妄想騙り"),
            ep_intro(w),
            ep_middle(w),
            ep_climax(w),
            ep_end(w),
            ]


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

